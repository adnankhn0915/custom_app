# Copyright (c) 2026, me and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class StoreProduct(WebsiteGenerator):
	def get_context(self, context):
		context.add_breadcrumbs = True
		context.parents = [
			{
				"label": "Store",
				"route": "/Products"
			},
			{
				"label": self.printrove_category,
				"route": f"/store/category/{self.printrove_category_id}"
			}
		]
		settings = frappe.get_cached_doc("Printrove Settings")
		if settings.use_custom_template:
			custom_rendered_html = frappe.render_template(
				settings.custom_template,{"doc":self}
			)
			context.custom_rendered_html = custom_rendered_html