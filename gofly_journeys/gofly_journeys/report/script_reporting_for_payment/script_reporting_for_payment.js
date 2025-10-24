// Copyright (c) 2025, GoFly Journeys and contributors
// For license information, please see license.txt

// frappe.query_reports["script reporting for payment"] = {
// 	"filters": [

// 	]
// };
frappe.query_reports["Script Reporting for Payment"] = {
    "filters": [
        {
            "fieldname": "customer",
            "label": __("Customer"),
            "fieldtype": "Link",
            "options": "Customer"
        },
        {
            "fieldname": "booking",
            "label": __("Booking"),
            "fieldtype": "Link",
            "options": "Booking"
        },
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1)
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today()
        }
    ]
};
