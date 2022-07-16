from __future__ import unicode_literals
import frappe

def generar_sil_serievalor(ind_codigo, tipper_codigo , ind_geof):
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
        else:
            per = frappe.get_doc("sil_periodo", existe)
        
        for dpa in referecnias_geografica(ind_geof):
            ser = frappe.new_doc("sil_serievalor")
            ser.ind_codigo = ind_codigo
            ser.ind_dpa = dpa.dpa
            ser.per_codigo =  periodicidad.per_codigo
            ser.period_codigo = per.period_codigo 
            ser.serval_longitud = dpa.longitud
            ser.serval_latitud = dpa.latitud   
            ser.insert()

def referecnias_geografica(ind_geof):

    provincia = frappe.db.get_single_value('sil_parametrosg', 'dpa_provincia')
    if not provincia:
        frappe.throw("No se ha definido la provincia , por favor defina la provincia en el formulario de parámetros")

    if ind_geof == "PROVINCIAL":
        return getProvincia(provincia)

    if ind_geof == "CANTONAL":
        return getCantones(provincia)
    
    if ind_geof == "PARROQUIAL":
        return getParroquias(provincia)
    

def getCantones(provincia):
    sql = """ select DISTINCT dpa_canton  as dpa from  tabsil_dpa td   where dpa_provincia = '{0}' """.format(provincia)
    cantones = frappe.db.sql (sql, as_dict=1)
    for rw in cantones:
        cent = getcentroide(rw.dpa)
        rw["longitud"] = cent.cent_lon
        rw["latitud"] = cent.cent_lat
    return cantones

def getParroquias(provincia):
    sql = """ select   dpa_parroquia   as dpa 
     from  tabsil_dpa  where dpa_provincia = '{0}'
     order by dpa_ncanton,dpa_nparroquia """.format(provincia)
    cantones = frappe.db.sql (sql, as_dict=1)
    for rw in cantones:
        cent = getcentroide(rw.dpa)
        rw["longitud"] = cent.cent_lon
        rw["latitud"] = cent.cent_lat
    return cantones

def getProvincia(provincia):
    sql = """ select DISTINCT dpa_provincia as dpa   from  tabsil_dpa  where dpa_provincia = '{0}' """.format(provincia)
    cantones = frappe.db.sql (sql, as_dict=1)
    for rw in cantones:
        cent = getcentroide(rw.dpa)
        rw["longitud"] = cent.cent_lon
        rw["latitud"] = cent.cent_lat
    return cantones

def getcentroide(pda):
    sql = """ select  cent_lat , cent_lon  from tabsil_centroide   where cent_pda = '{0}' """.format(pda)
    cantones = frappe.db.sql (sql, as_dict=1)
    return cantones[0]  

 
    


 