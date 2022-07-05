# -*- coding: utf-8 -*-
# Copyright (c) 2021, orlando and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import requests
from requests.auth import HTTPBasicAuth
 
class sil_sil_capa(Document):

    		

	def getCapas(self):
		srvmap = frappe.get_doc("servidores_mapa",self.servidores_mapa)
		url =  srvmap.url + "rest/layers.json"
		#frappe.throw(srvmap.usuario + "  " +  srvmap.password)
		authKey = 'admin:geoserver'
		headers ={'Authorization': "Basic " + authKey}
		r = requests.get(url, headers=headers ) 
		return r 
