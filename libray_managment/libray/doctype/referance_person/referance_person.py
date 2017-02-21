# -*- coding: utf-8 -*-
# Copyright (c) 2015, Hasan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class ReferancePerson(Document):

	def autoname(self):
		self.name = make_autoname("RP/.####") + '-' + str(self.referance_p_name)

	pass