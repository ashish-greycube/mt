from __future__ import unicode_literals
from frappe import _
import frappe

def get_data():
	return [
		{
			"label": _("MT Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "MT General Ledger",
					"doctype": "GL Entry"
				}
			]
		}
	
	]