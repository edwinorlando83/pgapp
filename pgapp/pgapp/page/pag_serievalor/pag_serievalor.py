import frappe

@frappe.whitelist()
def getIndicadores(period_codigo):
    sql =""" SELECT period_codigo , ind_nombre , ind_nprovincia, ind_ncanton , ind_nparroquia ,
         serval_meta , serval_valor , name
        from tabsil_serievalor   where period_codigo='{0}' 
        order by  period_codigo,ind_nombre,ind_nprovincia, ind_ncanton , ind_nparroquia """.format(period_codigo)
    return frappe.db.sql(sql, as_dict=1)

@frappe.whitelist()
def updateserie_meta(name,serval_meta ):
    obj = frappe.get_doc("sil_serievalor", name)
    obj.serval_meta = serval_meta 
    return obj.save()

@frappe.whitelist()
def updateserie_valor(name,serval_valor):
    obj = frappe.get_doc("sil_serievalor", name)
    obj.serval_valor = serval_valor 
    return obj.save()

