// Copyright (c) 2025, GoFly Journeys and contributors
// For license information, please see license.txt

frappe.ui.form.on('Guide', {
    first_name: function(frm) {
        set_full_name(frm);
    },
    last_name: function(frm) {
        set_full_name(frm);
    }
});

function set_full_name(frm) {
    let first = frm.doc.first_name || "";
    let last = frm.doc.last_name || "";
    frm.set_value('full_name', (first + " " + last).trim());
}

// -------------guide id-------------

frappe.ui.form.on('Guide', {
    before_save: function(frm) {
        // Generate Guide ID only if it is empty
        if (!frm.doc.guide_id) {
            frm.set_value('guide_id', generate_unique_id());
        }
    }
});

// Function to generate a 6-digit alphanumeric Guide ID
function generate_unique_id(length = 6) {
    let chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
}
