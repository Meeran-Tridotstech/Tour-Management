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
		# ✅ Run only when Booking status is "Booked"
		if self.booking_status != "Booked":
			return

		# ✅ 1. Create Tour Staff Assignment (avoid duplicates)
		existing_assignment = frappe.db.exists("Tour Staff Assignment", {"booking": self.name})
		if not existing_assignment:
			new_assignment = frappe.get_doc({
				"doctype": "Tour Staff Assignment",
				"booking": self.name,
				"customer": self.customer
			})
			new_assignment.insert()
			frappe.msgprint(f"✅ Tour Staff Assignment created for booking {self.name}")
		else:
			frappe.msgprint("ℹ️ Tour Staff Assignment already exists for this booking.")

		# # ✅ 2. Get Guide ID from Tour Staff Assignment
		# tsa = frappe.get_all("Tour Staff Assignment", filters={"booking": self.name}, limit=1)
		# guide_id = None
		# if tsa:
		# 	tsa_doc = frappe.get_doc("Tour Staff Assignment", tsa[0].name)
		# 	guide_id = tsa_doc.guide_id

		# ✅ 3. Create Travel Plan (avoid duplicates)
		existing_travel = frappe.db.exists("Travel Plan", {"booking": self.name})
		if not existing_travel:
			travel_plan = frappe.get_doc({
				"doctype": "Travel Plan",
				"booking": self.name
				
			})
			travel_plan.insert()
			frappe.msgprint(f"✅ Travel Plan created for Booking {self.name} with Guide Not Assigned")
		else:
			frappe.msgprint("ℹ️ Travel Plan already exists for this booking.")

		# ✅ 4. Auto-submit if still Draft
		if not self.docstatus:  # 0 = Draft
			self.submit()
			frappe.msgprint(f"✅ Booking {self.name} submitted successfully")			
     

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

