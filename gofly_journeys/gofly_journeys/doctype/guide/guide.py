# Copyright (c) 2025, GoFly Journeys and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address

class Guide(Document):
    def validate(self):
        if getattr(self, "email", None):  # safely check if field exists
            if not validate_email_address(self.email):
                frappe.throw("Please enter a valid Email Address")

