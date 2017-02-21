// Copyright (c) 2016, Hasan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Templete Article', {
	purchase_price:function(frm) {
		frm.set_value('discount', parseFloat(frm.doc.n_price) - parseFloat(frm.doc.purchase_price))
	},
	n_price:function(frm) {
		frm.set_value('discount', parseFloat(frm.doc.n_price) - parseFloat(frm.doc.purchase_price))
	}
});
