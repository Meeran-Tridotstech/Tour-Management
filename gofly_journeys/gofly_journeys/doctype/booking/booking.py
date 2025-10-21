# Copyright (c) 2025, GoFly Journeys and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class Booking(Document):		

	def validate(self):
		# Validation checks
		if self.return_date < self.travel_date:
			frappe.throw("Return Date cannot be earlier than the Travel Date.")
		
		if str(self.travel_date) < nowdate():
			frappe.throw("Travel date cannot be in the past")
		# ✅ Only run when Booking is submitted
		if self.booking_status == "Booked":
			# Check if already created to avoid duplicates
			existing = frappe.db.exists("Tour Staff Assignment", {"booking": self.name})
			if not existing:
				new_assignment = frappe.get_doc({
					"doctype": "Tour Staff Assignment",
					"booking": self.name,
					"customer": self.customer
				})
				new_assignment.insert()
				frappe.msgprint(f"✅ Tour Staff Assignment created for booking {self.name}")


	def on_update(self):
		# ✅ When Booking status becomes "Booked", create a Tour Staff Assignment record
		if self.booking_status == "Booked":
			# Check if already created to avoid duplicates
			existing = frappe.db.exists("Tour Staff Assignment", {"booking": self.name})
			if not existing:
				new_assignment = frappe.get_doc({
					"doctype": "Tour Staff Assignment",
					"booking": self.name,
					"customer": self.customer
				})
				new_assignment.insert()
				frappe.msgprint(f"✅ Tour Staff Assignment created for booking {self.name}")

			# ✅ Submit the Booking document if not already submitted
			if not self.docstatus:  # docstatus 0 = Draft
				frappe.msgprint(f"✅ Booking {self.name} is being submitted automatically")
				self.db_set("booking_status", "Booked")  # make sure field is saved
				self.submit()
				
				# Refresh the form on UI
				frappe.msgprint(f"✅ Booking {self.name} submitted successfully")
				frappe.local.flags.update_ui = True


#Guide Filter Based on Package Country and state
# @frappe.whitelist()
# def get_guide_query(doctype, txt, searchfield, start, page_len, filters):
#     docname = filters.get("docname")
#     if not docname:
#         return []

#     booking = frappe.get_doc("Booking", docname)
    
#     # Example: Get guides based on package country/state
#     guides = frappe.get_all(
#         "Guide",
#         filters={
#             "country": booking.package_country,
#             "state": booking.package_state
#         },
#         fields=["name", "full_name"],
#         limit_start=start,
#         limit_page_length=page_len
#     )

#     # Must return a list of lists
#     return [[g.name, g.full_name] for g in guides]

@frappe.whitelist()
def get_guide_query(doctype, txt, searchfield, start, page_len, filters):
    docname = filters.get("docname")
    if not docname:
        return []

    booking = frappe.get_doc("Booking", docname)
    
    # Get guides where country OR state matches
    guides = frappe.db.get_all(
        "Guide",
        or_filters=[
            ["Guide", "country", "=", booking.package_country],
            ["Guide", "state", "=", booking.package_state]
        ],
        fields=["name", "full_name"],
        limit_start=start,
        limit_page_length=page_len,
        order_by="name"
    )

    # Return list of lists for search_link
    return [[g.name, g.full_name] for g in guides]

