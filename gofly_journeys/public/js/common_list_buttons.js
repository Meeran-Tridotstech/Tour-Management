frappe.provide("gofly.common");

frappe.listview_settings["*"] = {
    onload(listview) {
        // Avoid adding multiple times
        if (listview.$page.find('.common-navigate-btn').length) return;

        // Create dropdown group
        const $btnGroup = $(`
            <div class="btn-group common-navigate-btn">
                <button class="btn btn-primary btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                    <i class="fa fa-compass"></i> Navigate
                </button>
                <ul class="dropdown-menu" style="min-width: 180px;">
                    <li><a class="dropdown-item" href="#List/Customer">Customer</a></li>
                    <li><a class="dropdown-item" href="#List/Tour Package">Tour Package</a></li>
                    <li><a class="dropdown-item" href="#List/Booking">Booking</a></li>
                    <li><a class="dropdown-item" href="#List/Payment">Payment</a></li>
                    <li><a class="dropdown-item" href="#List/Tour Staff Assignment">Tour Staff Assignment</a></li>
                </ul>
            </div>
        `);

        // Append to toolbar
        listview.page.add_inner_button_group($btnGroup);

        // Optional: add slight styling
        $btnGroup.find('button').css({
            'font-family': 'Poppins, sans-serif',
            'font-size': '13px',
            'border-radius': '6px',
            'background-color': '#1a237e',
            'color': '#fff'
        });
    }
};
