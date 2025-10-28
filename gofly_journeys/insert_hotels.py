import frappe
import json

def insert_hotels():
    hotel_data = [
  {"hotel_name": "Taj Coromandel", "country": "India", "city": "Chennai", "location": "Nungambakkam"},
  {"hotel_name": "Leela Palace", "country": "India", "city": "Delhi", "location": "Chanakyapuri"},
  {"hotel_name": "Hilton Garden Inn", "country": "USA", "city": "New York", "location": "Manhattan"},
  {"hotel_name": "Marriott Downtown", "country": "USA", "city": "Chicago", "location": "Wacker Drive"},
  {"hotel_name": "Four Seasons", "country": "Canada", "city": "Toronto", "location": "Yorkville"},
  {"hotel_name": "Ritz-Carlton", "country": "UK", "city": "London", "location": "Piccadilly"},
  {"hotel_name": "Hotel Le Meurice", "country": "France", "city": "Paris", "location": "Rue de Rivoli"},
  {"hotel_name": "Grand Hyatt", "country": "Germany", "city": "Berlin", "location": "Marlene-Dietrich-Platz"},
  {"hotel_name": "Atlantis The Palm", "country": "UAE", "city": "Dubai", "location": "Crescent Road"},
  {"hotel_name": "Mandarin Oriental", "country": "Singapore", "city": "Singapore", "location": "Marina Bay"},
  {"hotel_name": "Peninsula", "country": "China", "city": "Shanghai", "location": "The Bund"},
  {"hotel_name": "Park Hyatt", "country": "Japan", "city": "Tokyo", "location": "Shinjuku"},
  {"hotel_name": "Crown Towers", "country": "Australia", "city": "Melbourne", "location": "Southbank"},
  {"hotel_name": "Serena Hotel", "country": "Pakistan", "city": "Islamabad", "location": "Khayaban-e-Suharwardy"},
  {"hotel_name": "Yak & Yeti", "country": "Nepal", "city": "Kathmandu", "location": "Durbar Marg"},
  {"hotel_name": "Cinnamon Grand", "country": "Sri Lanka", "city": "Colombo", "location": "Colombo 03"},
  {"hotel_name": "Savoy Hotel", "country": "South Africa", "city": "Cape Town", "location": "Sea Point"},
  {"hotel_name": "Mandarin Oriental", "country": "Thailand", "city": "Bangkok", "location": "Chao Phraya River"},
  {"hotel_name": "Hotel Mulia", "country": "Indonesia", "city": "Jakarta", "location": "Senayan"},
  {"hotel_name": "The Oberoi", "country": "Egypt", "city": "Cairo", "location": "Nile Corniche"},
  {"hotel_name": "Four Seasons", "country": "Qatar", "city": "Doha", "location": "Corniche"},
  {"hotel_name": "La Mamounia", "country": "Morocco", "city": "Marrakech", "location": "Avenue Bab Jdid"},
  {"hotel_name": "Sheraton Addis", "country": "Ethiopia", "city": "Addis Ababa", "location": "Taitu Street"},
  {"hotel_name": "Hotel Nacional", "country": "Brazil", "city": "Rio de Janeiro", "location": "Copacabana"},
  {"hotel_name": "Belmond Copacabana Palace", "country": "Brazil", "city": "Rio de Janeiro", "location": "Avenida Atlântica"},
  {"hotel_name": "Hotel Fasano", "country": "Brazil", "city": "São Paulo", "location": "Jardins"},
  {"hotel_name": "The Langham", "country": "Hong Kong", "city": "Hong Kong", "location": "Tsim Sha Tsui"},
  {"hotel_name": "Waldorf Astoria", "country": "USA", "city": "Los Angeles", "location": "Beverly Hills"},
  {"hotel_name": "Hyatt Regency", "country": "India", "city": "Mumbai", "location": "Sahar Airport Road"},
  {"hotel_name": "ITC Grand Chola", "country": "India", "city": "Chennai", "location": "Guindy"},
  {"hotel_name": "The Park", "country": "India", "city": "Kolkata", "location": "Park Street"},
  {"hotel_name": "Raffles Hotel", "country": "Singapore", "city": "Singapore", "location": "Beach Road"},
  {"hotel_name": "Banyan Tree", "country": "Thailand", "city": "Phuket", "location": "Laguna"},
  {"hotel_name": "Anantara Resort", "country": "Maldives", "city": "Male", "location": "South Male Atoll"},
  {"hotel_name": "Hotel Adlon Kempinski", "country": "Germany", "city": "Berlin", "location": "Unter den Linden"},
  {"hotel_name": "Fairmont Peace Hotel", "country": "China", "city": "Shanghai", "location": "The Bund"},
  {"hotel_name": "InterContinental", "country": "Mexico", "city": "Mexico City", "location": "Polanco"},
  {"hotel_name": "JW Marriott", "country": "USA", "city": "Houston", "location": "Galleria"},
  {"hotel_name": "Hotel Danieli", "country": "Italy", "city": "Venice", "location": "Riva degli Schiavoni"},
  {"hotel_name": "Hotel de Paris", "country": "Monaco", "city": "Monte Carlo", "location": "Place du Casino"},
  {"hotel_name": "Hotel President Wilson", "country": "Switzerland", "city": "Geneva", "location": "Quai Wilson"},
  {"hotel_name": "Baur au Lac", "country": "Switzerland", "city": "Zurich", "location": "Talstrasse"},
  {"hotel_name": "Hotel Sacher", "country": "Austria", "city": "Vienna", "location": "Philharmonikerstrasse"},
  {"hotel_name": "Hotel Arts", "country": "Spain", "city": "Barcelona", "location": "Port Olímpic"},
  {"hotel_name": "Alvear Palace", "country": "Argentina", "city": "Buenos Aires", "location": "Recoleta"},
  {"hotel_name": "Belmond Monasterio", "country": "Peru", "city": "Cusco", "location": "Plaza Nazarenas"},
  {"hotel_name": "The Gritti Palace", "country": "Italy", "city": "Venice", "location": "Grand Canal"},
  {"hotel_name": "Belmond Grand Hotel Europe", "country": "Russia", "city": "Saint Petersburg", "location": "Nevsky Prospekt"},
  {"hotel_name": "Hotel Ukraina", "country": "Russia", "city": "Moscow", "location": "Kievskaya"},
  {"hotel_name": "Marina Bay Sands", "country": "Singapore", "city": "Singapore", "location": "Marina Bay"},
  {"hotel_name": "Fullerton Hotel", "country": "Singapore", "city": "Singapore", "location": "Fullerton Square"},
  {"hotel_name": "Hotel Eden", "country": "Italy", "city": "Rome", "location": "Via Ludovisi"},
  {"hotel_name": "Claridge's", "country": "UK", "city": "London", "location": "Brook Street"},
  {"hotel_name": "The Connaught", "country": "UK", "city": "London", "location": "Mayfair"},
  {"hotel_name": "The Plaza", "country": "USA", "city": "New York", "location": "Fifth Avenue"},
  {"hotel_name": "The Peninsula Beverly Hills", "country": "USA", "city": "Los Angeles", "location": "Santa Monica Blvd"},
  {"hotel_name": "Hotel du Cap-Eden-Roc", "country": "France", "city": "Antibes", "location": "Boulevard John Kennedy"},
  {"hotel_name": "Chateau Marmont", "country": "USA", "city": "Los Angeles", "location": "Sunset Blvd"},
  {"hotel_name": "Hotel Ritz", "country": "Spain", "city": "Madrid", "location": "Plaza de la Lealtad"},
  {"hotel_name": "Hotel Bristol", "country": "Poland", "city": "Warsaw", "location": "Krakowskie Przedmieście"},
  {"hotel_name": "Hotel Okura", "country": "Japan", "city": "Tokyo", "location": "Minato"},
  {"hotel_name": "Hotel Shilla", "country": "South Korea", "city": "Seoul", "location": "Jangchungdong"},
  {"hotel_name": "The Westin", "country": "USA", "city": "Seattle", "location": "Fifth Avenue"},
  {"hotel_name": "Hotel Lisboa", "country": "Macau", "city": "Macau", "location": "Avenida de Lisboa"},
  {"hotel_name": "MGM Grand", "country": "USA", "city": "Las Vegas", "location": "The Strip"},
  {"hotel_name": "Bellagio", "country": "USA", "city": "Las Vegas", "location": "Las Vegas Blvd"},
  {"hotel_name": "The Venetian", "country": "USA", "city": "Las Vegas", "location": "The Strip"},
  {"hotel_name": "Caesars Palace", "country": "USA", "city": "Las Vegas", "location": "The Strip"},
  {"hotel_name": "Waldorf Astoria", "country": "UAE", "city": "Dubai", "location": "Palm Jumeirah"},
  {"hotel_name": "Burj Al Arab", "country": "UAE", "city": "Dubai", "location": "Jumeirah Beach"},
  {"hotel_name": "Jumeirah Beach Hotel", "country": "UAE", "city": "Dubai", "location": "Jumeirah Street"},
  {"hotel_name": "Emirates Palace", "country": "UAE", "city": "Abu Dhabi", "location": "Corniche Road"},
  {"hotel_name": "Hotel Alfonso XIII", "country": "Spain", "city": "Seville", "location": "Calle San Fernando"},
  {"hotel_name": "Palace Hotel", "country": "Japan", "city": "Tokyo", "location": "Marunouchi"},
  {"hotel_name": "The St. Regis", "country": "USA", "city": "New York", "location": "Fifth Avenue"},
  {"hotel_name": "The Dorchester", "country": "UK", "city": "London", "location": "Park Lane"},
  {"hotel_name": "Beverly Hills Hotel", "country": "USA", "city": "Los Angeles", "location": "Sunset Boulevard"},
  {"hotel_name": "Hotel de Russie", "country": "Italy", "city": "Rome", "location": "Via del Babuino"},
  {"hotel_name": "Rosewood", "country": "Hong Kong", "city": "Hong Kong", "location": "Victoria Dockside"},
  {"hotel_name": "Mandarin Oriental", "country": "Hong Kong", "city": "Hong Kong", "location": "Connaught Road"},
  {"hotel_name": "The Peninsula", "country": "Hong Kong", "city": "Hong Kong", "location": "Salisbury Road"},
  {"hotel_name": "Shangri-La", "country": "Malaysia", "city": "Kuala Lumpur", "location": "Jalan Sultan Ismail"},
  {"hotel_name": "Majestic Hotel", "country": "Malaysia", "city": "Kuala Lumpur", "location": "Jalan Sultan Hishamuddin"},
  {"hotel_name": "E&O Hotel", "country": "Malaysia", "city": "Penang", "location": "George Town"},
  {"hotel_name": "Hotel New Otani", "country": "Japan", "city": "Tokyo", "location": "Kioicho"},
  {"hotel_name": "Conrad", "country": "South Korea", "city": "Seoul", "location": "Yeouido"},
  {"hotel_name": "Lotte Hotel", "country": "South Korea", "city": "Seoul", "location": "Sogong-dong"},
  {"hotel_name": "InterContinental", "country": "Vietnam", "city": "Hanoi", "location": "West Lake"},
  {"hotel_name": "Sofitel Metropole", "country": "Vietnam", "city": "Hanoi", "location": "Ngo Quyen Street"},
  {"hotel_name": "Park Hyatt", "country": "Vietnam", "city": "Ho Chi Minh City", "location": "Lam Son Square"},
  {"hotel_name": "Grand Hotel", "country": "Sweden", "city": "Stockholm", "location": "Södra Blasieholmshamnen"},
  {"hotel_name": "Radisson Blu", "country": "Norway", "city": "Oslo", "location": "Holbergs Gate"},
  {"hotel_name": "Hotel Continental", "country": "Norway", "city": "Oslo", "location": "Stortingsgata"},
  {"hotel_name": "Hotel d’Angleterre", "country": "Denmark", "city": "Copenhagen", "location": "Kongens Nytorv"},
  {"hotel_name": "Hotel Kempinski", "country": "Hungary", "city": "Budapest", "location": "Erzsébet tér"},
  {"hotel_name": "Aria Hotel", "country": "Hungary", "city": "Budapest", "location": "Hercegprímás Street"},
  {"hotel_name": "Hotel Metropole", "country": "Belgium", "city": "Brussels", "location": "Place de Brouckère"},
  {"hotel_name": "Steigenberger Frankfurter Hof", "country": "Germany", "city": "Frankfurt", "location": "Am Kaiserplatz"},
  {"hotel_name": "The Leela Mumbai", "country": "India", "city": "Mumbai", "location": "Andheri"},
  {"hotel_name": "The Oberoi Mumbai", "country": "India", "city": "Mumbai", "location": "Nariman Point"},
  {"hotel_name": "ITC Grand Chola", "country": "India", "city": "Chennai", "location": "Guindy"},
  {"hotel_name": "The Leela Palace Chennai", "country": "India", "city": "Chennai", "location": "Adyar"},
  {"hotel_name": "Taj Coromandel", "country": "India", "city": "Chennai", "location": "Nungambakkam"},
  {"hotel_name": "The Park Chennai", "country": "India", "city": "Chennai", "location": "Anna Salai"},
  {"hotel_name": "Taj Bengal", "country": "India", "city": "Kolkata", "location": "Alipore"},
  {"hotel_name": "The Oberoi Grand", "country": "India", "city": "Kolkata", "location": "B.B.D. Bagh"},
  {"hotel_name": "ITC Sonar", "country": "India", "city": "Kolkata", "location": "EM Bypass"},
  {"hotel_name": "The Leela Palace Udaipur", "country": "India", "city": "Udaipur", "location": "Lake Pichola"},
  {"hotel_name": "Taj Lake Palace", "country": "India", "city": "Udaipur", "location": "Lake Pichola"},
  {"hotel_name": "The Oberoi Udaivilas", "country": "India", "city": "Udaipur", "location": "Haridasji Ki Magri"},
  {"hotel_name": "JW Marriott Jaipur", "country": "India", "city": "Jaipur", "location": "Malviya Nagar"},
  {"hotel_name": "The Lalit Jaipur", "country": "India", "city": "Jaipur", "location": "Bani Park"},
  {"hotel_name": "Rambagh Palace", "country": "India", "city": "Jaipur", "location": "Civil Lines"},
  {"hotel_name": "Taj Jai Mahal Palace", "country": "India", "city": "Jaipur", "location": "Jaipur City"},
  {"hotel_name": "The Leela Palace New Delhi", "country": "India", "city": "Delhi", "location": "Chanakyapuri"},
  {"hotel_name": "Taj Mahal Hotel", "country": "India", "city": "Delhi", "location": "Connaught Place"},
  {"hotel_name": "The Oberoi, New Delhi", "country": "India", "city": "Delhi", "location": "Dr Zakir Hussain Marg"},
  {"hotel_name": "ITC Maurya", "country": "India", "city": "Delhi", "location": "Sardar Patel Marg"},
  {"hotel_name": "The Leela Ambience", "country": "India", "city": "Gurgaon", "location": "Sohna Road"},
  {"hotel_name": "Taj City Centre", "country": "India", "city": "Bengaluru", "location": "MG Road"},
  {"hotel_name": "The Leela Palace Bengaluru", "country": "India", "city": "Bengaluru", "location": "Old Airport Road"},
  {"hotel_name": "ITC Gardenia", "country": "India", "city": "Bengaluru", "location": "Residency Road"},
  {"hotel_name": "Shangri-La Bengaluru", "country": "India", "city": "Bengaluru", "location": "MG Road"},
  {"hotel_name": "Taj West End", "country": "India", "city": "Bengaluru", "location": "Race Course Road"},
  {"hotel_name": "The Gateway Hotel, Visakhapatnam", "country": "India", "city": "Visakhapatnam", "location": "Beach Road"},
  {"hotel_name": "Novotel Visakhapatnam", "country": "India", "city": "Visakhapatnam", "location": "Seaside"},
  {"hotel_name": "The Park Visakhapatnam", "country": "India", "city": "Visakhapatnam", "location": "Beach Road"},
  {"hotel_name": "Taj Palace, New Delhi", "country": "India", "city": "New Delhi", "location": "Chanakyapuri"},
  {"hotel_name": "Radisson Blu, Hyderabad", "country": "India", "city": "Hyderabad", "location": "HITEC City"},
  {"hotel_name": "Taj Falaknuma Palace", "country": "India", "city": "Hyderabad", "location": "Falaknuma"},
  {"hotel_name": "ITC Kakatiya", "country": "India", "city": "Hyderabad", "location": "Begumpet"},
  {"hotel_name": "The Westin, Pune", "country": "India", "city": "Pune", "location": "Bund Garden Road"},
  {"hotel_name": "JW Marriott Pune", "country": "India", "city": "Pune", "location": "Bund Garden Road"},
  {"hotel_name": "Conrad Pune", "country": "India", "city": "Pune", "location": "Magarpatta City"},
  {"hotel_name": "Radisson Blu, Pune", "country": "India", "city": "Pune", "location": "Koregaon Park"},
  {"hotel_name": "Taj Mahal Palace, Mumbai", "country": "India", "city": "Mumbai", "location": "Colaba"},
  {"hotel_name": "The Leela Palace, Udaipur", "country": "India", "city": "Udaipur", "location": "Lake Pichola"},
  {"hotel_name": "Radisson Blu, Jaipur", "country": "India", "city": "Jaipur", "location": "Vaishali Nagar"},
  {"hotel_name": "The Fern, Delhi", "country": "India", "city": "Delhi", "location": "Saket"},
  {"hotel_name": "The Oberoi Rajvilas, Jaipur", "country": "India", "city": "Jaipur", "location": "Chandpole"},
  {"hotel_name": "Taj Mahal Palace, Kolkata", "country": "India", "city": "Kolkata", "location": "Esplanade"},
  {"hotel_name": "Hyatt Regency, Kolkata", "country": "India", "city": "Kolkata", "location": "EM Bypass"},
  {"hotel_name": "The Park, Kolkata", "country": "India", "city": "Kolkata", "location": "Park Street"},
  {"hotel_name": "Taj Hari Mahal, Jodhpur", "country": "India", "city": "Jodhpur", "location": "Jaswant Thada Road"},
  {"hotel_name": "Umaid Bhawan Palace, Jodhpur", "country": "India", "city": "Jodhpur", "location": "Palace Road"},
  {"hotel_name": "Radisson Blu, Kochi", "country": "India", "city": "Kochi", "location": "Marine Drive"},
  {"hotel_name": "Le Méridien, Kochi", "country": "India", "city": "Kochi", "location": "Willingdon Island"},
  {"hotel_name": "Taj Malabar Resort, Kochi", "country": "India", "city": "Kochi", "location": "Willington Island"},
  {"hotel_name": "The Gateway Hotel, Mangalore", "country": "India", "city": "Mangalore", "location": "Kadri Hills"},
  {"hotel_name": "Radisson Blu, Mangalore", "country": "India", "city": "Mangalore", "location": "Kadri Road"}
]


    for data in hotel_data:
        country_name = data["country"]

        # ✅ Ensure the Country exists
        if not frappe.db.exists("Country", country_name):
            frappe.get_doc({
                "doctype": "Country",
                "country_name": country_name
            }).insert(ignore_permissions=True)

        # ✅ Insert the Hotel Booking
        doc = frappe.get_doc({
            "doctype": "Hotel Booking",
            "hotel_name": data["hotel_name"],
            "country": data["country"],
            "city": data["city"],
            "location": data["location"],
        })
        doc.insert(ignore_if_duplicate=True, ignore_permissions=True)

    frappe.db.commit()
    print(f"{len(hotel_data)} hotel records inserted successfully!")



# ---------------------------------------------------------------------------------------------------------------------------------------------
# import frappe
# from datetime import datetime

# @frappe.whitelist()
# def insert_travel_plan():
#     # Sample record
#     travel_plan = {
#         "booking": "Booking-001",
#         "guide": "Rahul Sharma",
#         "start_date": "2025-11-01",
#         "end_date": "2025-11-05",
#         "travel_status": "Planned",
#         "flight_number": "AI101",
#         "from_airport": "Chennai International Airport (MAA) - India",
#         "to_airport": "Delhi Indira Gandhi International Airport (DEL) - India",
#         "departure_date": "2025-11-01",
#         "departure_time": "06:00",
#         "arrival_date": "2025-11-01",
#         "arrival_time": "08:00",
#         "hotel_name": "Leela Palace",
#         "location": "Chanakyapuri",
#         "room_type": "Deluxe",
#         "booking_status": "Confirmed",
#         "vehicle_type": "Sedan",
#         "driver_name": "Ramesh Kumar",
#         "pickup": "Hotel Lobby",
#         "travel_date": "2025-11-01",
#         "cost": 15000
#     }

#     # Create and insert doc
#     doc = frappe.get_doc({
#         "doctype": "Travel Plan",
#         **travel_plan
#     })
#     doc.insert()
#     frappe.db.commit()  # Commit to save in database
#     return "Travel Plan inserted successfully!"













import frappe
from datetime import datetime, timedelta
import random

def insert_multiple_travel_plans():
    guides = ["Rahul Sharma", "Anita Verma", "Suresh Patel", "Priya Singh", "Arjun Mehta"]
    hotels = [
        {"hotel_name": "Leela Palace", "location": "Chanakyapuri"},
        {"hotel_name": "Taj Mahal Hotel", "location": "Connaught Place"},
        {"hotel_name": "ITC Maurya", "location": "Diplomatic Enclave"},
        {"hotel_name": "Hilton Garden Inn", "location": "Manhattan"},
        {"hotel_name": "Marriott Downtown", "location": "Chicago"},
        {"hotel_name": "Four Seasons", "location": "Toronto"},
        {"hotel_name": "Ritz-Carlton", "location": "London"},
        {"hotel_name": "Grand Hyatt", "location": "Berlin"},
        {"hotel_name": "Atlantis The Palm", "location": "Dubai"},
        {"hotel_name": "Mandarin Oriental", "location": "Singapore"}
    ]
    flights = [
        {"flight_number": "AI101", "from_airport": "Chennai International Airport (MAA) - India", "to_airport": "Delhi Indira Gandhi International Airport (DEL) - India"},
        {"flight_number": "AI202", "from_airport": "Mumbai Chhatrapati Shivaji International Airport (BOM) - India", "to_airport": "Bengaluru Kempegowda International Airport (BLR) - India"},
        {"flight_number": "AI303", "from_airport": "Hyderabad Rajiv Gandhi International Airport (HYD) - India", "to_airport": "Kolkata Netaji Subhas Chandra Bose International Airport (CCU) - India"},
    ]
    room_types = ["Deluxe", "Suite", "Standard"]
    booking_statuses = ["Confirmed", "Pending", "Canceled"]
    vehicles = ["Sedan", "SUV", "Van"]
    
    base_date = datetime(2025, 11, 1)
    
    for i in range(100):
        guide = random.choice(guides)
        hotel = random.choice(hotels)
        flight = random.choice(flights)
        room_type = random.choice(room_types)
        booking_status = random.choice(booking_statuses)
        vehicle_type = random.choice(vehicles)
        driver_name = f"Driver {i+1}"
        travel_date = base_date + timedelta(days=i)
        start_date = travel_date
        end_date = travel_date + timedelta(days=random.randint(2, 5))
        departure_time = f"{random.randint(5, 23):02d}:00"
        arrival_time = f"{random.randint(6, 24):02d}:00"
        cost = random.randint(10000, 50000)
        
        travel_plan = {
            "doctype": "Travel Plan",
            "booking": f"Booking-{i+1:03d}",
            "guide": guide,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "travel_status": "Planned",
            "flight_number": flight["flight_number"],
            "from_airport": flight["from_airport"],
            "to_airport": flight["to_airport"],
            "departure_date": start_date.strftime("%Y-%m-%d"),
            "departure_time": departure_time,
            "arrival_date": start_date.strftime("%Y-%m-%d"),
            "arrival_time": arrival_time,
            "hotel_name": hotel["hotel_name"],
            "location": hotel["location"],
            "room_type": room_type,
            "booking_status": booking_status,
            "vehicle_type": vehicle_type,
            "driver_name": driver_name,
            "pickup": "Hotel Lobby",
            "travel_date": travel_date.strftime("%Y-%m-%d"),
            "cost": cost
        }
        
        doc = frappe.get_doc(travel_plan)
        doc.insert(ignore_if_duplicate=True)
    
    frappe.db.commit()
    return "50 Travel Plan records inserted successfully!"







#-------------------------------------------------------------------------------------------------------------------------------------------------------
import frappe
from random import choice, randint

def insert_vehicle_records():
    vehicle_names = [
        "Toyota Innova", "Mahindra Scorpio", "Hyundai Creta", "Honda City",
        "Suzuki Swift", "Ford Endeavour", "Kia Seltos", "Maruti Baleno",
        "Tata Nexon", "BMW X5", "Mercedes GLE", "Audi Q7", "Toyota Fortuner",
        "Mahindra XUV500", "Honda Civic", "Hyundai Tucson", "Jeep Compass",
        "Nissan X-Trail", "MG Hector", "Volkswagen Tiguan", "Ford EcoSport",
        "Toyota Camry", "Honda Accord", "BMW 3 Series", "Audi A6", "Mercedes C-Class",
        "Kia Carnival", "Renault Duster", "Chevrolet Trailblazer", "Tata Harrier",
        "Mahindra Thar", "Hyundai Venue", "Suzuki Dzire", "Maruti Celerio", 
        "Honda Amaze", "Toyota Yaris", "Kia Sonet", "MG ZS", "Nissan Kicks",
        "Volkswagen Polo", "Hyundai i20", "Ford Figo", "Toyota Corolla", "Honda Jazz",
        "Skoda Octavia", "Volkswagen Passat", "Audi Q5", "Mercedes E-Class", "BMW X3",
        "Mahindra Bolero", "Tata Safari", "Chevrolet Spark", "Renault Kwid", "Hyundai Creta SX",
        "Kia Stinger", "Jaguar F-Pace", "Land Rover Discovery", "Ford Mustang",
        "Tesla Model S", "Tesla Model 3", "Tesla Model X", "Toyota Prius", "Honda HR-V",
        "BMW X1", "Audi Q3", "Mercedes GLC", "Volvo XC90", "Jeep Wrangler",
        "Hyundai Santa Fe", "Mazda CX-5", "Mitsubishi Outlander", "Nissan Rogue",
        "Chevrolet Traverse", "Honda Pilot", "Ford Explorer", "Kia Sportage", "Toyota RAV4",
        "Suzuki Ertiga", "Maruti Eeco", "Honda BR-V", "Toyota Innova Crysta",
        "Mahindra Marazzo", "Tata Hexa", "Volkswagen Tiguan Allspace", "Jeep Compass Trailhawk",
        "Audi A4", "BMW 5 Series", "Mercedes S-Class", "Kia K900", "Hyundai Palisade",
        "Ford Expedition", "Chevrolet Suburban", "GMC Yukon", "Nissan Armada", "Toyota Land Cruiser",
        "Mahindra XUV700", "Tata Safari Storme"
    ]

    vehicle_types = ["Sedan", "SUV", "Van", "Bus", "Bike", "Minivan", "Luxury Sedan", "Pickup Truck", "Electric Car", "Convertible"]
    availability_status = ["Available", "Booked", "Maintenance"]
    drivers = ["Ramesh Kumar", "Suresh Singh", "Rahul Sharma", "Vikram Patel", "Anil Joshi", "Deepak Verma", "Arun Mehta"]

    for i in range(1, 101):  # Insert 100 records
        vehicle_name = choice(vehicle_names)
        vehicle_type = choice(vehicle_types)
        doc = frappe.get_doc({
            "doctype": "Vehicle",
            "vehicle_name": f"{vehicle_name} {i}",
            "vehicle_number": f"TN{i:03d}AB{randint(1000,9999)}",
            "vehicle_type": vehicle_type,
            "capacity": randint(2, 50) if vehicle_type not in ["Bike", "Convertible"] else 1,
            "driver_name": choice(drivers),
            "availability": choice(availability_status),
            "cost_per_day": randint(1000, 25000),
            "contact_number": f"+91{randint(9000000000, 9999999999)}"
        })
        doc.insert()

    frappe.db.commit()
    print("100 Vehicle records inserted successfully!")
    
    
    
    
    
#     #--------------------------------------------------------------------------------------------------------------------

# from random import choice, randint
# from datetime import date, timedelta
# import frappe

# def insert_tour_packages():
#     package_data = [
#         {
#             "package_name": "Romantic Paris Getaway",
#             "country": "France",
#             "state": "Paris",
#             "explore": {
#                 "destination_name": "Eiffel Tower",
#                 "key_attractions": "Iconic landmark of Paris",
#                 "description": "Enjoy breathtaking views from the top of the Eiffel Tower.",
#                 "best_time_to_visit": "April to June"
#             }
#         },
#         {
#             "package_name": "Dubai Desert Adventure",
#             "country": "United Arab Emirates",
#             "state": "Dubai",
#             "explore": {
#                 "destination_name": "Burj Khalifa",
#                 "key_attractions": "Tallest building in the world",
#                 "description": "Experience Dubai from the highest observation deck.",
#                 "best_time_to_visit": "November to February"
#             }
#         },
#         {
#             "package_name": "Goa Beach Holidays",
#             "country": "India",
#             "state": "Goa",
#             "explore": {
#                 "destination_name": "Baga Beach",
#                 "key_attractions": "Beach activities and nightlife",
#                 "description": "Relax and enjoy beachside cafes and water sports.",
#                 "best_time_to_visit": "October to March"
#             }
#         },
#         {
#             "package_name": "Thailand Explorer",
#             "country": "Thailand",
#             "state": "Bangkok",
#             "explore": {
#                 "destination_name": "Chiang Mai Old City",
#                 "key_attractions": "Ancient temples and street food",
#                 "description": "Explore the cultural capital of Northern Thailand.",
#                 "best_time_to_visit": "November to February"
#             }
#         },
#         {
#             "package_name": "Malaysia Family Fun",
#             "country": "Malaysia",
#             "state": "Kuala Lumpur",
#             "explore": {
#                 "destination_name": "Langkawi Island",
#                 "key_attractions": "Sky Bridge, beaches, and waterfalls",
#                 "description": "Perfect island destination for families.",
#                 "best_time_to_visit": "December to March"
#             }
#         }
#     ]

#     for i, pkg in enumerate(package_data):
#         start_date = date.today() + timedelta(days=randint(5, 20))
#         end_date = start_date + timedelta(days=randint(3, 10))
#         days = (end_date - start_date).days
#         nights = days - 1

#         doc = frappe.get_doc({
#             "doctype": "Tour Package",
#             "package_name": pkg["package_name"],
#             "amount": randint(20000, 100000),
#             "country": pkg["country"],
#             "state": pkg["state"],
#             "start_date": start_date,
#             "end_date": end_date,
#             "days": days,
#             "nights": nights,
#             "package_status": "Available",
#             "expected_trip_month": choice(["January", "February", "March", "April", "May", "June"]),
#             "up_to": choice(["July", "August", "September", "October", "November", "December"]),
#             "explore": [pkg["explore"]],
#             "images": [
#                 {
#                     "image": "/files/sample_image.jpg",
#                     "caption": f"Image {i+1}"
#                 }
#             ]
#         })
#         doc.insert(ignore_permissions=True)
#         frappe.db.commit()
#         print(f"✅ Created Tour Package: {doc.name} ({pkg['country']})")



from random import choice, randint
from datetime import date, timedelta
import frappe

def insert_tour_packages():
    countries = {
        "India": {
            "states": ["Tamil Nadu", "Kerala", "Goa", "Maharashtra"],
            "destinations": [
                {
                    "destination_name": "Taj Mahal",
                    "key_attractions": "Symbol of love and Mughal architecture",
                    "description": "Experience the timeless beauty of the Taj Mahal at sunrise.",
                    "best_time_to_visit": "October to March"
                },
                {
                    "destination_name": "Baga Beach",
                    "key_attractions": "Beach activities and nightlife",
                    "description": "Relax and enjoy beachside cafes and water sports.",
                    "best_time_to_visit": "November to February"
                },
                {
                    "destination_name": "Munnar Hills",
                    "key_attractions": "Tea gardens and scenic hills",
                    "description": "Perfect for a peaceful mountain retreat.",
                    "best_time_to_visit": "September to March"
                }
            ]
        },
        "Thailand": {
            "states": ["Bangkok", "Chiang Mai", "Phuket"],
            "destinations": [
                {
                    "destination_name": "Phuket Beaches",
                    "key_attractions": "Tropical beaches and island hopping",
                    "description": "Explore Thailand’s most famous island paradise.",
                    "best_time_to_visit": "November to February"
                },
                {
                    "destination_name": "Chiang Mai Old City",
                    "key_attractions": "Ancient temples and street food",
                    "description": "Discover culture and cuisine in Northern Thailand.",
                    "best_time_to_visit": "November to February"
                }
            ]
        },
        "Malaysia": {
            "states": ["Kuala Lumpur", "Penang", "Langkawi"],
            "destinations": [
                {
                    "destination_name": "Langkawi Island",
                    "key_attractions": "Sky Bridge, beaches, and waterfalls",
                    "description": "Perfect island destination for families.",
                    "best_time_to_visit": "December to March"
                },
                {
                    "destination_name": "Batu Caves",
                    "key_attractions": "Hindu shrines and limestone caves",
                    "description": "A colorful and spiritual attraction near Kuala Lumpur.",
                    "best_time_to_visit": "January to February"
                }
            ]
        },
        "United Arab Emirates": {
            "states": ["Dubai", "Abu Dhabi"],
            "destinations": [
                {
                    "destination_name": "Burj Khalifa",
                    "key_attractions": "Tallest building in the world",
                    "description": "Experience Dubai from the highest observation deck.",
                    "best_time_to_visit": "November to February"
                },
                {
                    "destination_name": "Sheikh Zayed Grand Mosque",
                    "key_attractions": "Architectural masterpiece",
                    "description": "Marvel at the stunning white marble architecture.",
                    "best_time_to_visit": "November to March"
                }
            ]
        },
        "France": {
            "states": ["Paris", "Nice", "Lyon"],
            "destinations": [
                {
                    "destination_name": "Eiffel Tower",
                    "key_attractions": "Iconic landmark of Paris",
                    "description": "Enjoy breathtaking views from the top of the Eiffel Tower.",
                    "best_time_to_visit": "April to June"
                },
                {
                    "destination_name": "French Riviera",
                    "key_attractions": "Beaches, glamour, and Mediterranean views",
                    "description": "Relax along the stunning Côte d’Azur coastline.",
                    "best_time_to_visit": "May to September"
                }
            ]
        }
    }

    package_themes = [
        "Romantic Getaway", "Adventure Trip", "Family Vacation",
        "Cultural Tour", "Luxury Experience", "Wildlife Safari",
        "Beach Holiday", "Mountain Escape", "City Lights Tour", "Heritage Journey"
    ]

    for i in range(1, 101):
        # Randomly pick a country and corresponding state
        country = choice(list(countries.keys()))
        state = choice(countries[country]["states"])
        destination = choice(countries[country]["destinations"])

        # Generate a dynamic package name
        theme = choice(package_themes)
        package_name = f"{theme} in {state}"

        start_date = date.today() + timedelta(days=randint(5, 30))
        end_date = start_date + timedelta(days=randint(4, 12))
        days = (end_date - start_date).days
        nights = days - 1

        doc = frappe.get_doc({
            "doctype": "Tour Package",
            "package_name": package_name,
            "amount": randint(20000, 120000),
            "country": country,
            "state": state,
            "start_date": start_date,
            "end_date": end_date,
            "days": days,
            "nights": nights,
            "package_status": "Available",
            "expected_trip_month": choice(["January", "February", "March", "April", "May", "June"]),
            "up_to": choice(["July", "August", "September", "October", "November", "December"]),
            "explore": [
                {
                    "destination_name": destination["destination_name"],
                    "key_attractions": destination["key_attractions"],
                    "description": destination["description"],
                    "best_time_to_visit": destination["best_time_to_visit"]
                }
            ],
            "images": [
                {
                    "image": "/files/sample_image.jpg",
                    "caption": f"Image {i}"
                }
            ]
        })

        doc.insert(ignore_permissions=True)
        frappe.db.commit()
        print(f"✅ Created Tour Package {i}: {package_name} ({country})")

    print("\n🎉 Successfully inserted 100 tour packages!")




# -------------------------------------------------------------------------------------------------------------------------------
import frappe

def insert_staff_record():
    doc = frappe.get_doc({
        "doctype": "Staff",
        "staff_name": "John Doe",
        "contact_number": "9876543210",
        "email": "john.doe@example.com",
        "assigned_customer": "CUST-0001",  # existing Customer ID
        "assigned_tour": "BOOK-0001",      # existing Booking ID
        "allocation_date": "2025-10-27",
        "status": "Available",
        "remarks": "Assigned for Chennai–Goa Tour"
    })
    doc.insert(ignore_permissions=True)
    doc.submit()
    frappe.db.commit()
    print(f"✅ Staff record created successfully: {doc.name}")
