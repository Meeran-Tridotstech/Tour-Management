frappe.ui.form.on('Travel Plan', {
    to_airport: function(frm) {
        if (frm.doc.to_airport) {
            // Just copy the value directly
            frm.set_value('pickup', frm.doc.to_airport);
            frm.set_value('travel_date', frm.doc.arrival_date);
            frm.set_value('departure_date', frm.doc.travel_start_date);
            frm.set_value('return_departure_date', frm.doc.travel_end_date);


        } else {
            frm.set_value('pickup', '');
            frm.set_value('travel_date', '');

        }
    }
});
