# Copyright (c) 2024, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RepostSalesInvoice(Document):
	@staticmethod
	def clear_old_logs(days=30):
		from frappe.query_builder import Interval
		from frappe.query_builder.functions import Now

		table = frappe.qb.DocType("Repost Sales Invoice")
		frappe.db.delete(table, filters=(table.modified < (Now() - Interval(days=days))))
