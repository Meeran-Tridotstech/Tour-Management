# Copyright (c) 2025, GoFly Journeys and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class Payment(Document):
    def before_insert(self):
        if not self.payment_id:
            # Example: PAY-20251012-0001
            last_payment = frappe.db.sql("""
                SELECT payment_id FROM `tabPayment`
                ORDER BY creation DESC LIMIT 1
            """)
            last_num = 1
            if last_payment and last_payment[0][0]:
                try:
                    last_num = int(last_payment[0][0].split("-")[-1]) + 1
                except Exception:
                    last_num = 1
            self.payment_id = f"PAY-{nowdate().replace('-', '')}-{last_num:04d}"

    def validate(self):
        self.validate_amounts()

    def validate_amounts(self):
        # Ensure numeric fields are not negative
        for field in ["amount", "visa_amount", "advance_amount"]:
            value = getattr(self, field, None)
            if value is None:
                frappe.throw(f"{field.replace('_', ' ').title()} is required.")
            elif value < 0:
                frappe.throw(f"{field.replace('_', ' ').title()} cannot be negative.")

        # ✅ Calculate total_amount = package + visa
        self.total_amount = (self.amount or 0) + (self.visa_amount or 0)

        # ✅ Validate advance_amount <= total_amount
        if self.advance_amount > self.total_amount:
            frappe.throw("Advance Amount cannot be greater than Total Amount.")

        # ✅ Calculate balance_amount (only if not manually updated)
        if not self.balance_amount or self.balance_amount == 0:
            self.balance_amount = self.total_amount - (self.advance_amount or 0)

        # ✅ Validation for zero total
        if self.total_amount <= 0:
            frappe.throw("Total Amount must be greater than zero.")