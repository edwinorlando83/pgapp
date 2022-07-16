// Copyright (c) 2022, orlando and contributors
// For license information, please see license.txt

frappe.ui.form.on('sil_parametrosg', {
	// refresh: function(frm) {

	// }

	exportar(frm) {
		frappe.call({
			doc: frm.doc,
			method: "export_tra",			
			callback: r => {      
		         alert(r.message);
			}
		  });
	},
	importar(frm) {
		frappe.call({
			doc: frm.doc,
			method: "import_tra",			
			callback: r => {      
		         alert(r.message);
			}
		  });
	}

});
