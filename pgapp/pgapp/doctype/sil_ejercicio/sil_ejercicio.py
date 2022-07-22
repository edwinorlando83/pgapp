# Copyright (c) 2022, orlando and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class sil_ejercicio(Document):
	def on_update(self):
		if self.docstatus == 1:			 
			lst = frappe.get_all("sil_periodicidad",fields=["per_ennumero","name","per_nombre","tipper_codigo"])
			for rw in lst:				
					per = frappe.new_doc("sil_periodo")
					per.period_anio = self.eje_codigo
					per.period_mes = rw.per_ennumero
				 
					per.eje_codigo = self.name
					per.per_codigo= rw.name 
					per.period_codigo = str(self.eje_codigo) + "-" + str(rw.per_nombre) 
					per.insert()

