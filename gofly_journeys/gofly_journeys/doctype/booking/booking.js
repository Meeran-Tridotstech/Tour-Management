// Copyright (c) 2025, GoFly Journeys and contributors
// For license information, please see license.txt

frappe.ui.form.on("Booking", {
    after_save(frm) {
        frappe.call({
            method: "frappe.client.insert",
            args: {
                doc: {
                    doctype: "Payment",
                    booking: frm.doc.name,          // link booking to payment
                    title: "Payment for " + frm.doc.name // set document name/title
                }
            },
            callback: function(r) {
                if (!r.exc) {
                    frappe.set_route("Form", "Payment", r.message.name);
                }
            }
        });
    },
});


// frappe.ui.form.on("Booking", {
//     after_save(frm) {
//         frm.add_custom_button("Pay_Now",()=>{
//      frappe.call({
//             method: "frappe.client.insert",
//             args: {
//                 doc: {
//                     doctype: "Payment Page",
//                     booking: frm.doc.name  // link booking to payment
//                 }
//             },
//             callback: function(r) {
//                 if (!r.exc) {
//                     frappe.set_route("Form", "Payment Page", r.message.name);
//                 }
//             }
//         });
//         })
   
//     },
// });