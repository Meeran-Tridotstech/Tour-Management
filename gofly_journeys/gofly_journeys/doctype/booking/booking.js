frappe.ui.form.on('Booking', {
    refresh(frm) {

        // ============================================
        // 🔹 ROLE VALIDATION
        // ============================================
        const roles = frappe.user_roles;
        const is_guide = roles.includes('Guide');

        // List of visa-related fields in the child table
        const visa_fields = [
            'visa_status',
            'visa_approved_date',
            'visa_expiry_date',
            'visa_document',
            'remarks'
        ];

        // Loop through each field and set read_only based on role
        visa_fields.forEach(field => {
            frm.fields_dict.booking_members.grid.update_docfield_property(
                field,
                'read_only',
                !is_guide
            );

            // Optional: change background color for read-only fields
            if (!is_guide) {
                frm.fields_dict.booking_members.grid.wrapper
                    .find(`[data-fieldname="${field}"]`)
                    .css('background-color', '#f8f9fa');
            }
        });

        // ============================================
        // 💳 Make Payment Button
        // ============================================
        frm.fields_dict.make_payment.$wrapper.html(`
            <div style="text-align: right; margin-top: 10px;">
                <button id="go_to_payment" class="btn btn-success custom-payment-btn">
                    💳 Make Payment
                </button>
            </div>

            <style>
                .custom-payment-btn {
                    background-color: #28a745 !important;
                    color: white !important;
                    border: none;
                    border-radius: 6px;
                    padding: 8px 18px;
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

        frm.fields_dict.make_payment.$wrapper.find('#go_to_payment').on('click', function () {
            if (!frm.doc.customer) {
                frappe.msgprint(__('Please select a Customer first.'));
                return;
            }
            frappe.new_doc('Payment', {
                customer: frm.doc.customer,
                booking: frm.doc.name,
                amount: frm.doc.amount
            });
        });

        // ============================================
        // 📜 Terms & Conditions HTML Content
        // ============================================
        const html_content = `
            <div style="max-height:350px; overflow:auto; border:1px solid #ddd; padding:15px; border-radius:8px; background:#fafafa; font-family: Arial, sans-serif;">
                <h3 style="text-align:center; margin-bottom:10px; color:#2c3e50;">Terms & Conditions</h3>

                <h4 style="color:#2980b9;">1. Booking & Confirmation</h4>
                <ul>
                    <li><strong>All bookings are subject to availability.</strong></li>
                    <li>Booking is confirmed only after full or advance payment.</li>
                    <li><strong style="color:#e74c3c;">Customers must provide accurate personal information.</strong></li>
                    <li>Special requests (room, meals) are subject to availability.</li>
                </ul>

                <h4 style="color:#2980b9;">2. Payment Terms</h4>
                <ul>
                    <li><strong>Advance payment of X% is required</strong> to confirm the booking.</li>
                    <li>Remaining balance must be paid at least Y days before tour start.</li>
                    <li>Accepted payments: Bank transfer, Credit/Debit card, UPI, Online Payment.</li>
                    <li><strong style="color:#e74c3c;">Late payment may lead to booking cancellation without refund.</strong></li>
                </ul>

                <h4 style="color:#2980b9;">3. Cancellation & Refund Policy</h4>
                <ul>
                    <li>Cancellation >30 days: full refund minus processing fee.</li>
                    <li>Cancellation 15–30 days: 50% refund.</li>
                    <li><strong style="color:#e74c3c;">Cancellation less than 15 days: no refund.</strong></li>
                    <li>Cancellation by operator: full refund or alternate dates offered.</li>
                </ul>

                <h4 style="color:#2980b9;">4. Travel & Accommodation</h4>
                <ul>
                    <li>Hotels are based on double occupancy unless specified.</li>
                    <li>Additional charges for single occupancy or extra guests.</li>
                    <li>Travel insurance is recommended.</li>
                    <li><strong style="color:#e74c3c;">Carry valid ID or passport as required.</strong></li>
                </ul>

                <h4 style="color:#2980b9;">5. Customer Conduct & Liability</h4>
                <ul>
                    <li>Customers must follow local laws and respect customs.</li>
                    <li><strong style="color:#e74c3c;">Operator is not responsible for personal injury or loss of belongings.</strong></li>
                    <li>Misbehavior or property damage may lead to removal without refund.</li>
                </ul>

                <h4 style="color:#2980b9;">6. Force Majeure</h4>
                <ul>
                    <li>Operator is not liable for natural disasters, strikes, pandemics, or government restrictions.</li>
                    <li>Alternative arrangements or refunds may be offered according to policy.</li>
                </ul>

                <p style="margin-top:10px; font-style:italic; text-align:center; color:#c0392b;">
                    <strong>By booking, you agree to all terms & conditions.</strong>
                </p>
            </div>
        `;

        frm.fields_dict.terms_and_conditions.$wrapper.html(html_content);

        // ============================================
        // 🔒 Restrict VISA Fields (Parent)
        // ============================================
        frm.set_df_property('visa_status', 'read_only', !is_guide);
        frm.set_df_property('visa_approved_date', 'read_only', !is_guide);
        frm.set_df_property('visa_documents', 'read_only', !is_guide);
    },

    // ==============================
    // 2️⃣ Before Save Event
    // ==============================
    before_save(frm) {
        if (!frm.doc.accept_tnc) {
            frappe.throw("Please accept Terms & Conditions before booking.");
        }
    },

});


frappe.ui.form.on('Booking Member', {
    visa_approved_date(frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        if (row.visa_approved_date && row.visa_type) {
            // Set expiry date automatically (e.g., 90 days validity)
            let duration = 90;
            let approved = frappe.datetime.str_to_obj(row.visa_approved_date);
            let expiry = frappe.datetime.add_days(approved, duration);
            frappe.model.set_value(cdt, cdn, 'visa_expiry_date', frappe.datetime.obj_to_str(expiry));
        }
    },

    age(frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        if (!row.age || row.age <= 0) {
            frappe.msgprint(__('Age must be greater than 0.'));
            frappe.model.set_value(cdt, cdn, 'age', '');
            return;
        }

        if (row.age < 18) {
            frappe.msgprint(__('⚠️ Member {0} is under 18. Please ensure a guardian is assigned.', [row.member_name]));
        }

        if (row.age > 100) {
            frappe.throw(__('❌ Invalid age for {0}. Age cannot exceed 100 years.', [row.member_name]));
        }
    },

    before_save(frm) {
        // Validate all members before saving
        (frm.doc.booking_members || []).forEach(row => {
            if (!row.age || row.age <= 0) {
                frappe.throw(__('Please enter a valid age for {0}.', [row.member_name]));
            }
            if (row.age > 100) {
                frappe.throw(__('Invalid age for {0}. Must be less than 100.', [row.member_name]));
            }
        });
        // Update total visa fee before saving
        calculate_total_visa_fee(frm);
    },

    visa_type(frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        // Visa Type → Fee mapping
        const visa_fees = {
            "Tourist Visa": 3000,
            "Business Visa": 5000,
            "Student Visa": 7000,
            "Work Visa": 6000,
            "Medical Visa": 4500,
            "Transit Visa": 2000,
            "Diplomatic Visa": 0
        };

        let fee = visa_fees[row.visa_type] || 0;
        frappe.model.set_value(cdt, cdn, "visa_fee", fee);

        // Update total visa fee whenever visa fee changes
        calculate_total_visa_fee(frm);
    },

    // Also recalc if visa_fee manually changed
    visa_fee(frm, cdt, cdn) {
        calculate_total_visa_fee(frm);
    },

    // Recalc when a row is removed
    booking_members_remove(frm, cdt, cdn) {
        calculate_total_visa_fee(frm);
    },

    // Optional: Recalc when a row is added
    booking_members_add(frm, cdt, cdn) {
        calculate_total_visa_fee(frm);
    }
});

// ------------------- FUNCTION: Calculate Total Visa Fee -------------------
function calculate_total_visa_fee(frm) {
    let total = 0;
    (frm.doc.booking_members || []).forEach(row => {
        total += flt(row.visa_fee);
    });
    frm.set_value("total_visa_fee", total);
    frm.refresh_field("total_visa_fee");
}