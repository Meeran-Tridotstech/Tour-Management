frappe.ui.form.on("Payment", {
    refresh(frm) {
        gofly.common.add_open_related_button(frm);
        const paymentCount = frm.doc.payment_count || 0;
        const balance = frm.doc.balance_amount || 0;
        const total = frm.doc.total_amount || 0;
        const status = frm.doc.payment_status || "";

        // 🔒 Hide payment-related fields if payment is completed
        if (status === "Completed") {
            frm.set_df_property("balance_amount", "hidden", 1);
            frm.set_df_property("payment_count", "hidden", 1);
            frm.set_df_property("pay_amount", "hidden", 1);
            return;
        }

        // 💳 Show Pay Now button if payment not completed
        frm.add_custom_button("💳 Pay Now", () => {
            make_razorpay_payment(frm);
        });

        // Reset read-only each refresh
        frm.set_df_property("pay_amount", "read_only", 0);

        // 🟢 First Payment — set 50% of total
        if (paymentCount === 0 && total > 0) {
            if (!frm.doc.balance_amount || frm.doc.balance_amount === 0) {
                frm.set_value("balance_amount", total);
            }

            const first_installment = Math.round(total / 2);
            if (!frm.doc.pay_amount || frm.doc.pay_amount === 0) {
                frm.set_value("pay_amount", first_installment);
                frappe.show_alert({ message: `First payment ₹${first_installment} set`, indicator: "blue" });
            }
            frm.set_df_property("pay_amount", "read_only", 1);
        }

        // 🟠 Second Payment — auto-fill remaining balance
        if (paymentCount === 1 && balance > 0) {
            frm.set_value("pay_amount", balance);
            frm.set_df_property("pay_amount", "read_only", 1);
            frappe.show_alert({ message: `Final payment ₹${balance} auto-filled`, indicator: "blue" });
        }
    }
});


function make_razorpay_payment(frm) {
    let payAmount = parseFloat(frm.doc.pay_amount || 0);
    let balance = parseFloat(frm.doc.balance_amount || 0);
    const total = parseFloat(frm.doc.total_amount || 0);
    const paymentCount = frm.doc.payment_count || 0;

    // ✅ Validations
    if (payAmount <= 0) {
        frappe.msgprint("Please enter a valid Pay Amount.");
        return;
    }
    if (balance <= 0) {
        frappe.msgprint("Nothing to pay. Balance is zero.");
        return;
    }
    if (payAmount > balance) {
        frappe.show_alert({ message: `Pay Amount exceeds remaining balance. Adjusted to ₹${balance}.`, indicator: "orange" });
        payAmount = balance;
    }
    if (paymentCount >= 2) { // changed from 3 to 2
        frappe.msgprint("You can make a maximum of 2 payments for this booking.");
        return;
    }

    const amount_in_paise = Math.round(payAmount * 100);

    const options = {
        key: "rzp_test_1DP5mmOlF5G5ag",
        amount: amount_in_paise,
        currency: "INR",
        name: frm.doc.customer || "Customer",
        description: `Payment for Booking: ${frm.doc.booking || frm.doc.name}`,

        handler: function (response) {
            const now = frappe.datetime.now_datetime();
            const oldHistory = frm.doc.payment_history || "";
            const newEntry = `
                <div style="padding:8px 10px; border-left:4px solid #10b981; margin-bottom:8px;">
                    <b style="color:#10b981">Payment ID:</b> ${response.razorpay_payment_id}<br>
                    <b>Amount:</b> ₹${payAmount}<br>
                    <b>Date:</b> ${now}
                </div>
            `;
            const newHistory = newEntry + oldHistory;

            const newCount = paymentCount + 1;
            let newBalance = parseFloat((balance - payAmount).toFixed(2));

            // ✅ Final payment = set balance to 0
            if (newCount >= 2 || newBalance <= 0.009) {
                newBalance = 0;
            }

            // 🧮 Next installment if not complete
            let nextPay = 0;
            if (newBalance > 0) {
                const remaining_installments = Math.max(1, 2 - newCount); // changed to 2
                nextPay = Math.round(newBalance / remaining_installments);
                if (nextPay > newBalance) nextPay = newBalance;
            }

            // 🔄 Update fields
            frm.set_value("payment_history", newHistory);
            frm.set_value("balance_amount", newBalance);
            frm.set_value("payment_count", newCount);
            frm.set_value("pay_amount", nextPay);

            // ✅ Update status
            if (newBalance === 0) {
                frm.set_value("payment_status", "Completed");
                frappe.show_alert({ message: "✅ All payments completed successfully!", indicator: "green" });

                frm.set_df_property("balance_amount", "hidden", 1);
                frm.set_df_property("payment_count", "hidden", 1);
                frm.set_df_property("pay_amount", "hidden", 1);
            } else {
                frm.set_value("payment_status", "Partially Paid");
                frappe.show_alert({ message: `💸 ₹${payAmount} paid. Remaining: ₹${newBalance}`, indicator: "blue" });
                frm.set_df_property("pay_amount", "read_only", 1);
            }

            // 💾 Save Payment Doc
            frm.save().then(() => {
                // 🔗 Update related Booking after first payment
                if (newCount === 1 && frm.doc.booking) {
                    frappe.db.set_value("Booking", frm.doc.booking, "booking_status", "Booked")
                        .then(() => {
                            frappe.show_alert({ message: "Booking status updated to 'Booked'", indicator: "green" });
                            frappe.msgprint("Booking status has been updated to 'Booked'.");
                            frappe.set_route("Form", "Booking", frm.doc.booking);
                        });
                } else {
                    frm.reload_doc();
                }
            });
        },

        prefill: {
            name: frm.doc.customer || "Test User",
            email: frm.doc.email || "test@example.com",
            contact: frm.doc.mobile || "9999999999"
        },
        theme: { color: "#3399cc" },
        modal: {
            ondismiss: function () {
                frappe.msgprint("Payment popup closed before completion.");
            }
        }
    };

    const rzp = new Razorpay(options);
    rzp.open();
}