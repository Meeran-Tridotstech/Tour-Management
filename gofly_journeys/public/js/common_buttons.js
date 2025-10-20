frappe.provide("gofly.common");

gofly.common.add_open_related_button = function (frm) {
    // Prevent duplicate buttons
    frm.page.clear_custom_actions();

    // Dropdown options
    frm.page.add_inner_button('Customer', () => {
        frappe.set_route('List', 'Customer');
    }, 'Open Related');

    frm.page.add_inner_button('Tour Package', () => {
        
        frappe.set_route('List', 'Tour Package');
    }, 'Open Related');

    frm.page.add_inner_button('Booking', () => {
        frappe.set_route('List', 'Booking');
    }, 'Open Related');

    frm.page.add_inner_button('Payment', () => {
        frappe.set_route('List', 'Payment');
    }, 'Open Related');

    frm.page.add_inner_button('Tour Staff Assignment', () => {
        frappe.set_route('List', 'Tour Staff Assignment');
    }, 'Open Related');
};
