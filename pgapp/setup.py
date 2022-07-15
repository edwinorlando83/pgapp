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

def abrirjson(ruta):
    	with open(ruta, 'r') as f:
            data = json.load(f)
            return data
