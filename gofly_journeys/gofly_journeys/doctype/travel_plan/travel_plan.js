frappe.ui.form.on('Travel Plan', {
    to_airport: function(frm) {
        if (frm.doc.to_airport) {
            // Just copy the value directly
            frm.set_value('pickup', frm.doc.to_airport);
            frm.set_value('travel_date', frm.doc.arrival_date);
        } else {
            frm.set_value('pickup', '');
            frm.set_value('travel_date', '');

        }
    }
});
