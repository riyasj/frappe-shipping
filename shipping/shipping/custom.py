def tot_qty(doc,method):
	from frappe.utils import flt
	import json
	tot_qty = 0.0
	for q in doc.items:
		tot_qty += flt(q.qty)
	doc.tot_qty = tot_qty

def total(doc,method):
	from frappe.utils import flt
	amount = flt(doc.quantity) * flt(doc.rate)
	doc.amount = amount
