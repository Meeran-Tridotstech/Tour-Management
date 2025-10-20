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
