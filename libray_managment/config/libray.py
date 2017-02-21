from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Libray Manage"),
			"items": [
				{
					"type": "doctype",
					"name": "Libray Member",
					"description": _("Support queries from customers."),
				},
				{
					"type": "doctype",
					"name": "Referance Person",
					"description": _("Support queries from customers."),
				},
				{
					"type": "doctype",
					"name": "Templete Article",
					"description": _("Support queries from customers."),
				},
				{
					"type": "doctype",
					"name": "Membership",
					"description": _("Support queries from customers."),
				},
				{
					"type": "doctype",
					"name": "Article",
					"description": _("Support queries from customers."),
				}


				
			]
		}
	]