# Copyright (c) 2022, orlando and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json

class sil_parametrosg(Document):
	@frappe.whitelist()
	def export_tra(self):
		lst = frappe.get_all("Translation",fields=["source_text","translated_text"])
		with open("/home/frappe/frappe-bench/apps/pgapp/datatraduccion.json", "w") as outfile:
			json.dump(lst, outfile)
		return "Exportado Correctamnete"
	
	@frappe.whitelist()
	def import_tra(self):
		with open('/home/frappe/frappe-bench/apps/pgapp/datatraduccion.json', 'r') as openfile:
			json_object = json.load(openfile)
			for rw in json_object:	 
				tra = frappe.new_doc("Translation")
				tra.source_text = rw["source_text"]
				tra.translated_text = rw["translated_text"]
				tra.insert()
		return "Importado Correctamente"