from frappe.model.document import Document


class StockEntry(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from dr_audit_tools.stock_management.doctype.stock_entry_detail.stock_entry_detail import StockEntryDetail
		from frappe.types import DF

		comments: DF.SmallText | None
		description: DF.Data
		details: DF.Table[StockEntryDetail]
		fecha: DF.Date
		reason: DF.Link
		status: DF.Literal["Activo", "Anulado"]
		type: DF.Literal["", "Entrada", "Salida", "Ajuste"]
	# end: auto-generated types
	pass

	def before_save(self):
		# Recalculate -> Just to be on the safe side
		for detail in self.details:
			detail.qty_total = detail.qty if not detail.merma else detail.qty - detail.merma
