# -*- coding: utf-8 -*-
# Copyright (c) 2021, orlando and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class grupo_capas(Document):
	def validate(self):
		if not self.parent_grupo_capas:
			self.nivel = 1 
    			
		#if frappe.db.exists("grupo_capas", {"nombre":self.name}) :
		#frappe.throw(self.name)
