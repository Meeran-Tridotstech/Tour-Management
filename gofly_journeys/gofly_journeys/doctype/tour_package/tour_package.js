
frappe.ui.form.on('Tour Package', {
    refresh(frm) {
        calculate_days_left(frm);
        set_status_color(frm.doc.package_status);

        if (frm.doc.images && frm.doc.images.length > 0) {
            show_image_slider(frm);
        } else {
            frm.fields_dict.image_slider.$wrapper.html("<p>No images found.</p>");
        }
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
    },

    // ----------------- Expected Trip Month → Up To -----------------
    expected_trip_month(frm) {
        if (!frm.doc.expected_trip_month) return;

        // All months
        let months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ];

        // Find index of selected month
        let start_index = months.indexOf(frm.doc.expected_trip_month);

        // Get next 2 months
        let next_months = [];
        for (let i = 1; i <= 2; i++) {
            let idx = (start_index + i) % 12; // wrap around December → January
            next_months.push(months[idx]);
        }

        // Set options for 'up_to' field
        frm.set_df_property('up_to', 'options', [''].concat(next_months));
        frm.refresh_field('up_to');

        // Clear previous value
        frm.set_value('up_to', '');
    }
});


// ------------------ Calculate Days Left (Based on Today → End Date) ------------------
function calculate_days_left(frm) {
    if (frm.doc.end_date) {
        // Get today's date and end date
        let today = frappe.datetime.now_date();
        let today_obj = frappe.datetime.str_to_obj(today);
        let end_obj = frappe.datetime.str_to_obj(frm.doc.end_date);

        // Calculate difference
        let diff_ms = end_obj - today_obj;

        // If already ended
        if (diff_ms < 0) {
            frm.set_value("days_left", "0 days left");
            frm.set_value("package_status", "Closed");
            set_status_color("Closed");
            return;
        }

        // Convert to days
        let diff_days = Math.floor(diff_ms / (1000 * 60 * 60 * 24));

        // Set readable value
        frm.set_value(
            "days_left",
            `${diff_days} day${diff_days !== 1 ? "s left" : " left"}`
        );

        // Change status and color
        if (diff_days > 3) {
            frm.set_value("package_status", "Available");
            set_status_color("Available");
        } else if (diff_days <= 3 && diff_days > 0) {
            frm.set_value("package_status", "Available");
            set_status_color("Expiring");
        }
    } else {
        frm.set_value("days_left", "");
        if (!frm.doc.package_status) {
            frm.set_value("package_status", "Available");
            set_status_color("Available");
        }
    }
}


// ---------------- Color Logic ----------------
function set_status_color(status) {
    setTimeout(() => {
        let field = document.querySelector('[data-fieldname="package_status"]');
        if (!field) return;

        let input = field.querySelector('.control-value');
        if (!input) return;

        if (status === "Available") {
            input.style.color = "green";
        } else if (status === "Expiring") {
            input.style.color = "orange";
        } else if (status === "Closed") {
            input.style.color = "red";
        } else {
            input.style.color = "black";
        }
    }, 500);
}


function show_image_slider(frm) {
    let images = frm.doc.images.map(i => i.image).filter(Boolean);

    if (!images.length) return;

    // Generate HTML for images
    let img_html = images
        .map(img => `<img src="${img}" alt="Tour Image">`)
        .join("");

    let total_images = images.length;
    let total_duration = total_images * 3; // 3 seconds per image

    // Build slider HTML
    let html = `
        <div class="image-slider">
            <div class="slides">
                ${img_html}
            </div>
        </div>

        <style>
        .image-slider {
            width: 100%;
            overflow: hidden;
            position: relative;
            border-radius: 10px;
        }
        .slides {
            display: flex;
            width: calc(100% * ${total_images});
            animation: slide ${total_duration}s infinite steps(${total_images});
        }
        .slides img {
            width: 100%;
            height: 400px;
            object-fit: cover;
        }
        @keyframes slide {
            from { transform: translateX(0); }
            to { transform: translateX(-${(total_images - 1) * 100}%); }
        }
        </style>
    `;

    // Inject HTML into the HTML field
    frm.fields_dict.image_slider.$wrapper.html(html);
}