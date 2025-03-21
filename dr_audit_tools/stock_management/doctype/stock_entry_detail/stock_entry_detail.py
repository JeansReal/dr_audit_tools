from frappe.model.document import Document


class StockEntryDetail(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		item_code: DF.Link
		item_name: DF.ReadOnly | None
		merma: DF.Float
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		qty: DF.Float
		qty_total: DF.Float
	# end: auto-generated types
	pass
