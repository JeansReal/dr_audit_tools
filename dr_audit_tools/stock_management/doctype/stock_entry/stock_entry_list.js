frappe.listview_settings['Stock Entry'] = {

	get_indicator: (doc) => [__(doc.status), {
		'Activo': 'green',
		'Anulado': 'red',
	}[doc.status], 'status,=,' + doc.status],

}