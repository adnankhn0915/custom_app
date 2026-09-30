frappe.listview_settings['Store Product'] = {
    get_indicator: function(doc) {
        let status = "Not Published"
        let color = "grey"
        if(doc.is_published)
            status = "Published"
            color = "green"

    return [__(status), color, "is_published,=," + doc.is_published]
    }
}