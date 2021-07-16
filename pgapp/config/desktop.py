# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "pgapp",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("pgapp")
		},
		{
			"module_name": "silgeo",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("silgeo")
		}
	]
