frappe.ui.form.on('Booking', {
    refresh(frm) {
        // Create a custom green button with hover effect & right alignment
        frm.fields_dict.make_payment.$wrapper.html(`
            <div style="text-align: right; margin-top: 10px;">
                <button id="go_to_payment" 
                    class="btn btn-success custom-payment-btn">
                    💳 Make Payment
                </button>
            </div>

            <style>
                .custom-payment-btn {
                    background-color: #28a745 !important;  /* Green */
                    color: white !important;
                    border: none;
                    border-radius: 6px;
                    padding: 8px 18px;
                    font-weight: 600;
                    font-size: 14px;
                    transition: all 0.3s ease-in-out;
                }
                .custom-payment-btn:hover {
                    background-color: #218838 !important; /* Darker green */
                    transform: scale(1.05);
                    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                }
            </style>
        `);

        // Bind button click
        frm.fields_dict.make_payment.$wrapper.find('#go_to_payment').on('click', function () {
            if (!frm.doc.customer) {
                frappe.msgprint(__('Please select a Customer first.'));
                return;
            }

            // Redirect to Payment form & prefill fields
            frappe.new_doc('Payment', {
                customer: frm.doc.customer,
                booking: frm.doc.name
            });
        });


        if (frappe.session.user !== "Administrator") {
            // Disable adding, editing, and deleting rows in the child table
            frm.fields_dict.images.grid.wrapper.find('.grid-add-row, .grid-remove-rows').hide();
            frm.fields_dict.images.grid.cannot_add_rows = true;
            frm.fields_dict.images.grid.only_sortable = true;

            frm.fields_dict.images.grid.wrapper.find('.grid-row').each(function () {
                $(this).find('.grid-delete-row, .grid-row-check').hide();
            });
        }
    },
    visa_type: function (frm) {
        let visa_fees = {
            "Tourist Visa": 5000,
            "Business Visa": 7500,
            "Student Visa": 10000,
            "Work Visa": 15000,
            "Medical Visa": 8000,
            "Transit Visa": 2000,
            "Diplomatic Visa": 0
        };

        if (frm.doc.visa_type) {
            frm.set_value("visa_fee", visa_fees[frm.doc.visa_type] || 0);
        } else {
            frm.set_value("visa_fee", 0);
        }
    }
});
