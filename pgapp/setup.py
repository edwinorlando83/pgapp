import frappe
import json

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


