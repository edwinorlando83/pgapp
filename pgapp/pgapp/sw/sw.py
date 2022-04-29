import frappe
import psycopg2


@frappe.whitelist(allow_guest = True)
def getdatos():
    lst = frappe.db.get_list('sil_obra',fields='*')
    return lst

@frappe.whitelist(allow_guest = True)
def getCapas():
    sql = """select cap_desc, c.name,  t.cap_origen, t.cap_escala, t.cap_fechaact,
    c.is_group , c.parent_grupo_capas,c.nivel  ,t.name as capa , c.nombre,t.nombre as capanombre ,inicio_marcado, s.url ,s.wmsurl 
        from tabgrupo_capas c  inner join  tabcapas t on ( t.grupo_capas = c.name)
        inner join tabservidores_mapa s on ( t.servidores_mapa= s.name)
        where c.deshabilitado =0 and t.deshabilitado =0"""
    lst = frappe.db.sql(sql,as_dict=True)
    return lst


@frappe.whitelist(allow_guest = True)
def getIndicadores():
    sql = """ select  i.name, ind_nombre ,sil_grupoindicador , g.gruind_descripcion  from  tabsil_indicador i 
				     inner join tabsil_grupoindicador g on (i.sil_grupoindicador= g.name)"""
    lst = frappe.db.sql(sql,as_dict=True)
    return lst

@frappe.whitelist(allow_guest = True)
def getObras():
    sql = """ select tipo.name  tipo , o.name, obr_nombre,   concat((select  value from  tabSingles    where doctype = 'parametros' and  field  = 'url'), tipobr_icono ) as tipobr_icono 		
				,o.obr_latitud , o.obr_longitud
                from tabsil_obra o inner join tabsil_tipoobra tipo on (  tipo.name = o.sil_tipoobra  ) order by tipo.name"""
    lst = frappe.db.sql(sql,as_dict=True)
    return lst

@frappe.whitelist(allow_guest = True)
def getObrasporgrupo(grupo):
    sql = """ select   o.name, obr_nombre,   concat((select  value from  tabSingles    where doctype = 'parametros' and  field  = 'url'), tipobr_icono ) as tipobr_icono 		
				,o.obr_latitud , o.obr_longitud
				, concat((select  value from  tabSingles    where doctype = 'parametros' and  field  = 'url'), o.logo ) logo 
                from tabsil_obra o inner join tabsil_tipoobra tipo on (  tipo.name = o.sil_tipoobra  )
                where o.sil_tipoobra  = '{0}'""".format(grupo)
    lst = frappe.db.sql(sql,as_dict=True)
    return lst

 
@frappe.whitelist(allow_guest = True)
def getAdjuntos(name_obra):
    sql = """ select sil_tipoadjunto  ,concat((select  value from  tabSingles    where doctype = 'parametros' and  field  = 'url'), adjobr_archivo )  adjobr_archivo
        , o.adjobr_video 
        from tabsil_adjuntoobra o where parent ='{0}' """.format(name_obra)
    lst = frappe.db.sql(sql,as_dict=True)
    return lst  

@frappe.whitelist(allow_guest = True)
def getinfoobra(name_obra):
    sql = """ select * 
     ,concat((select  value from  tabSingles    where doctype = 'parametros' and  field  = 'url'), logo )  as fulllogo
     from tabsil_obra     where name=    '{0}' """.format(name_obra)
    lst = frappe.db.sql(sql,as_dict=True)[0]
    return lst  


@frappe.whitelist(allow_guest = True)
def getPeridosIndicador(sil_ingreso_ind):
    sql = """     select DISTINCT  sil_periodo , p.period_anio  , p.period_mes  from tabsil_serievalor sv  inner join 
    tabsil_periodo  p on (sv.sil_periodo= p.name) 
    where sv.sil_ingreso_ind  =    '{0}' """.format(sil_ingreso_ind)
    lst = frappe.db.sql(sql,as_dict=True)
    return lst  

@frappe.whitelist(allow_guest = True)
def getSeriesIndicador(sil_ingreso_ind):
    sql = """     
    SELECT   vs.parent, sil_periodo, s.sil_periodicidad  ,s.ind_geof,
    vs.provincia , vs.canton , vs.parroquias ,vs.valor ,
    i.ind_nombre , i.ind_definicion 
    FROM tabsil_ing_valorserie vs
    inner join tabsil_serievalor s on( s.name= vs.parent)
    inner join  tabsil_indicador  i on(i.name= s.sil_ingreso_ind) 
    where   i.name =    '{0}'  order by  vs.canton ,  vs.parroquias  """.format(sil_ingreso_ind)
    lst = frappe.db.sql(sql,as_dict=True)
    return lst  

@frappe.whitelist(allow_guest = True)
def getCantones():
    sql = """     
    SELECT DISTINCT dpa_ncanton    from tabsil_dpa td  where dpa_provincia = (select  value from  tabSingles    where doctype = 'parametros' and field ='dpa_provincia')
    order by 1  """ 
    lst = frappe.db.sql(sql,as_dict=True)
    return lst  

@frappe.whitelist(allow_guest = True)
def getParroquia(ncanton):
    sql = """     
    SELECT   dpa_nparroquia 
    from tabsil_dpa td  
    where dpa_provincia = (select  value from  tabSingles    where doctype = 'parametros' and field ='dpa_provincia')
    and dpa_ncanton ='{0}'
    order by 1   """.format(ncanton)
    lst = frappe.db.sql(sql,as_dict=True)
    return lst  

@frappe.whitelist(allow_guest = True)
def getInfoCapa(name_capa):
    sql = """     
     select t.name, m.url , m.espacio_trabajo  , cap_origen ,cap_escala ,cap_fechaact , cap_desc  from tabcapas t 
 inner join tabservidores_mapa m on (t.servidores_mapa = m.name)  
 where t.name = '{0}'   """.format(name_capa)
    lst = frappe.db.sql(sql,as_dict=True)[0]
    return lst  

@frappe.whitelist(allow_guest = True)
def getTipoObras():
    sql = "select  tipobr_desc, tipobr_icono,name  from tabsil_tipoobra"
    lst = frappe.db.sql(sql,as_dict=True) 
    return lst  

@frappe.whitelist(allow_guest = True)
def coneccionpg():
    conn = psycopg2.connect( database="sildb", user="postgres", password="frappe"  )
    cursor1=conn.cursor()
    sql="SELECT gid, objectid, area, perimeter, lim2fc_, lim2fc_id, elev, id, shape_leng, shape_area FROM capas.batimetria;"
    cursor1.execute(sql)
    db_version = cursor1.fetchall() #fetchone()
    cursor1.close()
    return db_version
@frappe.whitelist( )
def getVentaEmergente():
    sql = """  select name,tipo,html,url,REPLACE (texto,'src="/','src="http://62.171.170.162:8081/') as texto from tabventana_emergente te where CURRENT_DATE BETWEEN te.fecha_inicio and te.fecha_fin   """
    lst = frappe.db.sql(sql,as_dict=True)
    return lst


 

