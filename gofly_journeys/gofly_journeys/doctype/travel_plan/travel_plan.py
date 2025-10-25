import frappe
from frappe.model.document import Document
from datetime import datetime, date

class TravelPlan(Document):
    def validate(self):
        self.validate_airports()
        self.validate_dates()

    # 🏢 Airports validation
    def validate_airports(self):
        if self.from_airport and self.to_airport:
            if self.from_airport == self.to_airport:
                frappe.throw("⚠️ 'From Airport' and 'To Airport' cannot be the same.")

    # 📅 Date-only validation
    def validate_dates(self):
        today = date.today()

        # Convert string to date if necessary
        departure_date = self.convert_to_date(self.departure_date)
        arrival_date = self.convert_to_date(self.arrival_date)

        # Departure Date cannot be in the past
        if departure_date:
            if departure_date < today:
                frappe.throw("🚫 Departure Date cannot be in the past.")

        # Arrival Date cannot be before Departure Date
        if departure_date and arrival_date:
            if arrival_date < departure_date:
                frappe.throw("⚠️ Arrival Date cannot be before Departure Date.")

    # Helper: Convert string to date
    def convert_to_date(self, d):
        if isinstance(d, str):
            try:
                return datetime.strptime(d, "%Y-%m-%d").date()
            except ValueError:
                frappe.throw(f"❌ Invalid date format: {d}. Use YYYY-MM-DD")
        return d  # already date object
