frappe.listview_settings['Customer'] = {
    onload: function (listview) {

        // 🔹 Function to check and hide "Add Customer" button
        function hide_add_button_if_needed() {
            frappe.call({
                method: "frappe.client.get_list",
                args: {
                    doctype: "Customer",
                    filters: { owner: frappe.session.user },
                    limit: 1,
                    fields: ["name"]
                },
                callback: function (r) {
                    if (r.message && r.message.length) {
                        // Hide "New" button (main + fallback)
                        try { listview.page.clear_primary_action(); } catch (e) { }
                        listview.page.wrapper.find(".page-actions .btn.btn-primary").hide();
                        listview.page.wrapper.find(".page-actions .btn").each(function () {
                            if ($(this).text().trim() === "New") $(this).hide();
                        });

                        // Optional: show message once
                        console.log("Customer already exists for this user. 'Add Customer' hidden.");
                    }
                }
            });
        }

        // 🔹 Run when list first loads
        hide_add_button_if_needed();

        // 🔹 Auto-refresh after Customer creation (real-time)
        frappe.realtime.on("doc_update", function (data) {
            if (data.doctype === "Customer") {
                listview.refresh();
                setTimeout(() => hide_add_button_if_needed(), 500);
            }
        });

        // 🔹 Also check when user navigates back to Customer list
        frappe.router.on('change', function () {
            const route = frappe.get_route();
            if (route && route[0] === "List" && route[1] === "Customer") {
                setTimeout(() => hide_add_button_if_needed(), 500);
            }
        });

        // 🔹 Fallback refresh after saving a record manually
        frappe.ui.form.on('Customer', {
            after_save: function (frm) {
                if (frm.is_new()) {
                    frappe.set_route("List", "Customer");
                    setTimeout(() => hide_add_button_if_needed(), 800);
                }
            }
        });
    }
};
