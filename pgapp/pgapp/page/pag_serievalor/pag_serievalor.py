import frappe

@frappe.whitelist()
def getIndicadores(period_codigo):
    sql =""" SELECT period_codigo , ind_nombre , ind_nprovincia, ind_ncanton , ind_nparroquia ,
         serval_meta , serval_valor , name
        from tabsil_serievalor 
        order by  period_codigo,ind_nombre,ind_nprovincia, ind_ncanton , ind_nparroquia  """.format(period_codigo)
    return frappe.db.sql(sql, as_dict=1)
