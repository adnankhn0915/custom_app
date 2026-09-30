// Copyright (c) 2026, me and contributors
// For license information, please see license.txt

frappe.ui.form.on("Printrove Settings", {
	refresh(frm) {
        const btn = frm.add_custom_button("Sync Products Now", ()=>{
            frappe.call({
                method: "custom_app.tasks.sync_products_from_printrove",
                btn
            }).then(()=>{
                frappe.show_alert({
                    message: "Products synced successfully!",
                    indicator: "green"
                })
            })
        })
	},
});
