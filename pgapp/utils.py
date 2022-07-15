from __future__ import unicode_literals
import frappe

def generar_sil_periodo(tipper_codigo, anio):
    lstperiod= frappe.get_list("sil_periodicidad", filters={"tipper_codigo": tipper_codigo},   fields=['per_ennumero'])
    for period in lstperiod:
        existe = frappe.db.exists("sil_periodo", {"period_anio": anio, "period_mes": period.per_ennumero})
        if not existe:
            per = frappe.new_doc("sil_periodo")
            per.period_anio = anio
            per.period_mes = period.per_ennumero
            per.tipper_codigo = tipper_codigo    
            per.insert()

def generar_sil_serievalor(ind_codigo, tipper_codigo ):
    anio = frappe.db.get_single_value('sil_parametrosg', 'par_anio')
    if not anio:
        frappe.throw("No se ha definido el año , por favor defina el año en el formulario de  parámetros")

    
    lstperiod= frappe.get_list("sil_periodicidad", filters={"tipper_codigo": tipper_codigo},   fields=['per_codigo','per_ennumero'])
    for periodicidad in lstperiod:
        existe = frappe.db.exists("sil_periodo", {"period_anio": anio, "period_mes": periodicidad.per_ennumero})
        if not existe:
            per = frappe.new_doc("sil_periodo")
            per.period_anio = anio
            per.period_mes = periodicidad.per_ennumero
            per.tipper_codigo = tipper_codigo    
            per.insert()

            ser = frappe.new_doc("sil_serievalor")
            ser.ind_codigo = ind_codigo
            ser.per_codigo =  periodicidad.per_codigo
            ser.period_codigo = per.period_codigo    
            ser.insert()


 
    


 