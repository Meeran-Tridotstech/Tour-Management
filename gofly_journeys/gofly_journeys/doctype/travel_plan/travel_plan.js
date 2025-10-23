frappe.ui.form.on("Travel Plan", {
    from_airport: function(frm) { fetchFlights(frm); },
    to_airport: function(frm) { fetchFlights(frm); }
});

function fetchFlights(frm) {
    if (!frm.doc.from_airport || !frm.doc.to_airport) return;

    frappe.call({
        method: "gofly_journeys.gofly_journeys.doctype.travel_plan.travel_plan.fetch_flights_between",
        args: {
            dep_icao: frm.doc.from_airport,  // e.g. 'VIDP'
            arr_icao: frm.doc.to_airport     // e.g. 'VOMM'
        },
        freeze: true,
        freeze_message: "Fetching flights...",
        callback: function(r) {
            if (r.message && r.message.length > 0) {
                let flight = r.message[0]; // pick first flight
                frm.set_value("flight_number", flight.callsign);
                frm.set_value("departure_time", flight.departure_time);
                frm.set_value("arrival_time", flight.arrival_time);
                frm.set_value("departure_airport", flight.departure_airport);
                frm.set_value("arrival_airport", flight.arrival_airport);
                frm.refresh_fields();
                frappe.msgprint(`Found ${r.message.length} flights from ${frm.doc.from_airport} → ${frm.doc.to_airport}`);
            } else {
                frappe.msgprint("No flights found for this route in the last 24h");
            }
        }
    });
}
