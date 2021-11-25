// Copyright (c) 2021, orlando and contributors
// For license information, please see license.txt

frappe.ui.form.on('sil_serievalor', {
	 refresh: function(frm) {
		cur_frm.fields_dict["sil_ing_valorserie"].grid.wrapper.find('.grid-add-row').hide();
	  },
	  sil_ingreso_ind: function(frm) {

		cur_frm.clear_table("sil_ing_valorserie");

		if (frm.doc.ind_geof == 'PROVINCIAL') {


			frappe.call({
				doc: frm.doc, 
				method: "getProvincia", 
				freeze: true,
				callback: (r) => {
					console.log(r.message)
					frm.add_child('sil_ing_valorserie', { provincia: r.message.dpa_nprovincia, metodologia: '', observacion: '' });
					frm.refresh_field('sil_ing_valorserie');
				},
			});
		}

		if (frm.doc.ind_geof == 'CANTONAL') {


			frappe.call({
				doc: cur_frm.doc,
				method: "getCantones",
				freeze: true,
				callback: (r) => {
					console.log(r.message);
					$.each(r.message, function (i, row) {
						frm.add_child('sil_ing_valorserie', { provincia: row.dpa_nprovincia, canton: row.dpa_ncanton, metodologia: '', observacion: '' });
					});


					frm.refresh_field('sil_ing_valorserie');
				},
			});
		}

		if (frm.doc.ind_geof == 'PARROQUIAL') {

			frappe.call({
				doc: cur_frm.doc, method: "getParroquia", freeze: true,
				callback: (r) => {
					console.log(r.message);
					$.each(r.message, function (i, row) {
						frm.add_child('sil_ing_valorserie', { provincia: row.dpa_nprovincia, canton: row.dpa_ncanton, parroquias: row.dpa_nparroquia, metodologia: '', observacion: '' });
					});


					frm.refresh_field('sil_ing_valorserie');
				},
			});
		}

	}
});
