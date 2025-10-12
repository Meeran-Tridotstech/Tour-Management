# Copyright (c) 2025, GoFly Journeys and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate
from frappe.utils import today
import re



class Booking(Document):
	def validate(self):
		if self.visa_required:
			required_fields = ['passport_no', 'visa_type', 'visa_documents']
			for field in required_fields:
				if not self.get(field):
					frappe.throw(f"Please fill {field.replace('_', ' ').title()} before submitting visa booking.")
		
		if self.return_date < self.travel_date:
			frappe.throw("Return Date cannot be earlier than the Travel Date.")
		
		if self.travel_date < nowdate():
			frappe.throw("Travel Date cannot be in the past.")
			
		if self.visa_approved_date and self.visa_applied_date:
			if self.visa_approved_date < self.visa_applied_date:
				frappe.throw("Visa Approved Date cannot be earlier than Visa Applied Date.")

		self.validate_passport_no()
		# self.validate_visa_no()
		self.validate_dates()
		self.validate_visa_fee()


	def validate_passport_no(self):
			"""
			Validate passport number (Example: 1 letter + 7 digits, e.g. A1234567)
			"""
			if self.passport_no:
				pattern = r'^[A-Z][0-9]{7}$'
				if not re.match(pattern, self.passport_no):
					frappe.throw("Invalid Passport Number format. Example: A1234567")

	# def validate_visa_no(self):
	# 	"""
	# 	Optional: Validate visa number if you have a visa_no field
	# 	Example: 1 capital letter + 6-9 digits, e.g. V1234567
	# 	"""
	# 	if hasattr(self, 'visa_no') and self.visa_no:
	# 		pattern = r'^[A-Z]{1}[0-9]{6,9}$'
	# 		if not re.match(pattern, self.visa_no):
	# 			frappe.throw("Invalid Visa Number format. Example: V1234567")

	def validate_dates(self):
		"""
		Validate that passport expiry date is in the future
		and visa approved date is not before applied date
		"""

		if self.passport_expiry_date and self.passport_expiry_date <= today():
			frappe.throw("Passport Expiry Date must be a future date.")

		if self.passport_expiry_date and self.visa_approved_date:
			if self.passport_expiry_date <= self.visa_approved_date:
				frappe.throw("Passport Expiry Date must be after Visa Approved Date.")

	def validate_visa_fee(self):
		"""
		Ensure visa fee is not negative and included if required
		"""

		if hasattr(self, 'include_visa_fee') and self.include_visa_fee:
			if self.visa_fee is None or self.visa_fee == 0:
				frappe.throw("Visa Fee must be set if 'Include Visa in Package' is checked.")