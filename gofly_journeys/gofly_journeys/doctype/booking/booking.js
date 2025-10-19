frappe.ui.form.on('Booking', {
    refresh(frm) {
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
                const balance_amount = total_amount - advance_amount;

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
                            balance_amount,
                            pay_amount: advance_amount,
                            payment_count: 0,
                            payment_status: 'Pending'
                        }
                    },
                    callback: function (r) {
                        if (r.message) {
                            frappe.msgprint(__('✅ Payment record created successfully!'));
                            // Trigger Razorpay
                            make_razorpay_payment(r.message.name);
                        }
                    }
                });
            });
        });

        // ======================================
        // 📜 Terms & Conditions
        // ======================================
        const html_content = `
            <div style="max-height:350px; overflow:auto; border:1px solid #ddd; padding:15px; border-radius:8px; background:#fafafa;">
                <h3 style="text-align:center; color:#2c3e50;">Terms & Conditions</h3>
                <p>By booking, you agree to the following terms:</p>
                <ul>
                    <li>Bookings are confirmed only after advance payment.</li>
                    <li>Balance must be cleared before tour start date.</li>
                    <li>Cancellations within 15 days are non-refundable.</li>
                    <li>We are not liable for loss, delays, or damages due to natural causes.</li>
                </ul>
                <p style="color:#e74c3c; text-align:center; margin-top:8px;">
                    <strong>Please read carefully before proceeding.</strong>
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
    }
});

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

// ======================================
// 💳 Razorpay Payment Integration
// ======================================
function make_razorpay_payment(payment_name) {
    frappe.db.get_doc('Payment', payment_name).then(payment => {
        const payAmount = payment.advance_amount;
        const balance = payment.balance_amount;
        const count = payment.payment_count || 0;

        if (payAmount <= 0 || count >= 3) {
            frappe.msgprint('No payment required or max limit reached.');
            return;
        }

        const options = {
            key: 'rzp_test_1DP5mmOlF5G5ag',
            amount: payAmount * 100,
            currency: 'INR',
            name: payment.customer,
            description: `Payment for Booking: ${payment.booking}`,
            handler: function (response) {
                const now = frappe.datetime.now_datetime();
                const newHistory = `
                    <b style="color:green">* Payment ID:</b> ${response.razorpay_payment_id}
                    <br><b style="color:green">Amount:</b> ₹${payAmount}
                    <br><b style="color:green">Date:</b> ${now}
                    <br><br>${payment.payment_history || ''}
                `;

                const newCount = count + 1;
                const newBalance = balance - payAmount;

                frappe.db.set_value('Payment', payment_name, {
                    payment_history: newHistory,
                    balance_amount: newBalance,
                    payment_count: newCount,
                    payment_status: newBalance <= 0 ? 'Completed' : 'Partially Paid',
                    advance_amount: newBalance > 0 ? Math.ceil(newBalance / (3 - newCount)) : 0
                }).then(() => {
                    frappe.msgprint(
                        newBalance <= 0
                            ? '✅ All payments completed!'
                            : `₹${payAmount} paid. Remaining balance: ₹${newBalance}`
                    );
                });
            },
            prefill: {
                name: payment.customer,
                email: payment.email || 'tourist@gmail.com',
                contact: payment.mobile || '9999999999'
            },
            theme: { color: '#3399cc' }
        };

        const rzp = new Razorpay(options);
        rzp.open();
    });
}
