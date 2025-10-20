# Copyright (c) 2025, GoFly Journeys and contributors
# For license information, please see license.txt
import frappe
import requests
from frappe.model.document import Document
from frappe.utils import validate_email_address


class Customer(Document):
    def validate(self):
        # Email validation
        if self.email_address:
            if not validate_email_address(self.email_address):
                frappe.throw("Please enter a valid Email Address")

# Country:
#--------
@frappe.whitelist()
def get_states_for_country(country):
    """Fetch states from external API"""
    try:
        url = "https://countriesnow.space/api/v0.1/countries/states"
        payload = {"country": country}
        response = requests.post(url, json=payload, timeout=10)

        if response.ok:
            data = response.json()
            if not data.get("error") and data.get("data"):
                states = [s["name"] for s in data["data"]["states"]]
                return states
        return []
    except Exception as e:
        frappe.log_error(f"Error fetching states for {country}: {e}")
        return []


# State:
#------
@frappe.whitelist()
def get_cities_for_state(country, state):
    """Fetch cities for the given country/state"""
    try:
        url = "https://countriesnow.space/api/v0.1/countries/state/cities"
        payload = {"country": country, "state": state}
        response = requests.post(url, json=payload, timeout=10)

        if response.ok:
            data = response.json()
            if not data.get("error") and data.get("data"):
                return data["data"]  # list of cities
        return []
    except Exception as e:
        frappe.log_error(f"Error fetching cities for {state}: {e}")
        return []



