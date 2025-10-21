// Copyright (c) 2025, GoFly Journeys and contributors
// For license information, please see license.txt

frappe.ui.form.on("Tour Staff Assignment", {
	refresh(frm) {
        gofly.common.add_open_related_button(frm);

		frm.set_query('guide_id', function() {
            if (!frm.doc.booking) return;
            return {
                query: 'gofly_journeys.gofly_journeys.doctype.booking.booking.get_guide_query',
                filters: { docname: frm.doc.booking }
            };
        });
	}
});