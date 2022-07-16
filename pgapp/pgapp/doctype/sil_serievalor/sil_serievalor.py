# -*- coding: utf-8 -*-
# Copyright (c) 2021, orlando and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class sil_serievalor(Document):
	def before_insert(self):
		if len(self.ind_dpa) == 2: 
			res = getProvincia(self.ind_dpa)
			self.ind_nprovincia = res.dpa_nprovincia 
		
		if len(self.ind_dpa) == 4:
			res = getCanton(self.ind_dpa)
			self.ind_nprovincia = res.dpa_nprovincia
			self.ind_ncanton = res.dpa_ncanton

		if len(self.ind_dpa) == 6:
			res = getParroquia(self.ind_dpa)
			self.ind_nprovincia = res.dpa_nprovincia
			self.ind_ncanton = res.dpa_ncanton		
			self.dpa_nparroquia = res.dpa_nparroquia	

	@frappe.whitelist()
	def getProvincia(self):
		sql = '''select distinct  dpa_nprovincia from tabsil_dpa    where dpa_provincia = '13' '''
		cantones = frappe.db.sql (sql, as_dict=1)
		return cantones[0]
	
 

def getProvincia(codigo):
	sql = """select DISTINCT dpa_nprovincia,dpa_provincia from  tabsil_dpa  where dpa_provincia ='{0}' """.format(codigo)
	return frappe.db.sql(sql, as_dict=1)[0]

def getCanton(codigo):
	sql = """select DISTINCT dpa_ncanton , dpa_canton ,dpa_nprovincia,dpa_provincia  from  tabsil_dpa  where dpa_canton ='{0}' """.format(codigo)
	return frappe.db.sql(sql, as_dict=1)[0]

def getParroquia(codigo):
	sql = """select DISTINCT dpa_ncanton , dpa_canton ,dpa_nprovincia,dpa_provincia, dpa_parroquia , dpa_nparroquia
		from  tabsil_dpa  where dpa_nparroquia ='{0}'  """.format(codigo)
	return frappe.db.sql(sql, as_dict=1)[0]
