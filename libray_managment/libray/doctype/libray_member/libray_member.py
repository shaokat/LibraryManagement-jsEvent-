# -*- coding: utf-8 -*-
# Copyright (c) 2015, Hasan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe.utils.data import nowdate,add_years
import re


class LibrayMember(Document):
	def autoname(self):
		self.name=make_autoname('LM/.####')+'-'+str(self.frist_name)
		
	def on_submit(self):
		self.make_meebership()

	def make_meebership(self):
		doc=frappe.new_doc("Membership")

		doc.set('member_name',self.name)
		doc.set('member_frist_name',self.frist_name)
		doc.set('member_last_name',self.last_name)
		doc.set('status','Active')
		doc.set('email',self.email)
		doc.set('phone',self.phone)
		doc.set('form_date',nowdate())
		doc.set('to_date',add_years(nowdate(),1))
		doc.save()
		
		
		doc.submit()
		frappe.msgprint("Libray Membership Are Generate For 1 Year")

	def validate(self):
		frist_name=self.frist_name
		
		test=re.match("[a-zA-Z]",frist_name)
		frappe.throw(str(test))