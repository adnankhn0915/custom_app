import frappe

from frappe.integrations.utils import make_get_request,make_post_request

BASE_URL = "https://api.printrove.com/"

SECOND_IN_YEAR = 365 * 24 * 60 * 60

def get_access_token():
    token = frappe.cache.get_value("printrove_access_token")
    if token:
        return token
    printrove_settings = frappe.get_cached_doc("Printrove Settings")
    auth_route = "api/external/token"
    response = make_post_request(
        f"{BASE_URL}{auth_route}",
        data ={"email":printrove_settings.email,
               "password":printrove_settings.get_password("password")
               })
    access_token = response["access_token"]
    frappe.cache.set_value("printrove_access_token",access_token,expires_in_sec=SECOND_IN_YEAR)
    return access_token

@frappe.whitelist()
def sync_products_from_printrove():
    access_token = get_access_token()
    product_route = "api/external/products"
    headers = {"Authorization": f"Bearer {access_token}"}
    all_products = make_get_request( f"{BASE_URL}{product_route}", headers = headers)
    all_products = all_products["products"]
    
    for product in all_products:
        product_data = {
            "front_mockup" : product["mockup"]["front_mockup"],
            "back_mockup" :product["mockup"]["back_mockup"]
        }
        if not frappe.db.exists("Store Product",{"printrove_id" : product["id"]}):
        
            doc = frappe.get_doc({
                "doctype":"Store Product",
                "name": product["name"],
                "printrove_id" :product["id"],
                **product_data
            }).insert(ignore_permissions = True)
        else:
            doc = frappe.get_doc("Store Product",{"printrove_id":product["id"]})
            doc.update({
                **product_data
            })
            doc.save(ignore_permissions = True)
            