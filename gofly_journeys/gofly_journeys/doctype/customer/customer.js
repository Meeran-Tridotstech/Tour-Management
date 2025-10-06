// Copyright (c) 2025, GoFly Journeys and contributors
// For license information, please see license.txt


frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        // Add a custom button on top
        frm.add_custom_button(__('Go to Tour Package'), function() {
            // Redirect to the Tour Package List view
            frappe.set_route('List', 'Tour Package');
        }); 
    }
});

