import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Payment Id"), "fieldname": "payment_id", "fieldtype": "Data", "width": 120},
        {"label": _("Customer"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 150},
        {"label": _("Booking"), "fieldname": "booking", "fieldtype": "Link", "options": "Booking", "width": 120},
        {"label": _("Payment Date"), "fieldname": "payment_date", "fieldtype": "Date", "width": 100},
        {"label": _("Amount"), "fieldname": "amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Visa Amount"), "fieldname": "visa_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Total Amount"), "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Advance Amount"), "fieldname": "advance_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Balance Amount"), "fieldname": "balance_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Payment Count"), "fieldname": "payment_count", "fieldtype": "Int", "width": 100},
        {"label": _("Payment Status"), "fieldname": "payment_status", "fieldtype": "Data", "width": 120},
        {"label": _("Pay Amount"), "fieldname": "pay_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Sender Email"), "fieldname": "sender_email", "fieldtype": "Data", "width": 150},
        {"label": _("Payment History"), "fieldname": "payment_history", "fieldtype": "Data", "width": 200},
    ]

    conditions = []
    values = []

    if filters:
        if filters.get("customer"):
            conditions.append("customer=%s")
            values.append(filters.get("customer"))
        if filters.get("booking"):
            conditions.append("booking=%s")
            values.append(filters.get("booking"))
        if filters.get("payment_status"):
            conditions.append("payment_status=%s")
            values.append(filters.get("payment_status"))

    condition_sql = " AND ".join(conditions) if conditions else "1=1"

    payments = frappe.db.sql(f"""
        SELECT
            name as payment_id,
            customer,
            booking,
            payment_date,
            amount,
            visa_amount,
            total_amount,
            advance_amount,
            total_amount - advance_amount as balance_amount,
            (SELECT COUNT(*) FROM `tabPayment` p2 WHERE p2.booking = p1.booking) as payment_count,
            payment_status,
            pay_amount,
            sender_email,
            payment_history
        FROM `tabPayment` p1
        WHERE {condition_sql}
        ORDER BY customer
    """, tuple(values), as_dict=True)

    # Add warning for >3 payments
    for payment in payments:
        if payment["payment_count"] >= 3:
            payment["payment_history"] = (payment["payment_history"] or "") + " ⚠️ Max 3 payments reached"

    return columns, payments





