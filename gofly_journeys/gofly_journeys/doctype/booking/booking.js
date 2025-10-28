frappe.ui.form.on('Booking', {
    refresh(frm) {
        gofly.common.add_open_related_button(frm);
        const roles = frappe.user_roles;
        const is_guide = roles.includes('Guide');

        // ======================================
        // 🔒 Child Table Visa Fields Read-only for Non-Guides
        // ======================================
        const visa_fields = [
            'visa_status',
            'visa_approved_date',
            'visa_expiry_date',
            'visa_document',
            'remarks'
        ];

        visa_fields.forEach(field => {
            frm.fields_dict.booking_members.grid.update_docfield_property(field, 'read_only', !is_guide);
            if (!is_guide) {
                frm.fields_dict.booking_members.grid.wrapper
                    .find(`[data-fieldname="${field}"]`)
                    .css('background-color', '#f8f9fa');
            }
        });

        // ======================================
        // 💳 Make Payment Button UI
        // ======================================
        frm.fields_dict.make_payment.$wrapper.html(`
            <div style="text-align:right; margin-top:10px;">
                <button id="go_to_payment" class="btn btn-success custom-payment-btn">
                    Prview & Goto Payment
                </button>
            </div>
            <style>
                .custom-payment-btn {
                    background-color: #28a745 !important;
                    color: white !important;
                    border: none;
                    border-radius: 6px;
                    padding: 18px 18px;
                    font-weight: 600;
                    font-size: 14px;
                    transition: all 0.3s ease-in-out;
                }
                .custom-payment-btn:hover {
                    background-color: #218838 !important;
                    transform: scale(1.05);
                    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                }
            </style>
        `);

        // ======================================
        // 💰 Payment Creation Logic
        // ======================================
        frm.fields_dict.make_payment.$wrapper.find('#go_to_payment').on('click', function () {
            if (!frm.doc.customer) {
                frappe.msgprint(__('Please select a Customer first.'));
                return;
            }

            // 🔍 Check if Payment already exists for same Booking + Customer
            frappe.db.get_value('Payment', {
                customer: frm.doc.customer,
                booking: frm.doc.name
            }, 'name').then(r => {
                if (r.message && r.message.name) {
                    frappe.msgprint(__('Payment already exists for this Booking & Customer.'));
                    frappe.set_route('Form', 'Payment', r.message.name);
                    return;
                }

                // ✅ Create New Payment
                const total_amount = (frm.doc.amount || 0) + (frm.doc.total_visa_fee || 0);
                const advance_amount = Math.ceil(total_amount / 3);
                const balance_amount = total_amount; // 🔹 initial full balance

                frappe.call({
                    method: 'frappe.client.insert',
                    args: {
                        doc: {
                            doctype: 'Payment',
                            customer: frm.doc.customer,
                            booking: frm.doc.name,
                            amount: frm.doc.amount || 0,
                            visa_amount: frm.doc.total_visa_fee || 0,
                            total_amount,
                            advance_amount,
                            balance_amount, // 🔹 added
                            pay_amount: advance_amount,
                            payment_count: 0,
                            payment_status: 'Pending'
                        }
                    },
                    callback: function (r) {
                        if (r.message) {
                            frappe.msgprint(__('✅ Payment record created successfully!'));
                            frappe.set_route('Form', 'Payment', r.message.name);

                        }
                    }
                });
            });
        });


        // ======================================
        // 🌍 Enhanced Terms & Conditions (Tour Management)
        // ======================================
        const html_content = `
                <div style="
                    max-height:380px; 
                    overflow:auto; 
                    border:2px solid #3498db; 
                    padding:20px; 
                    border-radius:12px; 
                    background:linear-gradient(180deg, #f5f7fa, #e3f2fd);
                    font-family:'Poppins', 'Segoe UI', sans-serif;
                    color:#2c3e50;
                ">
                    <h2 style="text-align:center; color:#1565c0; font-weight:600; margin-bottom:15px;">
                        📜 Tour Booking Terms & Conditions
                    </h2>
                    <p style="font-size:14px; color:#34495e; text-align:center;">
                        Please review each point carefully before confirming your agreement.
                    </p>

                    <ul style="margin-top:15px; line-height:1.8; font-size:14px; padding-left:20px;">
                        <li>Bookings are confirmed only after advance payment.</li>
                        <li>Balance payment must be made before the tour start date.</li>
                        <li>Cancellations within 15 days are non-refundable.</li>
                        <li>Refunds (if any) will be processed within 7–10 working days.</li>
                        <li>Company reserves the right to modify or cancel tours due to unforeseen events (weather, strikes, etc.).</li>
                        <li>Travelers must carry valid ID, passport, visa, and travel documents.</li>
                        <li>Company is not liable for loss of baggage, delays, or personal belongings.</li>
                        <li>Participants must follow the guide’s instructions and maintain discipline during the tour.</li>
                        <li>Any property damage caused by participants will be charged accordingly.</li>
                        <li>Travel insurance is highly recommended and must be arranged by the traveler.</li>
                        <li>Company is not responsible for delays caused by transportation or external factors.</li>
                        <li>Medical emergencies are at the traveler’s own expense. Assistance will be provided as feasible.</li>
                        <li>Child fare and age policies apply as per the chosen package.</li>
                        <li>Any disputes shall be handled under the jurisdiction of the company’s registered city.</li>
                    </ul>

                    <p style="color:#e67e22; text-align:center; margin-top:18px; font-weight:600;">
                        ✅ Please ensure you have read and understood all the terms before proceeding with booking.
                    </p>
                </div>
            `;

        frm.fields_dict.terms_and_conditions.$wrapper.html(html_content);

        // 🔒 Restrict VISA fields (Parent)
        frm.set_df_property('visa_status', 'read_only', !is_guide);
        frm.set_df_property('visa_approved_date', 'read_only', !is_guide);
        frm.set_df_property('visa_documents', 'read_only', !is_guide);

    },

    before_save(frm) {
        if (!frm.doc.accept_tnc) {
            frappe.throw('Please accept Terms & Conditions before booking.');
        }
    },
    tour_package: function(frm) {
        if (frm.doc.tour_package) {
            // Fetch months from linked Tour Package
            frappe.db.get_value("Tour Package", frm.doc.tour_package, ["expected_trip_month", "up_to"])
            .then(r => {
                if (r.message) {
                    frm.expected_trip_month = r.message.expected_trip_month;
                    frm.up_to = r.message.up_to;
                }
            });
        }
    },

    travel_date: function(frm) {
        validate_month_range(frm, "travel_date");
    },

    return_date: function(frm) {
        validate_month_range(frm, "return_date");

        // Optional: logical check - return_date must be after travel_date
        if (frm.doc.travel_date && frm.doc.return_date) {
            const t1 = frappe.datetime.str_to_obj(frm.doc.travel_date);
            const t2 = frappe.datetime.str_to_obj(frm.doc.return_date);
            if (t2 < t1) {
                frappe.msgprint("Return Date cannot be before Travel Date.");
                frm.set_value("return_date", null);
            }
        }
    }
});

function validate_month_range(frm, fieldname) {
    if (!frm.doc.tour_package || !frm.doc[fieldname]) return;

    frappe.db.get_value("Tour Package", frm.doc.tour_package, ["expected_trip_month", "up_to"])
    .then(r => {
        if (!r.message) return;

        const from_month = r.message.expected_trip_month;
        const to_month = r.message.up_to;
        const selected_date = frappe.datetime.str_to_obj(frm.doc[fieldname]);

        const month_map = {
            "January": 0,
            "February": 1,
            "March": 2,
            "April": 3,
            "May": 4,
            "June": 5,
            "July": 6,
            "August": 7,
            "September": 8,
            "October": 9,
            "November": 10,
            "December": 11
        };

        const from_index = month_map[from_month];
        const to_index = month_map[to_month];
        const selected_index = selected_date.getMonth();

        // Validate if selected month is within range
        if (selected_index < from_index || selected_index > to_index) {
            frappe.msgprint(`Please select a date between ${from_month} and ${to_month}`);
            frm.set_value(fieldname, null);
        }
    });
}

// ======================================
// 🔹 Booking Member Child Table
// ======================================
frappe.ui.form.on('Booking Member', {
    visa_approved_date(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        if (row.visa_approved_date && row.visa_type) {
            const approved = frappe.datetime.str_to_obj(row.visa_approved_date);
            const expiry = frappe.datetime.add_days(approved, 90);
            frappe.model.set_value(cdt, cdn, 'visa_expiry_date', frappe.datetime.obj_to_str(expiry));
        }
    },

    age(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        if (!row.age || row.age <= 0) {
            frappe.msgprint(__('Age must be greater than 0.'));
            frappe.model.set_value(cdt, cdn, 'age', '');
        } else if (row.age < 18) {
            frappe.msgprint(__('⚠️ {0} is under 18.', [row.member_name]));
        } else if (row.age > 100) {
            frappe.throw(__('❌ Invalid age for {0}.', [row.member_name]));
        }
    },

    visa_type(frm, cdt, cdn) {
        const visa_fees = {
            "Tourist Visa": 3000,
            "Business Visa": 5000,
            "Student Visa": 7000,
            "Work Visa": 6000,
            "Medical Visa": 4500,
            "Transit Visa": 2000,
            "Diplomatic Visa": 0
        };
        const row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'visa_fee', visa_fees[row.visa_type] || 0);
        calculate_total_visa_fee(frm);
    },

    visa_fee(frm) { calculate_total_visa_fee(frm); },
    booking_members_add(frm) { calculate_total_visa_fee(frm); },
    booking_members_remove(frm) { calculate_total_visa_fee(frm); },
});

// ======================================
// 🔹 Calculate Total Visa Fee
// ======================================
function calculate_total_visa_fee(frm) {
    const total = (frm.doc.booking_members || []).reduce((sum, row) => sum + (row.visa_fee || 0), 0);
    frm.set_value('total_visa_fee', total);
}
