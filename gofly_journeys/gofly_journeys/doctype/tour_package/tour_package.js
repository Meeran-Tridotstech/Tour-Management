frappe.ui.form.on('Tour Package', {
    start_date: function(frm) {
        if (frm.doc.start_date) {
            // Add 5 days to Start Date
            let end_date = frappe.datetime.add_days(frm.doc.start_date, 5);
            frm.set_value('end_date', end_date);

            // Make End Date read-only
            frm.set_df_property('end_date', 'read_only', 1);
        }
    },
    validate: function(frm) {
        if (!frm.doc.start_date) {
            frappe.throw(__('Start Date is mandatory.'));
        }
        if (!frm.doc.end_date) {
            frappe.throw(__('End Date is mandatory.'));
        }

        let diff = frappe.datetime.get_diff(frm.doc.end_date, frm.doc.start_date);
        if (diff < 5) {
            frappe.throw(__('Tour duration must be at least 5 days.'));
        }
    },
    // --------------------- Package code
    package_name: function(frm) {
        if(frm.doc.package_name) {
            // Remove spaces and take first 3 letters (uppercase)
            let short_name = frm.doc.package_name.replace(/\s+/g, '').substring(0, 3).toUpperCase();
            
            // Generate random 3-digit number
            let random_number = Math.floor(100 + Math.random() * 900);

            // Set Package Code
            frm.set_value('package_code', `PKG-${short_name}-${random_number}`);
        }
    },
    book_now: function(frm) {
        // This runs when the Button field "book_now" is clicked
        frappe.new_doc('Booking', {
            tour_package: frm.doc.name, // Prefill tour_package field in Booking
            // Optional: prefill customer if needed
            // customer: frm.doc.customer || ''
        });
    }
});





