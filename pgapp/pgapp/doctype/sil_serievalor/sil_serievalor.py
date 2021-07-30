# -*- coding: utf-8 -*-
# Copyright (c) 2021, orlando and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class sil_serievalor(Document):
	def before_insert(self): 
    		self.serval_codigo = self.sil_ingreso_ind+"_" +self.sil_periodicidad+"_" + self.sil_periodo

	@frappe.whitelist()
	def getProvincia(self):
		sql = '''select distinct  dpa_nprovincia from "tabsil_dpa"    where dpa_provincia = '13' '''
		cantones = frappe.db.sql (sql, as_dict=1)
		return cantones[0]
	
	@frappe.whitelist()
	def getCantones(self):
		sql = '''select distinct  dpa_nprovincia, dpa_canton , dpa_ncanton from "tabsil_dpa"    where dpa_provincia = '13' order by dpa_ncanton'''
		cantones = frappe.db.sql (sql, as_dict=1)
		return cantones

	@frappe.whitelist()
	def getParroquia(self):
		sql = '''select distinct  dpa_nprovincia, dpa_canton , dpa_ncanton ,dpa_parroquia ,dpa_nparroquia from "tabsil_dpa"    where dpa_provincia = '13' order by dpa_ncanton,dpa_nparroquia'''
		cantones = frappe.db.sql (sql, as_dict=1)
		return cantones
