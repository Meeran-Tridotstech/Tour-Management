# Copyright (c) 2025, GoFly Journeys and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate
from frappe.utils import today
import re


class Booking(Document):
	def validate(self):
		if self.return_date < self.travel_date:
			frappe.throw("Return Date cannot be earlier than the Travel Date.")
		
		if self.travel_date < nowdate():
			frappe.throw("Travel Date cannot be in the past.")