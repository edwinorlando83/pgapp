# -*- coding: utf-8 -*-
# Copyright (c) 2021, orlando and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class sil_periodo(Document):
	def validate(self):
		if self.period_mes not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
			frappe.throw("El mes debe ser un valor entre 1 y 12")
    		
	def before_insert(self):
		self.period_codigo = str(self.period_anio) + "-" + str(self.period_mes).zfill(2)
