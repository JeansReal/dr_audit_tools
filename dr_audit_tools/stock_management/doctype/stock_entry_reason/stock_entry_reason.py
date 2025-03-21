from frappe.model.document import Document


class StockEntryReason(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		reason_name: DF.Data
		type: DF.Literal["", "Entrada", "Salida", "Ajuste"]
	# end: auto-generated types
	pass
