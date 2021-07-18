// Copyright (c) 2021, orlando and contributors
// For license information, please see license.txt

frappe.ui.form.on('sil_ingreso_ind', {
	refresh: function (frm) {
		cur_frm.fields_dict["sil_ingreso_ind_cant"].grid.wrapper.find('.grid-add-row').hide();
	},

	representacion(frm) {

		cur_frm.clear_table("sil_ingreso_ind_cant");

		if (frm.doc.representacion == 'PROVINCIAL') {


			frappe.call({
				doc: cur_frm.doc, 
				method: "getProvincia", 
				freeze: true,
				callback: (r) => {
					console.log(r.message)
					frm.add_child('sil_ingreso_ind_cant', { provincia: r.message.dpa_nprovincia, metodologia: '', observacion: '' });
					frm.refresh_field('sil_ingreso_ind_cant');
				},
			});
		}

		if (frm.doc.representacion == 'CANTONAL') {


			frappe.call({
				doc: cur_frm.doc,
				method: "getCantones",
				freeze: true,
				callback: (r) => {
					console.log(r.message);
					$.each(r.message, function (i, row) {
						frm.add_child('sil_ingreso_ind_cant', { provincia: row.dpa_nprovincia, canton: row.dpa_ncanton, metodologia: '', observacion: '' });
					});


					frm.refresh_field('sil_ingreso_ind_cant');
				},
			});
		}

		if (frm.doc.representacion == 'PARROQUIAL') {

			frappe.call({
				doc: cur_frm.doc, method: "getParroquia", freeze: true,
				callback: (r) => {
					console.log(r.message);
					$.each(r.message, function (i, row) {
						frm.add_child('sil_ingreso_ind_cant', { provincia: row.dpa_nprovincia, canton: row.dpa_ncanton, parroquias: row.dpa_nparroquia, metodologia: '', observacion: '' });
					});


					frm.refresh_field('sil_ingreso_ind_cant');
				},
			});
		}



	}
});
