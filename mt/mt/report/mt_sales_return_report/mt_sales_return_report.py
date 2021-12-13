# Copyright (c) 2013, GreyCube Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt
from frappe import msgprint, _

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data(filters)
	return columns, data

def get_columns():
	"""return columns based on filters"""
	columns = [
		{
			'label': _("Invoice"),
			'fieldname': 'name',
			'fieldtype': 'Link',
			'options': 'Sales Invoice',
			'width': 90
		},
		{
			'label': _("Return Against"),
			'fieldname': 'return_against',
			'fieldtype': 'Link',
			'options': 'Sales Invoice',
			'width': 100
		},		
		{
			'label': _("Posting Date"),
			'fieldname': 'posting_date',
			'fieldtype': 'Date',
			'width': 110
		},
		{
			'label': _("Customer"),
			'fieldname': 'customer',
			'fieldtype': 'Link',
			'options': 'Customer',
			'width': 210
		},
		{
			'label': _("Tax id"),
			'fieldname': 'tax_id',
			'fieldtype': 'Data',
			'width': 100
		},
		{
			'label': _("Owner"),
			'fieldname': 'owner',
			'fieldtype': 'Link',
			'options': 'User',
			'width': 120
		},		
		{
			'label': _("Total"),
			'fieldname': 'total',
			'fieldtype': 'Data',
			'width': 120
		},
		{
			'label': _("Total Taxes"),
			'fieldname': 'total_taxes_and_charges',
			'fieldtype': 'Data',
			'width': 120
		},
		{
			'label': _("Grand Total"),
			'fieldname': 'grand_total',
			'fieldtype': 'Data',
			'width': 120
		}		
	]
	return columns

def get_data(filters):
	conditions=" AND 1=1"
	if filters.get("customer"):
		conditions = " AND customer = %(customer)s"


	return frappe.db.sql("""select name,return_against,posting_date,customer,tax_id,owner,total,total_taxes_and_charges,grand_total 
	from `tabSales Invoice`
	where is_return = 1 and docstatus = 1 
	{conditions}
	and posting_date >=%(from_date)s and posting_date <=%(to_date)s 
		""".format(conditions=conditions), filters, as_list=1)	