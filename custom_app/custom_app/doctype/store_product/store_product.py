# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class StoreProduct(WebsiteGenerator):
	def get_context(self, context):
		settings = frappe.get_cached_doc("Printrove Settings")
		if settings.use_custom_template:
			custom_rendered_html = frappe.render_template(
				settings.custom_template,{"doc":self}
			)
			context.custom_rendered_html = custom_rendered_html