import json
dict_={'success': True, 'responseCode': 2, 'message': 'Login successfully.', 'itemsPerPage': 10, 'context': {'pricelist': 'product.pricelist(1,)', 'currency_id': 12, 'currencySymbol': 'Rp', 'currencyPosition': 'before', 'allowed_company_ids': [1], 'website_id': 1, 'websiteObj': 'website(1,)', 'tz': 'Asia/Calcutta', 'bin_size': False, 'edit_translations': False, 'uid': 80, 'partner': 'res.partner(102,)', 'user': 'res.users(80,)', 'lang': 'en_US', 'teamId': 5, 'salespersonId': False, 'lang_obj': 'res.lang(1,)', 'base_url': 'http://localhost:8080/', 'mobikul_obj': 'mobikul(1,)'}, 'addons': {'wishlist': True, 'review': False, 'email_verification': False, 'odoo_marketplace': True, 'website_sale_delivery': True, 'odoo_gdpr': False, 'website_sale_stock': True, 'website_customer_group': True}, 'customerId': 102, 'userId': 80, 'cartCount': 0, 'WishlistCount': 0, 'is_seller': False, 'seller_group': 'marketplace_seller_group', 'seller_state': 'new'}
print(json.dumps(dict_))
# dict_={
#       "category_id": "<category_id>",
#       "name": "<category_name>",
#       "children": [
#         {
#           "category_id": "<category_id>",
#           "name": "<category_name>",
#           "children": [
#             {
#               "category_id": "<category_id>",
#               "name": "<category_name>",
#               "children": [],
#               "icon": "<image_url>",
#             }
#           ],
#           "icon": "<image_url>"
#         }
#       ],
#       "icon": "<image_url>"
#     }
# dict_={
# "categories": [
#     {
#       "category_id": "<category_id>",
#       "name": "<category_name>",
#       "children": [
#         {
#           "category_id": "<category_id>",
#           "name": "<category_name>",
#           "children": [
#             {
#               "category_id": "<category_id>",
#               "name": "<category_name>",
#               "children": [],
#               "icon": "<image_url>",
#             }
#           ],
#           "icon": "<image_url>"
#         }
#       ],
#       "icon": "<image_url>"
#     }
#   ],
# }
# dict_={'success': True, 'responseCode': 2, 'message': 'Login successfully.', 'itemsPerPage': 10, 'context': {'pricelist': 'product.pricelist(1,)', 'currency_id': 12, 'currencySymbol': 'Rp', 'currencyPosition': 'before', 'allowed_company_ids': [1], 'website_id': 1, 'websiteObj': 'website(1,)', 'tz': 'Asia/Calcutta', 'bin_size': False, 'edit_translations': False, 'uid': 80, 'partner': 'res.partner(102,)', 'user': 'res.users(80,)', 'lang': 'en_US', 'teamId': 5, 'salespersonId': False, 'lang_obj': 'res.lang(1,)', 'base_url': 'http://localhost:8080/', 'mobikul_obj': 'mobikul(1,)'}, 'addons': {'wishlist': True, 'review': False, 'email_verification': False, 'odoo_marketplace': True, 'website_sale_delivery': True, 'odoo_gdpr': False, 'website_sale_stock': True, 'website_customer_group': True}, 'customerId': 102, 'userId': 80, 'cartCount': 0, 'WishlistCount': 0, 'is_seller': False, 'seller_group': 'marketplace_seller_group', 'seller_state': 'new'}
# # dict_={'success': True, 'responseCode': 2, 'message': 'Login successfully.', 'itemsPerPage': 10, 'context': {'pricelist': 'product.pricelist(1,)', 'currency_id': 12, 'currencySymbol': 'Rp', 'currencyPosition': 'before', 'allowed_company_ids': [1], 'website_id': 1, 'websiteObj': 'website(1,)', 'tz': 'Europe/Brussels', 'bin_size': False, 'edit_translations': False, 'uid': 4, 'partner': 'res.partner(4,)', 'user': 'res.users(4,)', 'lang': 'en_US', 'teamId': 5, 'salespersonId': False, 'lang_obj': 'res.lang(1,)', 'base_url': 'http://localhost:8080/', 'mobikul_obj': 'mobikul(1,)'}, 'addons': {'wishlist': True, 'review': False, 'email_verification': False, 'odoo_marketplace': True, 'website_sale_delivery': True, 'odoo_gdpr': False, 'website_sale_stock': True, 'website_customer_group': True}}
# # print(json.dumps(dict_))
# # x="\n\n \n"

# # if x.isalnum():
# #     print("yes")
# # else:
# #     print("no")

# print(json.dumps(dict_))
# sam="     "
# print("","s")


# """
# -- Database: new_db

# -- DROP DATABASE IF EXISTS new_db;

# -- CREATE DATABASE new_db
# --     WITH 
# --     OWNER = samir
# --     ENCODING = 'UTF8'
# --     LC_COLLATE = 'C'
# --     LC_CTYPE = 'en_US.UTF-8'
# --     TABLESPACE = pg_default
# --     CONNECTION LIMIT = -1;


# Insert 
# 	INTO ir_module_module (id, create_uid, create_date, write_date, write_uid, website, summary, name, author, icon, state, latest_version, shortdesc, category_id, description, application, demo, web, license, sequence, auto_install, to_buy, maintainer, contributors, published_version, url, menus_by_module, reports_by_module, views_by_module)
# 				VALUES (257, NULL, NULL, '2022-01-14 11:13:01.528557', 1, '', 'Total Sales Target for Sales Person Target for salesperson target sales order target sales goal sales person goal sales team target sales person wise target for sales order target based on salesman target for sales target based on salesman goal for sales', 'salesperson_sales_target_app', 'Edge Technologies', '/salesperson_sales_target_app/static/description/icon.png', 'installed', '14.0.1.1', 'Sales Target Based Sales Person', 19, ' Sales Person Sales Target ', False, True, False, 'OPL-1', 100, False, False, NULL, NULL, NULL, 'https://youtu.be/ksExOXqA2bg', 'Sales/Orders/Sales Target', '', 'Sale Target (form) Sale Target (tree)')
# """
# NULL="X"
# x=(335,NULL,NULL,"2022-01-14 11:11:06.038667",1,"https://store.webkul.com/Odoo-Marketplace-Advance-Commission.html","The admin can now set advanced commission rules for his/her Odoo Multi-vendor marketplace on products, products categories and sellers individually.","marketplace_advance_commission","Webkul Software Pvt. Ltd.","/marketplace_advance_commission/static/description/icon.png","installed","14.0.1.0.0","Odoo Marketplace Advance Commission",17,"Seller agent commission Set seller commission Admin commission on Odoo Marketplace Marketplace seller commission Commission rules Odoo seller commission Odoo Seller pays commission Marketplace seller commission rules New commission rules Seller product commission Product sale commission on marketplace Odoo Marketplace Odoo multi vendor Marketplace Multi seller marketplace Multi-seller marketplace multi-vendor Marketplace",True,True,False,"Other proprietary",1,False,False,NULL,NULL,NULL,"http://odoodemo.webkul.com/?module=marketplace_advance_commission&lifetime=120&lout=1&custom_url=/","","","* INHERIT Make Readable Commission (form) * INHERIT Make Readable Commissions (form) * INHERIT Marketplace.base.config.setting.commission (form) * INHERIT mp.commission.inherit.seller.globel.config.form.view (form) * INHERIT product.public.category.form.inherit (form) * INHERIT seller.form.inherit (form) * INHERIT seller.payment (form) * INHERIT seller.product.template.common.form (form) Commtype Desc Wizard Wizard FormView (form)")
# # print(x)
# x=(335, NULL, NULL, '2022-01-14 11:11:06.038667', 1, 'https://store.webkul.com/Odoo-Marketplace-Advance-Commission.html', 'The admin can now set advanced commission rules for his/her Odoo Multi-vendor marketplace on products, products categories and sellers individually.', 'marketplace_advance_commission', 'Webkul Software Pvt. Ltd.', '/marketplace_advance_commission/static/description/icon.png', 'installed', '14.0.1.0.0', 'Odoo Marketplace Advance Commission', 17, 'Seller agent commission Set seller commission Admin commission on Odoo Marketplace Marketplace seller commission Commission rules Odoo seller commission Odoo Seller pays commission Marketplace seller commission rules New commission rules Seller product commission Product sale commission on marketplace Odoo Marketplace Odoo multi vendor Marketplace Multi seller marketplace Multi-seller marketplace multi-vendor Marketplace', True, True, False, 'Other proprietary', 1, False, False, NULL, NULL, NULL, 'http://odoodemo.webkul.com/?module=marketplace_advance_commission&lifetime=120&lout=1&custom_url=/', '', '', '* INHERIT Make Readable Commission (form) * INHERIT Make Readable Commissions (form) * INHERIT Marketplace.base.config.setting.commission (form) * INHERIT mp.commission.inherit.seller.globel.config.form.view (form) * INHERIT product.public.category.form.inherit (form) * INHERIT seller.form.inherit (form) * INHERIT seller.payment (form) * INHERIT seller.product.template.common.form (form) Commtype Desc Wizard Wizard FormView (form)')

# s = {'success': True, 'responseCode': 2, 'message': 'Login successfully.', 'itemsPerPage': 10, 'context': {'pricelist': product.pricelist(1,), 'currency_id': 12, 'currencySymbol': 'Rp', 'currencyPosition': 'before', 'allowed_company_ids': [1], 'website_id': 1, 'websiteObj': website(1,), 'tz': 'Asia/Calcutta', 'bin_size': False, 'edit_translations': False, 'uid': 80, 'partner': res.partner(102,), 'user': res.users(80,), 'lang': 'en_US', 'teamId': 5, 'salespersonId': False, 'lang_obj': res.lang(1,), 'base_url': 'http://localhost:8080/', 'mobikul_obj': mobikul(1,)}, 'addons': {'wishlist': True, 'review': False, 'email_verification': False, 'odoo_marketplace': True, 'website_sale_delivery': True, 'odoo_gdpr': False, 'website_sale_stock': True, 'website_customer_group': True}, 'customerId': 102, 'userId': 80, 'cartCount': 0, 'WishlistCount': 0, 'is_seller': False, 'seller_group': 'marketplace_seller_group', 'seller_state': 'new', 'customerBannerImage': 'http://localhost:8080/web/image/res.partner/102/banner_image?unique=20220108071344', 'customerProfileImage': 'http://localhost:8080/web/image/res.partner/102/image_1920?unique=20220108071344', 'cartId': '', 'themeCode': '?', 'customerName': 'Gaurav Batra', 'customerEmail': '', 'customerPhoneNumber': '8971182182', 'customerLang': 'en'}

