# Copyright (c) 2025, GoFly Journeys and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address

class Customer(Document):
    def validate(self):
        # Full Name
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        elif self.first_name:
            self.full_name = self.first_name
        elif self.last_name:
            self.full_name = self.last_name

        # Pincode validation
        if self.postal_code:
            pincode = str(self.postal_code)
            if not pincode.isdigit():
                frappe.throw("Pincode must contain only digits")
            if len(pincode) != 6:
                frappe.throw("Pincode must be exactly 6 digits")

        # Email validation
        if self.email_address:
            if not validate_email_address(self.email_address):
                frappe.throw("Please enter a valid Email Address")
