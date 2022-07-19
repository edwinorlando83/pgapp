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

function dibujar(datos){
	console.log(datos);

	let html =`<table border=1 class="table1">
	<tbody>
	  <tr>
		<td>1</td>
		<td ></td>
		<td ></td>
		<td ></td>
		<td ></td>
		<td ></td>
		<td ></td>
	  </tr>
 
 `;
 
 
	datos.forEach((row) => {
		html +=` 
		  <tr>
			<td > ${row.ind_nombre}</td>
			<td >${row.ind_nprovincia}</td>
			<td >${row.ind_ncanton}</td>
			<td >${row.ind_nparroquia}</td>
		
			<td > <input onchange="myFunction(this.value,'${row.name}' )"    value='${row.serval_meta}' > </input>   </td>
			<td >  <input value='${row.serval_valor}' > </input>  </td>
			<td > </td>
		  </tr>
		 `; 
    });

	html +=` 
	</tbody>
	</table>`;

	me.page.main.find(".div_datos").html( html);


}

function getIndicadores(inperiod_codigo){

	frappe.call({
        "method": "pgapp.pgapp.page.pag_serievalor.pag_serievalor.getIndicadores",
        args: {
            period_codigo: inperiod_codigo,
          
        },
        callback: function(r) {

			dibujar(r.message);

        }
    });
}
function myFunction(data ,name){
alert(name)
}