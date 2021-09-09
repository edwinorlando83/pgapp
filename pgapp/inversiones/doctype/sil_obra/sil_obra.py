# Copyright (c) 2021, orlando and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class sil_obra(Document):
	
	@frappe.whitelist()
	def getCantones(self):
		return get_cantones()
	
	@frappe.whitelist()
	def getParroquias(self, canton):
		return get_parroquias(canton)

    		
@frappe.whitelist()
def get_cantones():
	sql = """select distinct  dpa_ncanton  from \"tabsil_dpa\"  where dpa_provincia = (select  value from \"tabSingles\"  ts where field = 'dpa_provincia')"""
	return frappe.db.sql(sql)

def get_parroquias(canton):
	sql = """select    dpa_nparroquia  from \"tabsil_dpa\"  where  dpa_ncanton = %s """
	return frappe.db.sql(sql,canton)
