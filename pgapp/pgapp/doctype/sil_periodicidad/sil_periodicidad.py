# -*- coding: utf-8 -*-
# Copyright (c) 2021, orlando and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class sil_periodicidad(Document):
	def generar():
		anio = frappe.db.get_single_value('sil_parametrosg', 'par_anioinicio')
		if not anio:
			frappe.throw("No se ha definido el año de incio, por favor defina el año en el formulario de  parámetros")
		
		per = frappe.new_doc("sil_periodo")
