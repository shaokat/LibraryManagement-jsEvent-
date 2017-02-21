# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Libray Managment",
			"color": "grey",
			"icon": "fa fa-book",
			"type": "module",
			"label": _("Libray Managment")
		},
		{
			"module_name": "Libray",
			"color": "grey",
			"icon": "fa fa-book",
			"type": "module",
			"label": _("Libray")
		}
	]
