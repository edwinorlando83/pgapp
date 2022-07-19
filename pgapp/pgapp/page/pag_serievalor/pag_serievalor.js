let me;
frappe.pages['pag_serievalor'].on_page_load = function (wrapper) {
	me = this;
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Series',
		single_column: true
	});

	page.main.html(frappe.render_template("pag_serievalor", {}));

	var periodo = frappe.ui.form.make_control({
		parent: page.main.find(".entidad"),
		df: {
			fieldtype: "Link",
			options: "sil_periodo",
			fieldname: "Periodo",
			label: "Periodo",
			reqd: 1,
			only_input: true,
			get_query: () => {

			},
			change: function () {
				getIndicadores(periodo.get_value());

			}
		}

	});
	periodo.refresh();

}

function dibujar(datos) {
	console.log(datos);

	let html = `<table  class="ExcelTable2007">
	<tbody>
	  <tr>
	    <th class="heading">&nbsp;</th>
		<th>Indicador</th>
		<th >Provincia</th>
		<th>Cantón</th>
		<th>Parroquia</th>
		<th>Meta</th>
		<th>Valor</th>		 
	  </tr> 
 `;
 let i=1;
	datos.forEach((row) => {
		html += ` 
		  <tr>
		  <td > ${i}</td>
			<td > ${row.ind_nombre}</td>
			<td >${row.ind_nprovincia}</td>
			<td >${row.ind_ncanton}</td>
			<td >${row.ind_nparroquia}</td>
		
			<td > <input  onkeypress="return isNumberKey(this, event);"  onchange=" actulizar_meta(this.value,'${row.name}' )"    value='${row.serval_meta}' > </input>   </td>
			<td >  <input  onkeypress="return isNumberKey(this, event);"  onchange="actulizar_valor(this.value,'${row.name}' )"  value='${row.serval_valor}' > </input>  </td>
			 
		  </tr>
		 `;
		 i++;
	});

	html += ` 
	</tbody>
	</table>`;

	me.page.main.find(".div_datos").html(html);


}

function getIndicadores(inperiod_codigo) {

	frappe.call({
		"method": "pgapp.pgapp.page.pag_serievalor.pag_serievalor.getIndicadores",
		args: {
			period_codigo: inperiod_codigo,

		},
		callback: function (r) {

			dibujar(r.message);

		}
	});
}
function actulizar_meta(inserval_meta, inname) {

	frappe.call({
		"method": "pgapp.pgapp.page.pag_serievalor.pag_serievalor.updateserie_meta",
		args: {
			name: inname,
			serval_meta: inserval_meta,

		},
		callback: function (r) {
			console.log(r.message);
			frappe.show_alert('Se actualizo la información de meta', 1);

		}
	});

}

function actulizar_valor(inserval_valor, inname) {

	frappe.call({
		"method": "pgapp.pgapp.page.pag_serievalor.pag_serievalor.updateserie_valor",
		args: {
			name: inname,
			serval_valor: inserval_valor,

		},
		callback: function (r) {
			console.log(r.message);


			frappe.show_alert('Se actualizo la información de Valor', 1);


		}
	});

}

function isNumberKey(txt, evt) {
	var charCode = (evt.which) ? evt.which : evt.keyCode;
	if (charCode == 46) {
	  //Check if the text already contains the . character
	  if (txt.value.indexOf('.') === -1) {
		return true;
	  } else {
		return false;
	  }
	} else {
	  if (charCode > 31 &&
		(charCode < 48 || charCode > 57))
		return false;
	}
	return true;
  }
