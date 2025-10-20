// Copyright (c) 2025, GoFly Journeys and contributors
// For license information, please see license.txt

frappe.ui.form.on("Tour Staff Assignment", {
	refresh(frm) {
        gofly.common.add_open_related_button(frm);

	}
});