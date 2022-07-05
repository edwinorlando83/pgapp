// Copyright (c) 2021, orlando and contributors
// For license information, please see license.txt

frappe.ui.form.on('sil_capa', {
	refresh: function (frm) {

/*
	 	$.ajax({
			method: "GET",
			url: "http://localhost:8080/geoserver/rest/layers.json",
			dataType: "json",
			username: "admin",
			password: "geoserver",
			headers: {
				"Authorization": "Basic " + btoa("admin" + ":" + "geoserver")
			  },
			success: function (data) {
				alert(data);
				console.log(data);
			}
		}); 
		*/

	 	/*frappe.call({
				doc: cur_frm.doc, method: "getCapas", freeze: true,
				callback: (r) => {
				   console.log(r)
				},
			  }); */

	}
});
