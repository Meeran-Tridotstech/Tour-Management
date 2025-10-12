import frappe
from frappe.utils import now_datetime

@frappe.whitelist()
def handle_razorpay_success(payment_id, razorpay_payment_id):
    payment = frappe.get_doc("Payment", payment_id)

    # Store payment info
    payment.razorpay_payment_id = razorpay_payment_id
    payment.payment_status = "Paid"

    # Store history text (append mode)
    current_entry = f"Paid {payment.balance_amount} on {now_datetime()} | Razorpay ID: {razorpay_payment_id}"
    if payment.payment_history:
        payment.payment_history += f"\n{current_entry}"
    else:
        payment.payment_history = current_entry

    # Once paid, clear the balance
    payment.balance_amount = 0

    payment.save(ignore_permissions=True)
    frappe.db.commit()

    return {"message": "Payment recorded successfully"}
