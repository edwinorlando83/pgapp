 


frappe.listview_settings['sil_periodicidad'] = {     
    hide_name_column: true,  
    onload(listview) {
       
           const handler = listview.filter_area.filter_list.on_change.bind(listview.filter_area.filter_list);
           listview.filter_area.filter_list.on_change = () => {
               handler();
          },
            listview.page.add_inner_button(__("Generar Periodicidad"), function () {
                frappe.call({
                    method: 'asimed.entidades.doctype.entidades.entidades.sincronizarSIA',
                    freeze: true,
                    freeze_message: "Verificando...",
                    callback: function(r) {
                        console.log(r);
                    }
                });
           }, __('Acciones'));
            
       
    } 
    
}