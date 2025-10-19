frappe.ui.form.on("Payment", {
    refresh(frm) {
        // Add "Pay Now" button if payment not completed
        if (frm.doc.payment_status !== "Completed") {
            frm.add_custom_button("💳 Pay Now", () => {
                make_razorpay_payment(frm);
            }, "Actions");
        }

        const paymentCount = frm.doc.payment_count || 0;
        const balance = frm.doc.balance_amount || 0;
        const advance = frm.doc.advance_amount || 0;

        // Reset read-only state each refresh
        frm.set_df_property("pay_amount", "read_only", 0);

        // 1️⃣ First Payment — set Advance amount
        if (paymentCount === 0 && advance > 0) {
            if (!frm.doc.pay_amount || frm.doc.pay_amount === 0) {
                frm.set_value("pay_amount", advance);
                frappe.msgprint(`💰 Advance amount ₹${advance} set for first payment.`);
            }
            frm.set_df_property("pay_amount", "read_only", 1);
        }

        // 3️⃣ Third Payment — set remaining balance automatically
        if (paymentCount === 2 && balance > 0) {
            if (!frm.doc.pay_amount || frm.doc.pay_amount === 0) {
                frm.set_value("pay_amount", balance);
                frappe.msgprint(`💰 Final payment ₹${balance} auto-filled.`);
            }
            frm.set_df_property("pay_amount", "read_only", 1);
        }
    }
});


function make_razorpay_payment(frm) {
    const payAmount = frm.doc.pay_amount || 0;
    const balance = frm.doc.balance_amount || 0;
    const paymentCount = frm.doc.payment_count || 0;

    // ✅ Basic validations
    if (payAmount <= 0) {
        frappe.msgprint("Please enter a valid Pay Amount.");
        return;
    }
    if (payAmount > balance) {
        frappe.msgprint("Pay Amount cannot exceed Balance Amount.");
        return;
    }
    if (paymentCount >= 3) {
        frappe.msgprint("You can make a maximum of 3 payments for this booking.");
        return;
    }

    // Convert to paise for Razorpay
    const amount_in_paise = payAmount * 100;

    const options = {
        key: "rzp_test_1DP5mmOlF5G5ag", // replace with live key later
        amount: amount_in_paise,
        currency: "INR",
        name: frm.doc.customer || "Customer",
        description: `Payment for Booking: ${frm.doc.booking || frm.doc.name}`,
        handler: function (response) {
            const now = frappe.datetime.now_datetime();
            const oldHistory = frm.doc.payment_history || "";
            const newEntry = `
                <b style="color:green">* Payment ID:</b> ${response.razorpay_payment_id}<br>
                <b style="color:green">Amount:</b> ₹${payAmount}<br>
                <b style="color:green">Date:</b> ${now}<br><br>
            `;
            const newHistory = newEntry + oldHistory;

            const newCount = paymentCount + 1;
            const newBalance = balance - payAmount;

            // Update form values
            frm.set_value("payment_history", newHistory);
            frm.set_value("balance_amount", newBalance);
            frm.set_value("payment_count", newCount);
            frm.set_value("pay_amount", 0);

            if (newBalance <= 0) {
                frm.set_value("payment_status", "Completed");
                frappe.msgprint("✅ All payments completed successfully!");
            } else {
                frm.set_value("payment_status", "Partially Paid");
                frappe.msgprint(`💸 ₹${payAmount} paid. Remaining balance: ₹${newBalance}`);

                // Auto-fill for final payment
                if (newCount === 2 && newBalance > 0) {
                    frm.set_value("pay_amount", newBalance);
                    frm.set_df_property("pay_amount", "read_only", 1);
                    frappe.msgprint(`💰 Auto-filled final payment ₹${newBalance}.`);
                }
            }

            // Save updated record
            frm.save();
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
                frappe.msgprint("Payment popup closed before completion.");
            }
        }
    };

    const rzp = new Razorpay(options);
    rzp.open();
}
