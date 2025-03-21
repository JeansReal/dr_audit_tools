frappe.ui.form.on("Stock Entry", {
	setup(frm) {
		frm.page.sidebar.toggle(false);
	}
});

frappe.ui.form.on("Stock Entry Detail", {
	qty(frm, cdt, cdn) {
		let row = locals[cdt][cdn];

		if (row.merma & row.merma > 0) {
			row.qty_total = row.qty - row.merma;
		} else {
			row.qty_total = row.qty;
		}

		frm.refresh_field('details');
	},

	merma(frm, cdt, cdn) {
		let row = locals[cdt][cdn];

		row.qty_total = row.qty - row.merma;

		frm.refresh_field('details');
	}
});
