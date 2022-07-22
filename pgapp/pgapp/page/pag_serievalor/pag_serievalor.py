import frappe

@frappe.whitelist()
def getIndicadores(ind_codigo,eje_codigo):
    sql =""" SELECT s.period_codigo , s.ind_codigo , ind_nombre , ind_nprovincia, ifnull(ind_ncanton,'') ind_ncanton ,  ifnull(ind_nparroquia,'') ind_nparroquia ,
         serval_meta , serval_valor , s.name , per.tipper_codigo 
        from tabsil_serievalor s  inner join tabsil_periodo per 
        on (per.name = s.period_codigo)
        INNER  join tabsil_ejercicio e on ( e.name = per.eje_codigo)
         where s.ind_codigo  ='{0}' and   per.eje_codigo = '{1}'
        order by  period_codigo,ind_nombre,ind_nprovincia, ind_ncanton , ind_nparroquia """.format(ind_codigo,eje_codigo)
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

