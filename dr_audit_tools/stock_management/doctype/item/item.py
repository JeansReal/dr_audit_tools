# Copyright (c) 2025, Agile Shift and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Item(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.Data
		uom: DF.Literal["", "LIBRA", "UNIDAD"]
	# end: auto-generated types
	pass
