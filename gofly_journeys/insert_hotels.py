import frappe
import json
#-----------------Hitel Booking ---------------------------------------
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



# --  Travel plan  -------------------------------------------------------------------------------------------------------------------------------------------

import frappe
import random
from frappe.utils import nowdate, add_days, nowtime

def insert_multiple_travel_plans():
    # Static data
    guides = ["Arun Kumar", "Fatima Noor", "Rahul Verma", "Zoya Khan", "Deepak Reddy", "Priya Das", "Nasser Ali", "Ibrahim Syed"]
    room_types = [
        "Single Room", "Double Room", "Twin Room", "Triple Room", "Deluxe Room", "Executive Room",
        "Suite", "Junior Suite", "Presidential Suite", "Family Room", "Connecting Room", "Studio Room",
        "Villa", "Penthouse", "Cabana", "Accessible Room", "Superior Room", "Standard Room",
        "Honeymoon Suite", "Apartment"
    ]
    travel_statuses = ["Planned", "Ongoing", "Completed"]
    booking_statuses = ["Confirmed", "Pending", "Canceled"]
    
    from_airports = [
        "Chennai International Airport (MAA) - India",
        "Delhi Indira Gandhi International Airport (DEL) - India",
        "Mumbai Chhatrapati Shivaji Maharaj International Airport (BOM) - India",
        "Dubai International Airport (DXB) - UAE",
        "Doha Hamad International Airport (DOH) - Qatar",
        "Singapore Changi Airport (SIN) - Singapore",
        "London Heathrow Airport (LHR) - United Kingdom",
        "New York John F. Kennedy International Airport (JFK) - USA"
    ]
    
    to_airports = [
        "Bengaluru Kempegowda International Airport (BLR) - India",
        "Hyderabad Rajiv Gandhi International Airport (HYD) - India",
        "Kolkata Netaji Subhas Chandra Bose International Airport (CCU) - India",
        "Abu Dhabi Zayed International Airport (AUH) - UAE",
        "Paris Charles de Gaulle Airport (CDG) - France",
        "Frankfurt Airport (FRA) - Germany",
        "Tokyo Haneda Airport (HND) - Japan",
        "Toronto Pearson International Airport (YYZ) - Canada"
    ]
    
    hotels = [
        "Marriott Hotel", "Taj Palace", "Oberoi Grand", "Radisson Blu",
        "Le Meridien", "ITC Grand Chola", "Hilton Garden", "Hyatt Regency",
        "Trident Hotel", "The Park"
    ]

    vehicles = frappe.get_all("Vehicle", pluck="name")
    bookings = frappe.get_all("Booking", pluck="name")

    for i in range(1, 101):
        try:
            # Random values
            guide = random.choice(guides)
            hotel_name = random.choice(hotels)
            room_type = random.choice(room_types)
            from_airport = random.choice(from_airports)
            to_airport = random.choice(to_airports)
            travel_status = random.choice(travel_statuses)
            booking_status = random.choice(booking_statuses)
            flight_number = f"FL{random.randint(1000, 9999)}"
            vehicle = random.choice(vehicles) if vehicles else None
            booking = random.choice(bookings) if bookings else None

            start_date = nowdate()
            end_date = add_days(start_date, random.randint(2, 10))

            # Construct document
            doc = frappe.get_doc({
                "doctype": "Travel Plan",
                "booking": booking,
                "guide": guide,
                "travel_start_date": start_date,
                "travel_end_date": end_date,
                "travel_status": travel_status,
                "flight_number": flight_number,
                "from_airport": from_airport,
                "to_airport": to_airport,
                "departure_date": start_date,
                "departure_time": nowtime(),
                "arrival_date": end_date,
                "arrival_time": nowtime(),
                "return_departure_date": add_days(end_date, 1),
                "return_departure_time": nowtime(),
                "return_arrival_date": add_days(end_date, 2),
                "return_arrival_time": nowtime(),
                "hotel_name": hotel_name,
                "location": random.choice(["Chennai", "Delhi", "Mumbai", "Dubai", "Singapore", "London"]),
                "room_type": room_type,
                "booking_status": booking_status,
                "vehicle": vehicle,
                "pickup": random.choice(["Hotel Lobby", "Airport Terminal", "Main Bus Stop", "Travel Office"]),
                "travel_date": start_date,
                "cost": random.randint(3000, 20000)
            })

            doc.insert(ignore_permissions=True)
            frappe.db.commit()

            print(f"✅ Record {i}: {hotel_name} ({from_airport} → {to_airport}) saved")

        except Exception as e:
            print(f"❌ Error inserting record {i}: {str(e)}")
            frappe.db.rollback()







#-----------------------  Vehicle Records  --------------------------------------------------------------------------------------------------------------------------------
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
    
    
    
    
    
##--------------  Tour Package  ------------------------------------------------------------------------------------------------------

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



#-----------------------  Booking Doctype   --------------------------------------------------------------------------------------------
import frappe
from random import choice, randint
from frappe.utils import nowdate, add_days

def insert_multiple_bookings():
    customers = [d.name for d in frappe.get_all("Customer")]
    packages = [d.name for d in frappe.get_all("Tour Package")]

    if not customers or not packages:
        frappe.throw("Please create some Customer and Tour Package records first.")

    for i in range(1, 101):  # 100 records
        customer = choice(customers)
        tour_package = choice(packages)

        # Fetch package details
        pkg = frappe.get_doc("Tour Package", tour_package)

        booking = frappe.new_doc("Booking")
        booking.customer = customer
        booking.tour_package = tour_package
        booking.tour_package_name = pkg.package_name
        booking.start_date = pkg.start_date
        booking.end_date = pkg.end_date
        booking.package_status = pkg.package_status
        booking.amount = pkg.amount
        booking.package_country = pkg.country
        booking.package_state = pkg.state

        booking.travel_date = add_days(nowdate(), randint(1, 30))
        booking.return_date = add_days(booking.travel_date, randint(3, 10))
        booking.booking_status = choice(["Draft", "Booked", "Confirmed"])
        booking.booking_date = nowdate()

        booking.insert(ignore_permissions=True)
        frappe.db.commit()

    frappe.msgprint("✅ 100 Booking records created successfully!")




#-----------------------------   Payment  --------------------------------------------------------------------------------------------
import frappe
from frappe.utils import nowdate
import random

def insert_multiple_payments():
    customers = [
        "John Doe", "Jane Smith", "Rahul Kumar", "Amit Patel", "Priya Sharma",
        "Ravi Iyer", "Sneha Reddy", "Arjun Mehta", "Fatima Khan", "Vijay Rao",
        "Anjali Nair", "Suresh Das", "Kiran Verma", "Deepak Singh", "Neha Joshi",
        "Manoj Babu", "Lakshmi Devi", "Pooja Mishra", "Ajay Kumar", "Sara Thomas"
    ]

    payment_modes = ["Cash", "UPI", "Credit Card", "Debit Card", "Bank Transfer"]

    for i in range(1, 101):  # ✅ 100 records
        try:
            customer = random.choice(customers)
            amount = random.randint(2000, 10000)
            visa_amount = round(amount * random.uniform(0.4, 0.8), 2)
            advance_amount = round(amount * random.uniform(0.3, 0.7), 2)
            payment_mode = random.choice(payment_modes)

            payment = frappe.get_doc({
                "doctype": "Payment",
                "customer": customer,
                "amount": amount,
                "visa_amount": visa_amount,
                "advance_amount": advance_amount,
                "payment_mode": payment_mode,
                "posting_date": nowdate(),
            })

            payment.insert(ignore_permissions=True)
            frappe.db.commit()
            print(f"✅ Payment {i} created: {payment.name} ({customer}, ₹{amount})")

        except frappe.DuplicateEntryError:
            print(f"⚠️ Skipping duplicate for record {i}")
        except Exception as e:
            print(f"❌ Error on record {i}: {e}")
#--------------------------------------------------------------------------------

import frappe
import random

def insert_multiple_tour_staff_assignments():
    """
    Inserts 100 sample Tour Staff Assignment records with valid data.
    """

    # Get existing link data to maintain relational integrity
    bookings = frappe.get_all("Booking", pluck="name")
    customers = frappe.get_all("Customer", pluck="name")
    guides = frappe.get_all("Guide", fields=["name", "full_name", "email", "phone_number", "status"])

    if not bookings or not customers or not guides:
        frappe.throw("Make sure Booking, Customer, and Guide records exist before running this script.")

    for i in range(1, 101):
        try:
            # Pick random values
            booking = random.choice(bookings)
            customer = random.choice(customers)
            guide_data = random.choice(guides)

            guide_id = guide_data.get("name")
            guide_name = guide_data.get("full_name")
            guide_email = guide_data.get("email")
            guide_phone = guide_data.get("phone_number")
            guide_status = guide_data.get("status")

            booking_status = random.choice(["Confirmed", "Pending", "Cancelled"])

            # Create document
            doc = frappe.get_doc({
                "doctype": "Tour Staff Assignment",
                "booking": booking,
                "customer": customer,
                "guide_id": guide_id,
                "guide": guide_name,
                "booking_status": booking_status,
                "email": guide_email,
                "status": guide_status,
                "phone": guide_phone,
            })

            doc.insert(ignore_permissions=True)
            frappe.db.commit()
            print(f"✅ Record {i} created: {guide_name} → {customer} ({booking_status})")

        except Exception as e:
            frappe.db.rollback()
            print(f"❌ Error creating record {i}: {e}")
#----------------------------------------------------------------------------------------------------------
import frappe
import random
from datetime import datetime, timedelta

def insert_staff_records():
    """
    Create 100 Staff records with unique names, different countries,
    and all fields filled with valid random values.
    """

    customers = frappe.get_all("Customer", pluck="name")
    tours = frappe.get_all("Booking", pluck="name")

    if not customers or not tours:
        frappe.throw("Please ensure that 'Customer' and 'Booking' records exist before running this script.")

    # 100 unique first names
    first_names = [
        "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Krishna", "Ishaan", "Rohan",
        "Ananya", "Diya", "Sara", "Aditi", "Meera", "Ira", "Saanvi", "Navya", "Myra", "Aarohi",
        "Zara", "Kabir", "Tanish", "Parth", "Rudra", "Aryan", "Harsh", "Manav", "Dev", "Raj",
        "Nisha", "Sneha", "Neha", "Priya", "Divya", "Kavya", "Anjali", "Pooja", "Ritika", "Shruti",
        "Abhinav", "Amar", "Akhil", "Ajay", "Aravind", "Naveen", "Surya", "Deepak", "Vikram", "Rahul",
        "Leela", "Lakshmi", "Maya", "Tara", "Nandini", "Anitha", "Vani", "Geeta", "Bhavana", "Revathi",
        "Siddharth", "Yash", "Jay", "Rakesh", "Tarun", "Varun", "Sameer", "Karthik", "Vivek", "Sandeep",
        "Arpita", "Swathi", "Keerthi", "Chandni", "Suhana", "Pavithra", "Rashmi", "Harini", "Megha", "Deeksha",
        "Kiran", "Manisha", "Shravya", "Rajesh", "Vinay", "Kamal", "Lalith", "Roshan", "Hema", "Ashwin",
        "Tanvi", "Avantika", "Riya", "Simran", "Dhruv", "Aniket", "Charan", "Omkar", "Pranav", "Suman"
    ]

    # 100 countries (unique)
    countries = [
        "India", "United States", "United Kingdom", "Canada", "Australia", "Germany", "France", "Italy", "Spain", "Netherlands",
        "Sweden", "Norway", "Denmark", "Finland", "Switzerland", "Austria", "Belgium", "Ireland", "Portugal", "Greece",
        "Russia", "Poland", "Czech Republic", "Hungary", "Romania", "Ukraine", "Turkey", "UAE", "Qatar", "Saudi Arabia",
        "Oman", "Kuwait", "Bahrain", "Egypt", "South Africa", "Nigeria", "Kenya", "Ethiopia", "Morocco", "Ghana",
        "China", "Japan", "South Korea", "Singapore", "Malaysia", "Thailand", "Vietnam", "Philippines", "Indonesia", "Taiwan",
        "Sri Lanka", "Bangladesh", "Nepal", "Bhutan", "Maldives", "Pakistan", "Afghanistan", "Iran", "Iraq", "Israel",
        "Jordan", "Lebanon", "Syria", "Yemen", "Mexico", "Brazil", "Argentina", "Chile", "Peru", "Colombia",
        "Venezuela", "Cuba", "Panama", "Costa Rica", "Jamaica", "Honduras", "Bolivia", "Uruguay", "Paraguay", "Ecuador",
        "New Zealand", "Fiji", "Papua New Guinea", "Tonga", "Samoa", "Solomon Islands", "Vanuatu", "Nauru", "Kiribati", "Palau",
        "Luxembourg", "Monaco", "Liechtenstein", "Iceland", "Andorra", "Malta", "Cyprus", "Estonia", "Latvia", "Lithuania"
    ]

    remarks_list = [
        "Assigned successfully", "Available for next tour", "Closed due to completion",
        "Pending reassignment", "Reallocation required", "Confirmed allocation"
    ]

    for i in range(100):
        try:
            staff_name = f"{first_names[i]} {random.choice(['Singh', 'Patel', 'Kumar', 'Sharma', 'Nair', 'Reddy', 'Das', 'Pillai'])}"
            country = countries[i]
            contact_number = f"+91{random.randint(7000000000, 9999999999)}"
            email = f"{staff_name.replace(' ', '').lower()}@{country.replace(' ', '').lower()}.com"
            assigned_customer = random.choice(customers)
            assigned_tour = random.choice(tours)
            allocation_date = datetime.now().date() - timedelta(days=random.randint(0, 60))
            status = random.choice(["Available", "Closed"])
            remarks = random.choice(remarks_list)

            doc = frappe.get_doc({
                "doctype": "Staff",
                "staff_name": f"{staff_name} ({country})",
                "contact_number": contact_number,
                "email": email,
                "assigned_customer": assigned_customer,
                "assigned_tour": assigned_tour,
                "allocation_date": allocation_date,
                "status": status,
                "remarks": remarks
            })

            doc.insert(ignore_permissions=True)
            frappe.db.commit()
            print(f"✅ Created Staff Record {i+1}: {staff_name} - {country}")

        except Exception as e:
            frappe.db.rollback()
            print(f"❌ Error inserting record {i+1}: {e}")



#-------------------------------------------------------------------------------------------------------------
import frappe
import random
from datetime import datetime, timedelta

def insert_multiple_guides():
    """
    Create 100 Guide records with all field values filled uniquely.
    """

    # Example countries (ensure these exist in Country doctype)
    countries = [
        "India", "United States", "United Kingdom", "Canada", "Australia", "Germany", "France",
        "Italy", "Spain", "Netherlands", "Switzerland", "Norway", "Sweden", "Denmark",
        "Finland", "Japan", "China", "Singapore", "UAE", "Qatar", "Saudi Arabia", "Egypt",
        "South Africa", "Kenya", "Brazil", "Mexico", "Argentina", "Chile", "Thailand",
        "Malaysia", "Vietnam", "Indonesia", "Philippines", "Nepal", "Sri Lanka", "Bangladesh",
        "Pakistan", "Turkey", "Poland", "Portugal", "Greece", "Ireland", "Belgium", "Austria",
        "Czech Republic", "Hungary", "Romania", "Russia", "New Zealand", "South Korea", "Oman",
        "Bahrain", "Kuwait", "Jordan", "Israel", "Iran", "Iraq", "Morocco", "Nigeria", "Ghana",
        "Ethiopia", "Colombia", "Peru", "Venezuela", "Chile", "Uruguay", "Paraguay", "Bolivia",
        "Maldives", "Bhutan", "Fiji", "Panama", "Costa Rica", "Luxembourg", "Monaco", "Cyprus",
        "Malta", "Iceland", "Estonia", "Latvia", "Lithuania", "Slovakia", "Slovenia", "Croatia",
        "Serbia", "Bosnia", "Bulgaria", "Albania", "Georgia", "Ukraine", "Belarus", "Armenia",
        "Azerbaijan", "Moldova", "Kazakhstan", "Uzbekistan", "Myanmar", "Cambodia", "Laos", "Mongolia"
    ]

    first_names = [
        "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Krishna", "Rohan", "Ananya", "Diya", "Sara",
        "Kabir", "Tanish", "Parth", "Rudra", "Aryan", "Harsh", "Dev", "Raj", "Nisha", "Sneha",
        "Neha", "Priya", "Divya", "Kavya", "Anjali", "Pooja", "Ritika", "Shruti", "Abhinav", "Amar",
        "Vikram", "Rahul", "Leela", "Lakshmi", "Maya", "Tara", "Anitha", "Vani", "Geeta", "Bhavana",
        "Siddharth", "Yash", "Rakesh", "Varun", "Karthik", "Vivek", "Sandeep", "Keerthi", "Suhana", "Rashmi",
        "Kiran", "Manisha", "Shravya", "Vinay", "Kamal", "Lalith", "Roshan", "Hema", "Ashwin", "Tanvi",
        "Avantika", "Riya", "Simran", "Dhruv", "Aniket", "Charan", "Omkar", "Pranav", "Suman", "Suresh",
        "Meena", "Rekha", "Bala", "Deepa", "Siva", "Murali", "Aravind", "Mohan", "Kiran", "Sathish",
        "Sujatha", "Ravi", "Nandha", "Priyanka", "Ajay", "Pradeep", "Uma", "Swathi", "Veena", "Ramya",
        "Arpita", "Deeksha", "Vignesh", "Sowmiya", "Rahima", "Sakthi", "Hari", "Navin", "Saran", "Divakar"
    ]

    last_names = [
        "Kumar", "Patel", "Sharma", "Reddy", "Nair", "Das", "Menon", "Singh", "Pillai", "Gupta"
    ]

    languages = [
        "English", "Hindi", "Tamil", "Telugu", "Malayalam", "Kannada", "French", "Spanish", "Arabic", "German"
    ]

    statuses = ["Available", "Assigned", "On Tour", "On Leave", "Inactive", "Blocked"]
    genders = ["Male", "Female", "Other"]

    cities = ["Chennai", "Delhi", "Mumbai", "Bengaluru", "Hyderabad", "Pune", "Kolkata", "Ahmedabad", "Dubai", "Singapore"]
    states = ["Tamil Nadu", "Delhi", "Maharashtra", "Karnataka", "Telangana", "West Bengal", "Gujarat", "Kerala", "Punjab", "Rajasthan"]

    for i in range(100):
        try:
            first_name = first_names[i]
            last_name = random.choice(last_names)
            full_name = f"{first_name} {last_name}"
            gender = random.choice(genders)
            dob = datetime.now().date() - timedelta(days=random.randint(9000, 20000))
            email = f"{first_name.lower()}.{last_name.lower()}@example.com"
            phone = f"+91{random.randint(7000000000, 9999999999)}"
            passport = f"P{random.randint(1000000,9999999)}"
            country = countries[i]
            state = random.choice(states)
            city = random.choice(cities)
            experience = random.randint(1, 20)
            language_known = ", ".join(random.sample(languages, k=random.randint(2, 5)))
            status = random.choice(statuses)
            guide_id = f"G-{i+1:03}"

            doc = frappe.get_doc({
                "doctype": "Guide",
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
                "gender": gender,
                "date_of_birth": dob,
                "email": email,
                "phone_number": phone,
                "passport": passport,
                "country": country,
                "state": state,
                "city": city,
                "guide_id": guide_id,
                "experience": experience,
                "languages_known": language_known,
                "status": status
            })

            doc.insert(ignore_permissions=True)
            frappe.db.commit()
            print(f"✅ Created Guide {i+1}: {full_name} ({country})")

        except Exception as e:
            frappe.db.rollback()
            print(f"❌ Error creating guide {i+1}: {e}")
