frappe.ui.form.on('Tour Package', {
    refresh(frm) {
        calculate_days_left(frm);
        set_status_color(frm.doc.package_status);

        // ------------------ Image Slider ------------------
        if (frm.doc.images && frm.doc.images.length > 0) {
            show_image_slider(frm);
        } else {
            frm.fields_dict.image_slider.$wrapper.html("<p>No images found.</p>");
        }

        // ------------------ BOOK NOW Button Logic ------------------
        if (frm.fields_dict.book_now && frm.doc.docstatus < 2) {
            // Remove old click handler before adding new one
            frm.fields_dict.book_now.$input.off("click").on("click", function () {
                create_booking_from_package(frm);
            });
        }

        // ------------------ Styling BOOK NOW Button ------------------
        setTimeout(() => {
            let btn = frm.fields_dict.book_now?.$input;
            if (btn) {
                btn.css({
                    "width": "205%",
                    "background-color": "#007bff",
                    "color": "white",
                    "font-weight": "600",
                    "border": "none",
                    "border-radius": "6px",
                    "padding": "10px",
                    "font-size": "15px",
                    "cursor": "pointer",
                    "transition": "0.3s",
                });
                btn.hover(
                    function () {
                        $(this).css("background-color", "#0056b3");
                    },
                    function () {
                        $(this).css("background-color", "#007bff");
                    }
                );
            }
        }, 500);



        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "User",
                name: frappe.session.user
            },
            callback: function (r) {
                if (r.message) {
                    let roles = r.message.roles.map(role => role.role);
                    // Show 'images' field only if user has 'Staff' role
                    if (roles.includes("Staff"&&"Administrator")) {
                        frm.set_df_property('images', 'hidden', 0);
                    } else {
                        frm.set_df_property('images', 'hidden', 1);
                    }
                }
            }
        });

        
    },

    // ----------------- Start and End Date Logic -----------------
    start_date(frm) {
        if (frm.doc.start_date) {
            let end_date = frappe.datetime.add_days(frm.doc.start_date, 30);
            frm.set_value('end_date', end_date);
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

        let months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ];

        let start_index = months.indexOf(frm.doc.expected_trip_month);
        let next_months = [];
        for (let i = 1; i <= 2; i++) {
            let idx = (start_index + i) % 12;
            next_months.push(months[idx]);
        }

        frm.set_df_property('up_to', 'options', [''].concat(next_months));
        frm.refresh_field('up_to');
        frm.set_value('up_to', '');
    }
});


// ------------------ Create Booking Record from Tour Package ------------------
function create_booking_from_package(frm) {
    frappe.new_doc('Booking', {
        tour_package: frm.doc.name,             // Link field to Tour Package
        tour_package_name: frm.doc.package_name, // Optional (if exists)
        start_date: frm.doc.start_date,
        end_date: frm.doc.end_date,
        package_status: frm.doc.package_status,
        amount: frm.doc.amount,                 // optional
        country: frm.doc.country,               // optional
        state: frm.doc.state                    // optional
    });
}


// ------------------ Calculate Days Left ------------------
function calculate_days_left(frm) {
    if (frm.doc.end_date) {
        let today = frappe.datetime.now_date();
        let today_obj = frappe.datetime.str_to_obj(today);
        let end_obj = frappe.datetime.str_to_obj(frm.doc.end_date);
        let diff_ms = end_obj - today_obj;

        if (diff_ms < 0) {
            frm.set_value("days_left", "0 days left");
            frm.set_value("package_status", "Closed");
            set_status_color("Closed");
            return;
        }

        let diff_days = Math.floor(diff_ms / (1000 * 60 * 60 * 24));
        frm.set_value("days_left", `${diff_days} day${diff_days !== 1 ? "s left" : " left"}`);

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


// ------------------ Status Color ------------------
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

// function show_image_slider(frm) {
//     let images = frm.doc.images.map(i => i.image).filter(Boolean);
//     if (!images.length) return;

//     let img_html = images.map(img => `<img src="${img}" alt="Tour Image">`).join("");
//     let total_images = images.length;
//     let total_duration = total_images * 2; // 1s per image

//     let html = `
//         <div class="image-slider">
//             <div class="slides">
//                 ${img_html}
//             </div>
//         </div>

//         <style>
//         .image-slider {
//             width: 100%;
//             overflow: hidden;
//             position: relative;
//             border-radius: 10px;
//         }
//         .slides {
//             display: flex;
//             width: ${total_images * 100}%;
//             animation: slide ${total_duration}s linear infinite;
//         }
//         .slides img {
//             width: ${100 / total_images}%;
//             height: 400px;
//             object-fit: cover;
//         }
//         @keyframes slide {
//             0% { transform: translateX(0); }
//             100% { transform: translateX(-${(total_images - 1) * (100 / total_images)}%); }
//         }
//         .image-slider:hover .slides {
//             animation-play-state: paused;
//         }
//         </style>
//     `;
//     frm.fields_dict.image_slider.$wrapper.html(html);
// }


function show_image_slider(frm) {
    let images = (frm.doc.images || []).map(i => i.image).filter(Boolean);
    if (!images.length) return;

    // Build HTML for slider
    let img_html = images.map((img, idx) => `
        <div class="slide${idx === 0 ? ' active' : ''}">
            <img src="${img}" alt="Tour Image">
        </div>
    `).join("");

    let html = `
        <div class="image-slider">
            ${img_html}
            <button class="prev">&#10094;</button>
            <button class="next">&#10095;</button>
        </div>

        <style>
        .image-slider {
            position: relative;
            width: 100%;
            max-width: 1000px;
            height: 370px;
            margin: auto;
            overflow: hidden;
            border-radius: 10px;
        }
        .image-slider img {
            width: 100%;
            height: 100%;
            object-fit: content;
            display: block;
        }
        .slide {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            opacity: 0;
            transition: opacity 0.8s ease-in-out;
        }
        .slide.active {
            opacity: 1;
        }
        .image-slider button {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(0,0,0,0.4);
            color: #fff;
            border: none;
            padding: 10px;
            font-size: 24px;
            border-radius: 50%;
            cursor: pointer;
            z-index: 10;
        }
        .image-slider .prev { left: 10px; }
        .image-slider .next { right: 10px; }
        </style>
    `;

    // Inject HTML
    frm.fields_dict.image_slider.$wrapper.html(html);

    // Slider logic
    let currentIndex = 0;
    const slides = frm.fields_dict.image_slider.$wrapper.find('.slide');

    function showSlide(index) {
        slides.removeClass('active');
        slides.eq(index).addClass('active');
    }

    // Auto slide every 3 seconds
    let slideInterval = setInterval(() => {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }, 3000);

    // Prev/Next buttons
    frm.fields_dict.image_slider.$wrapper.find('.prev').on('click', function() {
        clearInterval(slideInterval);
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    });

    frm.fields_dict.image_slider.$wrapper.find('.next').on('click', function() {
        clearInterval(slideInterval);
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    });
}
