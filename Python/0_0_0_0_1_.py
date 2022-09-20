
# print(4%5)
# print(5%4)

# print(60%40)

# print(1e4)
# j=0
# print(type(3j+3*j))

# print([i + 'phile' for i in ('Cyno', 'Oro', 'Nycto')])

# ['Cynophile', 'Orophile', 'Nyctophile']
# m = 0.0
# n = 10
# print(m or n)
comb_info = {
    "has_discounted_price" : False,
    "list_price" : 80000.0,
    "price" : 98000.0, 
}
x = comb_info['has_discounted_price'] and comb_info['list_price'] or comb_info['price'] or 0

{'product_id': 1274, 'product_template_id': 1282, 'display_name': '[INSK028C02] Abacel 18 EC - 500 ml', 'display_image': False, 'price': 98000.0, 'list_price': 80000.0, 'price_extra': 0.0, 'has_discounted_price': False}
print(x)
{'product_id': 1277, 'product_template_id': 1285, 'display_name': '[INSK028C03] Abacel 18 EC - 500 ml', 'display_image': False, 'price': 95000.0, 'list_price': 110000.0, 'price_extra': 0.0, 'has_discounted_price': True}