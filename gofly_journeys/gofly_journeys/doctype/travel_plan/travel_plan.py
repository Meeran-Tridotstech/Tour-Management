import frappe
from frappe.model.document import Document
import requests
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

class TravelPlan(Document):
    pass

@frappe.whitelist()
def fetch_flights_between(dep_icao, arr_icao):
    """
    Fetch flights between dep_icao and arr_icao using OpenSky API (authenticated)
    """

    username = "meeran-api-client"
    password = "4000 Credits"  # Replace with your actual secret

    now = datetime.utcnow()
    begin = int((now - timedelta(days=1)).timestamp())
    end = int(now.timestamp())
    url = f"https://opensky-network.org/api/flights/departure?airport={dep_icao}&begin={begin}&end={end}"

    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        data = response.json()

        # Filter flights arriving at arr_icao
        flights = []
        for f in data:
            if f.get("estArrivalAirport") == arr_icao:
                flights.append({
                    "icao24": f.get("icao24") or "",
                    "callsign": f.get("callsign") or "",
                    "departure_airport": f.get("estDepartureAirport") or "",
                    "arrival_airport": f.get("estArrivalAirport") or "",
                    "departure_time": datetime.utcfromtimestamp(f.get("firstSeen")).strftime('%Y-%m-%d %H:%M:%S') if f.get("firstSeen") else "",
                    "arrival_time": datetime.utcfromtimestamp(f.get("lastSeen")).strftime('%Y-%m-%d %H:%M:%S') if f.get("lastSeen") else "",
                    "on_ground": f.get("on_ground")
                })

        return flights

    except requests.exceptions.RequestException as e:
        frappe.throw(f"Error fetching flights: {str(e)}")
