import frappe,os
import json 
import csv

def after_install ():
    config_app()

#def boot_session():
#    frappe.defaults.set_user_default("unidad", "U")

def config_app():
    frappe.db.set_value('System Settings', None, 'allow_login_using_user_name', 1)
    frappe.db.set_value('Website Settings', None, 'app_name', 'Sil')
    frappe.db.set_value('Website Settings', None, 'disable_signup', 1)
   
    
    tipper = frappe.new_doc("sil_tipoperiodicidad")
    tipper.tipper_codigo = "AN"
    tipper.tipper_descripcion = "ANUAL"
    tipper.insert()

    tipper = frappe.new_doc("sil_tipoperiodicidad")
    tipper.tipper_codigo = "SE"
    tipper.tipper_descripcion = "SEMESTRAL"
    tipper.insert()

    tipper = frappe.new_doc("sil_tipoperiodicidad")
    tipper.tipper_codigo = "TR"
    tipper.tipper_descripcion = "TRIMESTRAL"
    tipper.insert()

    tipper = frappe.new_doc("sil_tipoperiodicidad")
    tipper.tipper_codigo = "ME"
    tipper.tipper_descripcion = "MENSUAL"
    tipper.insert()
    # PERIODICIDAD
    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "01"
    per.per_nombre = "Año"  
    per.per_ennumero = 12
    per.tipper_codigo = "AN"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "02"
    per.per_nombre = "Enero"  
    per.per_ennumero = 1
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "03"
    per.per_nombre = "Febrero"  
    per.per_ennumero = 2
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "04"
    per.per_nombre = "Marzo"  
    per.per_ennumero = 3
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "05"
    per.per_nombre = "Abril"  
    per.per_ennumero = 4
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "06"
    per.per_nombre = "Mayo"  
    per.per_ennumero = 5
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "07"
    per.per_nombre = "Junio"  
    per.per_ennumero = 6
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "08"
    per.per_nombre = "Julio"  
    per.per_ennumero = 7
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "09"
    per.per_nombre = "Agosto"  
    per.per_ennumero = 8
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "10"
    per.per_nombre = "Septiembre"
    per.per_ennumero = 9
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "11"
    per.per_nombre = "Octubre"  
    per.per_ennumero = 10
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "12"
    per.per_nombre = "Noviembre"  
    per.per_ennumero = 11
    per.tipper_codigo = "ME"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "13"
    per.per_nombre = "Diciembre" 
    per.per_ennumero = 12
    per.tipper_codigo = "ME"
    per.insert() 

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "14"
    per.per_nombre = "Semestre I" 
    per.per_ennumero = 6
    per.tipper_codigo = "SE"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "15"
    per.per_nombre = "Semestre II" 
    per.per_ennumero = 12
    per.tipper_codigo = "SE"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "16"
    per.per_nombre = "Trimestre I" 
    per.per_ennumero = 3
    per.tipper_codigo = "TR"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "17"
    per.per_nombre = "Trimestre II" 
    per.per_ennumero = 6
    per.tipper_codigo = "TR"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "18"
    per.per_nombre = "Trimestre III" 
    per.per_ennumero = 9
    per.tipper_codigo = "TR"
    per.insert()

    per = frappe.new_doc("sil_periodicidad")
    per.per_codigo = "19"
    per.per_nombre = "Trimestre IV" 
    per.per_ennumero = 12
    per.tipper_codigo = "TR"
    per.insert()
    frappe.db.commit()
    insertDPA();
    insertcentroides();
    roles();
    insertsatelites();

#bench --site silweb execute pgapp.setup.insertDPA 
def insertDPA( ):
    ruta = os.path.abspath(frappe.get_app_path("pgapp","datos"))
    dpas= abrirjson(ruta+"/dpa.json") 
    frappe.db.delete("sil_dpa")
    for rw in dpas:
        dpa = frappe.new_doc("sil_dpa")
        dpa.dpa_anio = "2020"
        dpa.dpa_provincia = str(rw["DPA_PROVIN"]).zfill(2)
        dpa.dpa_canton = str(rw["DPA_CANTON"]).zfill(4)
        dpa.dpa_parroquia = str(rw["DPA_PARROQ"]).zfill(6)
        dpa.dpa_nprovincia = rw["DPA_DESPRO"]
        dpa.dpa_ncanton = rw["DPA_DESCAN"]
        dpa.dpa_nparroquia = rw["DPA_DESPAR"]
        dpa.insert()
    
    print("DPA insertados")
#bench --site silweb execute pgapp.setup.insertsatelites 
def insertsatelites():
    frappe.db.delete("sil_fuenteinformacion")
    obj = frappe.new_doc("sil_fuenteinformacion")
    obj.fueinf_codigo = "01"
    obj.fueinf_descripcion = "Registro Institucional"
    obj.insert()

    obj = frappe.new_doc("sil_fuenteinformacion")
    obj.fueinf_codigo = "02"
    obj.fueinf_descripcion = "Registro Admnistrativo del GAD"
    obj.insert()

    obj = frappe.new_doc("sil_fuenteinformacion")
    obj.fueinf_codigo = "03"
    obj.fueinf_descripcion = "Catastro Predial Urbano o Rural"
    obj.insert()

    obj = frappe.new_doc("sil_fuenteinformacion")
    obj.fueinf_codigo = "04"
    obj.fueinf_descripcion = "Certificados de Uso del Suelo"
    obj.insert()

    obj = frappe.new_doc("sil_fuenteinformacion")
    obj.fueinf_codigo = "05"
    obj.fueinf_descripcion = "Reporte de Agua Potable y Alcantarillado"
    obj.insert()

    obj = frappe.new_doc("sil_fuenteinformacion")
    obj.fueinf_codigo = "06"
    obj.fueinf_descripcion = "Sistema Financiero GAD"
    obj.insert()

    obj = frappe.new_doc("sil_fuenteinformacion")
    obj.fueinf_codigo = "07"
    obj.fueinf_descripcion = "COE Provincial"
    obj.insert()
    ## 
    frappe.db.delete("sil_representacion")
    obj = frappe.new_doc("sil_representacion")
    obj.rep_codigo = "01"
    obj.rep_descripcion = "Provincial"
    obj.insert()

    obj = frappe.new_doc("sil_representacion")
    obj.rep_codigo = "02"
    obj.rep_descripcion = "Cantonal"
    obj.insert()

    obj = frappe.new_doc("sil_representacion")
    obj.rep_codigo = "03"
    obj.rep_descripcion = "Parroquial"
    obj.insert()

    ##### 
    frappe.db.delete("sil_unidadmedida")
    obj = frappe.new_doc("sil_unidadmedida")
    obj.unimed_codigo = "POR"
    obj.unimed_desc = "PORCENTAJE"
    obj.insert()

    obj = frappe.new_doc("sil_unidadmedida")
    obj.unimed_codigo = "NUM"
    obj.unimed_desc = "NUMERO"
    obj.insert()

    obj = frappe.new_doc("sil_unidadmedida")
    obj.unimed_codigo = "UNI"
    obj.unimed_desc = "UNIDAD"
    obj.insert()

    obj = frappe.new_doc("sil_unidadmedida")
    obj.unimed_codigo = "KM"
    obj.unimed_desc = "KILOMETROS"
    obj.insert()
    ################
  
    frappe.db.delete("sil_tipovalor")
    obj = frappe.new_doc("sil_tipovalor")
    obj.tipval_codigo = "VUN"
    obj.tipval_descripcion = "Valor Único"
    obj.insert()

    obj = frappe.new_doc("sil_tipovalor")
    obj.tipval_codigo = "VPC"
    obj.tipval_descripcion = "Valor porcentual por Categoria"
    obj.insert()

    obj = frappe.new_doc("sil_tipovalor")
    obj.tipval_codigo = "VUC"
    obj.tipval_descripcion = "Valor unico por categoria"
    obj.insert()
    ################

    frappe.db.delete("sil_tipoadjunto")
    obj = frappe.new_doc("sil_tipoadjunto")
    obj.tipadj_codigo = "IMG"
    obj.tipadj_desc = "IMAGEN"
    obj.insert()

    obj = frappe.new_doc("sil_tipoadjunto")
    obj.tipadj_codigo = "VID"
    obj.tipadj_desc = "VIDEO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoadjunto")
    obj.tipadj_codigo = "PDF"
    obj.tipadj_desc = "DOCUMENTO PD"
    obj.insert()
    ################

    frappe.db.delete("sil_componente")
    obj = frappe.new_doc("sil_componente")
    obj.com_codigo = "TE"
    obj.com_nombre = "Territorial"
    obj.insert()

    obj = frappe.new_doc("sil_componente")
    obj.com_codigo = "AC"
    obj.com_nombre = "Atencion Ciudadana"
    obj.insert()

    obj = frappe.new_doc("sil_componente")
    obj.com_codigo = "AF"
    obj.com_nombre = "Administrativo Financiero"
    obj.insert()

    obj = frappe.new_doc("sil_componente")
    obj.com_codigo = "IP"
    obj.com_nombre = "Institucional"
    obj.insert()

    ################

    frappe.db.delete("sil_estado")
    obj = frappe.new_doc("sil_estado")
    obj.est_codigo = "A"
    obj.est_descripcion = "ACTIVO"
    obj.insert()

    obj = frappe.new_doc("sil_estado")
    obj.est_codigo = "I"
    obj.est_descripcion = "INACTIVO"
    obj.insert()

     ################

    frappe.db.delete("sil_estadoobra")
    obj = frappe.new_doc("sil_estadoobra")
    obj.estobr_codigo = "I"
    obj.estobr_desc = "Inicio"
    obj.insert()

    obj = frappe.new_doc("sil_estadoobra")
    obj.estobr_codigo = "P"
    obj.estobr_desc = "En Proceso"
    obj.insert()

    obj = frappe.new_doc("sil_estadoobra")
    obj.estobr_codigo = "T"
    obj.estobr_desc = "Terminada"
    obj.insert()

    ################

    frappe.db.delete("sil_grupoindicador")
    obj = frappe.new_doc("sil_grupoindicador")
    obj.gruind_codigo = "VIAVIA"
    obj.gruind_descripcion = "FOMENTO PRODUCTIVO"
    obj.insert()
  
    obj = frappe.new_doc("sil_grupoindicador")
    obj.gruind_codigo = "FOMPRO"
    obj.gruind_descripcion = "RIEGO Y DRENAJE"
    obj.insert()   

    obj = frappe.new_doc("sil_grupoindicador")
    obj.gruind_codigo = "RIEDRE"
    obj.gruind_descripcion = "RIEGO Y DRENAJE"
    obj.insert()  
    ###########

    frappe.db.delete("sil_tipoobra")
    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "VIAVIA"
    obj.tipobr_icono = "VIAS"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "VIAASF"
    obj.tipobr_icono = "ASFALTADO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "VIAADO"
    obj.tipobr_icono = "ADOQUINADO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "VIAEMP"
    obj.tipobr_icono = "EMPREDADO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "VIALAS"
    obj.tipobr_icono = "LASTRADO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "ALCDUC"
    obj.tipobr_icono = "ALCANTARILLADO DUCTOS"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "LIMDES"
    obj.tipobr_icono = "LIMPIEZA Y DESAZOLVE"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "CANRIE"
    obj.tipobr_icono = "CANALES DE RIEGO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "REHRIE"
    obj.tipobr_icono = "REHABILITACION RIEGO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "DRAREL"
    obj.tipobr_icono = "DRAGADO Y RELLENO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "PUEPUE"
    obj.tipobr_icono = "PUENTES"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "AGRAGR"
    obj.tipobr_icono = "AGROPECUARIO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "EQUIEQUI"
    obj.tipobr_icono = "EQUIPAMIENTO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "MEJRIE"
    obj.tipobr_icono = "MEJORAMIENTO RIEGO"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "MEJVIA"
    obj.tipobr_icono = "MEJORAMIENTO VIAL"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "MURCON"
    obj.tipobr_icono = "MURO DE CONTENCION"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "CONEST"
    obj.tipobr_icono = "CONSULTORIA ESTUDIOS"
    obj.insert()

    obj = frappe.new_doc("sil_tipoobra")
    obj.tipobr_desc = "OTROBR "
    obj.tipobr_icono = "OTRAS OBRA"
    obj.insert()

    
    ################

    frappe.db.delete("sil_formato")
    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "TAB"
    obj.for_descripcion = "Tabla"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "GBA"
    obj.for_descripcion = "Grafico Barras"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "GBC"
    obj.for_descripcion = "Grafico Columnas"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "GPI"
    obj.for_descripcion = "Grafico Pie"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "GPD"
    obj.for_descripcion = "Grafico Dona"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "GLI"
    obj.for_descripcion = "Grafico Lineas"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "GAR"
    obj.for_descripcion = "Grafico Areas"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "GMA"
    obj.for_descripcion = "Grafico Mapa Punto"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "GMC"
    obj.for_descripcion = "Grafico Mapa Areas (coropletico)"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "PDF"
    obj.for_descripcion = "Archivo PDF a exhibir"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "TXT"
    obj.for_descripcion = "Archivo TEXTO a exhibir"
    obj.insert()

    obj = frappe.new_doc("sil_formato")
    obj.for_codigo = "IMG"
    obj.for_descripcion = "Archivo Imagen a exhibir"
    obj.insert()

    ################

    frappe.db.delete("tipodetalle")
    obj = frappe.new_doc("tipodetalle")
    obj.tipdet_codigo = "LON"
    obj.tipdet_desc = "LONGITUD DE LA OBRA"
    obj.insert()

    obj = frappe.new_doc("tipodetalle")
    obj.tipdet_codigo = "SUP"
    obj.tipdet_desc = "SUPERFICIE DE LAOBRA"
    obj.insert()

    obj = frappe.new_doc("tipodetalle")
    obj.tipdet_codigo = "POB"
    obj.tipdet_desc = "POBLACION BENEFICIARIA"
    obj.insert()

    obj = frappe.new_doc("tipodetalle")
    obj.tipdet_codigo = "AVA"
    obj.tipdet_desc = "AVANCE DE LA OBRA"
    obj.insert()

    obj = frappe.new_doc("tipodetalle")
    obj.tipdet_codigo = "CON"
    obj.tipdet_desc = "CONTRATO"
    obj.insert()

     ################

 
    frappe.db.delete("sil_tipogeografico")
    obj = frappe.new_doc("sil_tipogeografico")
    obj.tipgeo_codigo = "PU"
    obj.tipgeo_desc = "PUNTO"
    obj.insert()

    obj = frappe.new_doc("sil_tipogeografico")
    obj.tipgeo_codigo = "LI"
    obj.tipgeo_desc = "LINEA"
    obj.insert()

    obj = frappe.new_doc("sil_tipogeografico")
    obj.tipgeo_codigo = "PO"
    obj.tipgeo_desc = "POLIGONO"
    obj.insert()

    obj = frappe.new_doc("sil_tipogeografico")
    obj.tipgeo_codigo = "SN"
    obj.tipgeo_desc = "SIN TIPO"
    obj.insert()







#bench --site silweb execute pgapp.setup.insertcentroides 
def insertcentroides():
    ruta = os.path.abspath(frappe.get_app_path("pgapp","datos"))
    frappe.db.delete("sil_centroide")
    with open(ruta+'/centroides.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f' ===> {", ".join(row)}')
                line_count += 1
            else:
              
                dpac = frappe.new_doc("sil_centroide")
                dpac.cent_pda = row[0]
                dpac.cent_lat = row[1]
                dpac.cent_lon = row[2]
                dpac.insert()

                line_count += 1
    print(f'Processed {line_count} lines.')

def roles():
    roles=['COORDINADOR','OPERADOR','Accounts User','Translator']
    rol=frappe.new_doc('Role Profile')     
    rol.role_profile="sil_admin"
    rol.save()
    ix=1
    for r in roles:
            hr=frappe.new_doc('Has Role')
            hr.parent= rol.name
            hr.role=r
            hr.parentfield='roles'
            hr.parenttype='Role Profile'
            hr.idx=ix
            hr.save()
            ix=ix+1
    
    modprof = frappe.new_doc("Module Profile")
    modprof.module_profile_name = "ModEmpresa"
    modulosNoOcupa=["Workflow","Integrations","Custom","Website","Core","Social" ,"Event Streaming"]
    for md in modulosNoOcupa:
        modprof.append("block_modules", {"module": md} )
    modprof.insert()


def abrirjson(ruta):
    	with open(ruta, 'r') as f:
            data = json.load(f)
            return data
