from __future__ import unicode_literals
import frappe

def generar_sil_serievalor(ind_codigo ,anio):    
    indicador = frappe.get_doc("sil_indicador",ind_codigo)
    lstperiod= frappe.get_list("sil_periodo", filters={"tipper_codigo": indicador.tipper_codigo , "eje_codigo":anio},   fields=['name' ])
    contador=0
    for silper in lstperiod:         
        for dpa in referecnias_geografica(indicador.rep_codigo):
            if indicador.rep_codigo == "01":
                dpa_codigo = dpa.dpa_provincia
            if indicador.rep_codigo == "02":
                dpa_codigo = dpa.dpa_canton
            if indicador.rep_codigo == "03":
                dpa_codigo = dpa.dpa_parroquia
                    
            existe = frappe.db.exists("sil_serievalor", {"ind_codigo":ind_codigo , "period_codigo":silper.name , "ind_dpa": dpa_codigo})
            if not existe:
                ser = frappe.new_doc("sil_serievalor")
                ser.ind_codigo = ind_codigo            
                ser.period_codigo =  silper.name          
                ser.serval_longitud = dpa.longitud
                ser.serval_latitud = dpa.latitud   
                
                if indicador.rep_codigo == "01":                
                    ser.ind_nprovincia = dpa.dpa_nprovincia
                    ser.ind_dpa = dpa.dpa_provincia 
            
                if indicador.rep_codigo == "02":                
                    ser.ind_nprovincia = dpa.dpa_nprovincia
                    ser.ind_ncanton = dpa.dpa_ncanton
                    ser.ind_dpa = dpa.dpa_canton

                if indicador.rep_codigo == "03":                
                    ser.ind_nprovincia = dpa.dpa_nprovincia
                    ser.ind_ncanton = dpa.dpa_ncanton		
                    ser.ind_nparroquia = dpa.dpa_nparroquia
                    ser.ind_dpa = dpa.dpa_parroquia	

                ser.insert()
                frappe.db.commit()
                contador+=1
    if contador > 0:
       
        return "Se ha generado {2} registros para el indicador {0} para el año {1}".format(ind_codigo,anio,contador)
    else:
        return "Ya se ha generado registros para el indicador {0} el año {1}".format(ind_codigo,anio)
            

def referecnias_geografica(ind_geof):
    
    provincia = frappe.db.get_single_value('sil_parametrosg', 'dpa_provincia')
    if not provincia:
        frappe.throw("No se ha definido la provincia , por favor defina la provincia en el formulario de parámetros")

    if ind_geof == "01":
        return getProvincia(provincia)

    if ind_geof == "02":
        return getCantones(provincia)
    
    if ind_geof == "03":
        return getParroquias(provincia)
    

def getCantones(provincia):
    sql = """select DISTINCT dpa_ncanton , dpa_canton ,dpa_nprovincia,dpa_provincia  
    from  tabsil_dpa  where dpa_provincia ='{0}' """.format(provincia)
    cantones = frappe.db.sql (sql, as_dict=1)

    for rw in cantones:
        cent = getcentroide(rw.dpa_canton)
        rw["longitud"] = cent.cent_lon
        rw["latitud"] = cent.cent_lat
    return cantones

def getParroquias(provincia):
    sql = """select DISTINCT dpa_ncanton , dpa_canton ,dpa_nprovincia,dpa_provincia, dpa_parroquia , dpa_nparroquia
		from  tabsil_dpa  where dpa_provincia ='{0}'  """.format(provincia)
    parroquias = frappe.db.sql (sql, as_dict=1)
    for rw in parroquias:
        cent = getcentroide(rw.dpa_parroquia)
        rw["longitud"] = cent.cent_lon
        rw["latitud"] = cent.cent_lat
    return parroquias

def getProvincia(provincia):
    sql = """select DISTINCT dpa_nprovincia,dpa_provincia from  tabsil_dpa  where dpa_provincia ='{0}' """.format(provincia)
    provincias = frappe.db.sql (sql, as_dict=1)
    for rw in provincias:
        cent = getcentroide(rw.dpa_provincia)
        rw["longitud"] = cent.cent_lon
        rw["latitud"] = cent.cent_lat
    return provincias

def getcentroide(pda):
    sql = """ select  cent_lat , cent_lon  from tabsil_centroide   where cent_pda = '{0}' """.format(pda)
    cantones = frappe.db.sql (sql, as_dict=1)
    return cantones[0]  

 
    


 