# Copyright (c) 2025, GoFly Journeys and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, 

import frappe
from frappe import _

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_data(filters)

    return columns, data

def get_columns():
    return [
        {"label": _("Payment ID"), "fieldname": "name", "fieldtype": "Link", "options": "Payment", "width": 120},
        {"label": _("Customer"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 150},
        {"label": _("Booking"), "fieldname": "booking", "fieldtype": "Link", "options": "Booking", "width": 150},
        {"label": _("Payment Date"), "fieldname": "payment_date", "fieldtype": "Date", "width": 120},
        {"label": _("Package Amount"), "fieldname": "package_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Visa Amount"), "fieldname": "visa_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Total Amount"), "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Advance Amount"), "fieldname": "advance_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Balance Amount"), "fieldname": "balance_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Payment Count"), "fieldname": "payment_count", "fieldtype": "Int", "width": 100},
        {"label": _("Note"), "fieldname": "note", "fieldtype": "Data", "width": 200},
        {"label": _("Payment Status"), "fieldname": "payment_status", "fieldtype": "Data", "width": 120},
        {"label": _("Pay Amount"), "fieldname": "pay_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Sender Email"), "fieldname": "sender_email", "fieldtype": "Data", "width": 150},
        {"label": _("Payment History"), "fieldname": "payment_history", "fieldtype": "Data", "width": 200},
    ]

def get_data(filters):
    conditions = []
    values = {}

    if filters.get("customer"):
        conditions.append("customer = %(customer)s")
        values["customer"] = filters["customer"]

    if filters.get("booking"):
        conditions.append("booking = %(booking)s")
        values["booking"] = filters["booking"]

    if filters.get("from_date") and filters.get("to_date"):
        conditions.append("payment_date BETWEEN %(from_date)s AND %(to_date)s")
        values["from_date"] = filters["from_date"]
        values["to_date"] = filters["to_date"]

    condition_str = " AND " + " AND ".join(conditions) if conditions else ""

    query = f"""
        SELECT
            name,
            customer,
            booking,
            payment_date,
            amount AS package_amount,
            IFNULL(visa_amount, 0) AS visa_amount,
            IFNULL(total_amount, amount) AS total_amount,
            IFNULL(advance_amount, 0) AS advance_amount,
            (IFNULL(total_amount, amount) - IFNULL(advance_amount, 0)) AS balance_amount,
            (
                SELECT COUNT(*) FROM `tabPayment` p2 WHERE p2.booking = p1.booking
            ) AS payment_count,
            payment_status,
            IFNULL(pay_amount, 0) AS pay_amount,
            sender_email,
            IFNULL(payment_history, "") AS payment_history
        FROM `tabPayment` p1
        WHERE docstatus = 1 {condition_str}
        ORDER BY payment_date DESC
    """

    data = frappe.db.sql(query, values, as_dict=True)

    # Add note if payment_count >= 3
    for d in data:
        if d.get("payment_count") and d["payment_count"] >= 3:
            d["note"] = "⚠️ You can only make 3 payments for this booking"
        else:
            d["note"] = ""

    return data





