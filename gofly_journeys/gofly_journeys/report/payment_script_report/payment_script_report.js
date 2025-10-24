frappe.query_reports["Payment Script Report"] = {
    "filters": [
        {"fieldname": "customer", "label": __("Customer"), "fieldtype": "Link", "options": "Customer"},
        {"fieldname": "booking", "label": __("Booking"), "fieldtype": "Link", "options": "Booking"},
        {"fieldname": "payment_status", "label": __("Payment Status"), "fieldtype": "Select", "options": "\nPaid\nPartial\nUnpaid"}
    ],

    "after_datatable_render": function(report, datatable) {
        if(!report.data || report.data.length == 0) return;

        // Aggregate payments per customer
        let totals = {};
        report.data.forEach(d => {
            let customer = d.customer || "Unknown";
            totals[customer] = (totals[customer] || 0) + d.amount;
        });

        let labels = Object.keys(totals);
        let values = Object.values(totals);

        const chart_data = {
            data: {
                labels: labels,
                datasets: [{name: "Total Payment Amount", values: values}]
            },
            type: 'bar', // Bar chart
            height: 300
        };

        // Create or replace chart div
        let chart_div = document.querySelector('#report-chart');
        if(!chart_div) {
            chart_div = frappe.dom.set_child(frappe.query_report.wrapper, 'div', {'id':'report-chart'});
        } else {
            chart_div.innerHTML = '';
        }

        frappe.query_reports["Payment Script Report"].chart = new frappe.Chart(chart_div, chart_data);
    }
};



