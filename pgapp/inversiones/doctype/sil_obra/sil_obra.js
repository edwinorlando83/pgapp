// Copyright (c) 2021, orlando and contributors
// For license information, please see license.txt

frappe.ui.form.on('sil_obra', {
	refresh: function(frm) {
		esAniveldeCanton();
	},
	cantones(frm) {
		get_parroquias(frm.doc.cantones, frm);
	},
	onload: function (frm) {
		get_cantones(frm);
		if (frm.doc.cantones) get_parroquias(frm.doc.cantones, frm);
	}
});

function get_cantones( frm) {
	frappe.call({
		doc: cur_frm.doc,
		method: "getCantones",	
		callback: (r) => { 
 
			frm.set_df_property("cantones", "options",r.message);
			frm.refresh_field("cantones");
		},
	});
}

function get_parroquias( incanton, frm) {
	frappe.call({
		doc: cur_frm.doc,
		method: "getParroquias",
		args: { canton: incanton },
		callback: (r) => {
			frm.set_df_property("parroquia", "options", r.message);
			frm.refresh_field("parroquia");
		},
	});
}

function esAniveldeCanton(){

	//leer el codigo dpa_canton 

	frappe.db.get_single_value('parametros', 'dpa_canton').then(val => {
		
		if (val!=undefined){

			cur_frm.set_df_property('cantones', 'read_only', true);
		}
		
		
	});
}