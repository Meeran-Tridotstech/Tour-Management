frappe.ui.form.on('Tour Package', {
    refresh(frm) {
        calculate_days_left(frm);
    },

    // ----------------- Start and End Date Logic -----------------
    start_date(frm) {
        if (frm.doc.start_date) {
            // Auto add 30 days to Start Date
            let end_date = frappe.datetime.add_days(frm.doc.start_date, 30);
            frm.set_value('end_date', end_date);

            // Make End Date read-only
            frm.set_df_property('end_date', 'read_only', 1);
        }

        calculate_days_left(frm);
    },

    end_date(frm) {
        calculate_days_left(frm);
    },

    // ----------------- Package Code Generation -----------------
    package_name(frm) {
        if (frm.doc.package_name) {
            let short_name = frm.doc.package_name.replace(/\s+/g, '').substring(0, 3).toUpperCase();
            let random_number = Math.floor(100 + Math.random() * 900);
            frm.set_value('package_code', `PKG-${short_name}-${random_number}`);
        }
    },

    // ----------------- Country → State Dynamic Filter -----------------
    country(frm) {
        if (!frm.doc.country) return;

        frappe.call({
            method: "gofly_journeys.gofly_journeys.doctype.customer.customer.get_states_for_country",
            args: { country: frm.doc.country },
            callback: function (r) {
                let state_options = r.message && r.message.length ? [''].concat(r.message) : [''];
                frm.set_df_property('state', 'options', state_options);
                frm.refresh_field('state');
            }
        });
    }
});


// ------------------ Calculate Days Left (Based on Today → End Date) ------------------
function calculate_days_left(frm) {
    if (frm.doc.end_date) {
        // Get today's date and end date
        let today = frappe.datetime.now_date();
        let today_obj = frappe.datetime.str_to_obj(today);
        let end_obj = frappe.datetime.str_to_obj(frm.doc.end_date);

        // Calculate difference in milliseconds
        let diff_ms = end_obj - today_obj;

        // If already ended
        if (diff_ms < 0) {
            frm.set_value("days_left", "0 days left");
            frm.set_value("package_status", "Closed");  // Automatically close the package
            return;
        }

        // Convert to days
        let diff_days = Math.floor(diff_ms / (1000 * 60 * 60 * 24));

        // Set readable value
        frm.set_value(
            "days_left",
            `${diff_days} day${diff_days !== 1 ? "s left" : " left"}`
        );

        // If days_left > 0 and status is not Closed, keep as Available
        if (diff_days > 0 && frm.doc.package_status !== "Closed") {
            frm.set_value("package_status", "Available");
        }
    } else {
        frm.set_value("days_left", "");
        if (!frm.doc.package_status) {
            frm.set_value("package_status", "Available");  // default if empty
        }
    }
}
