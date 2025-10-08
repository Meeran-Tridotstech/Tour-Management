frappe.listview_settings['Customer'] = {
    onload: function(listview) {
        console.log('customer_list onload');
        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Customer",
                filters: { owner: frappe.session.user },
                limit: 1,
                fields: ["name"]
            },
            callback: function(r) {
                if (r.message && r.message.length) {
                    // remove default primary action (New)
                    try { listview.page.clear_primary_action(); } catch(e){}

                    // extra safety: hide any visible New buttons in DOM
                    listview.page.wrapper.find(".page-actions .btn.btn-primary").hide();
                    listview.page.wrapper.find(".page-actions .btn").each(function() {
                        if ($(this).text().trim() === "New") $(this).hide();
                    });
                }
            }
        });
    }
};
