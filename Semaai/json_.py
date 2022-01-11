import json
dict_={'success': True, 'responseCode': 2, 'message': 'Login successfully.', 'itemsPerPage': 10, 'context': {'pricelist': 'product.pricelist(1,)', 'currency_id': 12, 'currencySymbol': 'Rp', 'currencyPosition': 'before', 'allowed_company_ids': [1], 'website_id': 1, 'websiteObj': 'website(1,)', 'tz': 'Asia/Calcutta', 'bin_size': False, 'edit_translations': False, 'uid': 80, 'partner': 'res.partner(102,)', 'user': 'res.users(80,)', 'lang': 'en_US', 'teamId': 5, 'salespersonId': False, 'lang_obj': 'res.lang(1,)', 'base_url': 'http://localhost:8080/', 'mobikul_obj': 'mobikul(1,)'}, 'addons': {'wishlist': True, 'review': False, 'email_verification': False, 'odoo_marketplace': True, 'website_sale_delivery': True, 'odoo_gdpr': False, 'website_sale_stock': True, 'website_customer_group': True}, 'customerId': 102, 'userId': 80, 'cartCount': 0, 'WishlistCount': 0, 'is_seller': False, 'seller_group': 'marketplace_seller_group', 'seller_state': 'new'}
print(json.dumps(dict_))

dict_={
      "category_id": "<category_id>",
      "name": "<category_name>",
      "children": [
        {
          "category_id": "<category_id>",
          "name": "<category_name>",
          "children": [
            {
              "category_id": "<category_id>",
              "name": "<category_name>",
              "children": [],
              "icon": "<image_url>",
            }
          ],
          "icon": "<image_url>"
        }
      ],
      "icon": "<image_url>"
    }
dict_={
"categories": [
    {
      "category_id": "<category_id>",
      "name": "<category_name>",
      "children": [
        {
          "category_id": "<category_id>",
          "name": "<category_name>",
          "children": [
            {
              "category_id": "<category_id>",
              "name": "<category_name>",
              "children": [],
              "icon": "<image_url>",
            }
          ],
          "icon": "<image_url>"
        }
      ],
      "icon": "<image_url>"
    }
  ],
}
dict_={'success': True, 'responseCode': 2, 'message': 'Login successfully.', 'itemsPerPage': 10, 'context': {'pricelist': 'product.pricelist(1,)', 'currency_id': 12, 'currencySymbol': 'Rp', 'currencyPosition': 'before', 'allowed_company_ids': [1], 'website_id': 1, 'websiteObj': 'website(1,)', 'tz': 'Asia/Calcutta', 'bin_size': False, 'edit_translations': False, 'uid': 80, 'partner': 'res.partner(102,)', 'user': 'res.users(80,)', 'lang': 'en_US', 'teamId': 5, 'salespersonId': False, 'lang_obj': 'res.lang(1,)', 'base_url': 'http://localhost:8080/', 'mobikul_obj': 'mobikul(1,)'}, 'addons': {'wishlist': True, 'review': False, 'email_verification': False, 'odoo_marketplace': True, 'website_sale_delivery': True, 'odoo_gdpr': False, 'website_sale_stock': True, 'website_customer_group': True}, 'customerId': 102, 'userId': 80, 'cartCount': 0, 'WishlistCount': 0, 'is_seller': False, 'seller_group': 'marketplace_seller_group', 'seller_state': 'new'}
dict_={'success': True, 'responseCode': 2, 'message': 'Login successfully.', 'itemsPerPage': 10, 'context': {'pricelist': 'product.pricelist(1,)', 'currency_id': 12, 'currencySymbol': 'Rp', 'currencyPosition': 'before', 'allowed_company_ids': [1], 'website_id': 1, 'websiteObj': 'website(1,)', 'tz': 'Europe/Brussels', 'bin_size': False, 'edit_translations': False, 'uid': 4, 'partner': 'res.partner(4,)', 'user': 'res.users(4,)', 'lang': 'en_US', 'teamId': 5, 'salespersonId': False, 'lang_obj': 'res.lang(1,)', 'base_url': 'http://localhost:8080/', 'mobikul_obj': 'mobikul(1,)'}, 'addons': {'wishlist': True, 'review': False, 'email_verification': False, 'odoo_marketplace': True, 'website_sale_delivery': True, 'odoo_gdpr': False, 'website_sale_stock': True, 'website_customer_group': True}}
# print(json.dumps(dict_))
# x="\n\n \n"

# if x.isalnum():
#     print("yes")
# else:
#     print("no")
name=""
result=(name or "") + (name and "\n" or "")
if not result.isalnum():
    print("yes")
print(result)
print("Samir" and "Sam" or False)
