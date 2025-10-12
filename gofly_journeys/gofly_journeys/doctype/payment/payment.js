
frappe.ui.form.on("Payment", {
    refresh(frm) {
        // Add "Pay Now" button if payment not completed
        if (frm.doc.payment_status !== "Completed") {
            frm.add_custom_button("Pay Now", () => {
                make_razorpay_payment(frm);
            }, "Actions");
        }

        const paymentCount = frm.doc.payment_count || 0;

        // Reset read-only
        frm.set_df_property("pay_amount", "read_only", 0);

        // 1️⃣ First Payment — auto set Advance amount
        if (paymentCount === 0 && frm.doc.advance_amount > 0) {
            if (!frm.doc.pay_amount || frm.doc.pay_amount === 0) {
                frm.set_value("pay_amount", frm.doc.advance_amount);
                frappe.msgprint(`Advance amount ₹${frm.doc.advance_amount} set for first payment.`);
            }
            frm.set_df_property("pay_amount", "read_only", 1);
        }

        // 3️⃣ Third Payment — auto set remaining balance
        if (paymentCount === 2 && frm.doc.balance_amount > 0) {
            if (!frm.doc.pay_amount || frm.doc.pay_amount === 0) {
                frm.set_value("pay_amount", frm.doc.balance_amount);
                frappe.msgprint(`Remaining balance ₹${frm.doc.balance_amount} auto-filled for final payment.`);
            }
            frm.set_df_property("pay_amount", "read_only", 1);
        }

    }
});

function make_razorpay_payment(frm) {
    const payAmount = frm.doc.pay_amount || 0;
    const balance = frm.doc.balance_amount || 0;
    const paymentCount = frm.doc.payment_count || 0;

    // Validations
    if (payAmount <= 0) {
        frappe.msgprint("Please enter a valid Pay Amount.");
        return;
    }
    if (payAmount > balance) {
        frappe.msgprint("Pay Amount cannot exceed Balance Amount.");
        return;
    }
    if (paymentCount >= 3) {
        frappe.msgprint("You can only make 3 payments for this booking.");
        return;
    }

    // Convert to paise for Razorpay
    const amount_in_paise = payAmount * 100;

    let options = {
        key: "rzp_test_1DP5mmOlF5G5ag", // Replace with live key in production
        amount: amount_in_paise,
        currency: "INR",
        name: frm.doc.customer || "Customer",
        description: `Payment for Booking ID: ${frm.doc.name}`,
        handler: function (response) {
            const now = frappe.datetime.now_datetime();

            // Append payment history
            const oldHistory = frm.doc.payment_history || "";
            const newHistory = `<b style="color:green">* Payment ID:</b> ${response.razorpay_payment_id} \n<b style="color:green">   Amount: </b>₹${payAmount} \n<b style="color:green">   Date:</b> ${now}\n\n` + oldHistory;

            // Update balance
            let newBalance;
            if (paymentCount === 0) {
                newBalance = balance; // advance already counted
            } else {
                newBalance = balance - payAmount;
            }

            const newCount = paymentCount + 1;

            frm.set_value("payment_history", newHistory);
            frm.set_value("balance_amount", newBalance);
            frm.set_value("pay_amount", 0);
            frm.set_value("payment_count", newCount);

            if (newBalance <= 0) {
                frm.set_value("payment_status", "Completed");
                frappe.msgprint("🎉 All payments completed successfully!");
            } else {
                frm.set_value("payment_status", "Partially Paid");
                frappe.msgprint(`✅ ₹${payAmount} paid.\nRemaining balance: ₹${newBalance}`);

                if (newCount === 2 && newBalance > 0) {
                    frm.set_value("pay_amount", newBalance);
                    frm.set_df_property("pay_amount", "read_only", 1);
                    frappe.msgprint(`Auto-filled remaining ₹${newBalance} for final payment.`);
                }
            }

            frm.save_or_submit();
        },
        prefill: {
            name: frm.doc.customer || "Test User",
            email: frm.doc.email || "test@example.com",
            contact: frm.doc.mobile || "9999999999"
        },
        theme: {
            color: "#3399cc"
        },
        modal: {
            ondismiss: function () {
                frappe.msgprint("You closed the Razorpay popup.");
            }
        }
    };

    let rzp = new Razorpay(options);
    rzp.open();
}
