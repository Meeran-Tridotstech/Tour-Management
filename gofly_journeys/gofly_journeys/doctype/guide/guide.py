# Copyright (c) 2025, GoFly Journeys and contributors
# For license information, please see license.txt
import re
import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address

class Guide(Document):
    def validate(self):
        #Email Validation:
        #----------------
        if getattr(self, "email", None):  # safely check if field exists
            if not validate_email_address(self.email):
                frappe.throw("Please enter a valid Email Address")
    
        #Passport Validation
        #------------------
        if self.passport:
                # Example pattern: 1 uppercase letter + 7 digits
                pattern = r'^[A-Z]{1}\d{7}$'
                if not re.match(pattern, self.passport):
                    frappe.throw("Invalid passport number. Format should be: A1234567")