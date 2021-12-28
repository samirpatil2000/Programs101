product_ids=[]
q=[]
domain=[]
for s in ("Battery","FMC"):
    q += [('name', 'ilike', s)]
    product_ids+=[12,34,5]
if product_ids:
    domain+=[['|',('id','in',product_ids),*q]]
print(domain)
domain=[('|', ('name', 'ilike', 'Battery'), ('name', 'ilike', 'FMC')),('id', 'in', [12, 34, 5, 12, 34, 5])]

(217, 234, 218, 57, 58)
['|', ('id', 'in', [217, 553, 554, 234, 218, 219, 557, 556, 555, 57, 58, 221, 220, 107]), ('name', 'ilike', 'fmc'), ('sale_ok', '=', True), ('is_mobikul_available', '=', True), ('company_id', 'in', [1, False])]
(217, 234, 218, 57, 58)

['|', '|', ('id', 'in', [217, 553, 554, 234, 218, 219, 557, 556, 555, 57, 58, 221, 220, 107]), ('name', 'ilike', 'battery'), ('name', 'ilike', 'fmc'), ('sale_ok', '=', True), ('is_mobikul_available', '=', True), ('company_id', 'in', [1, False])]


(203, 200, 201, 202, 80)
['|', ('name', 'ilike', 'battery'), ('sale_ok', '=', True), ('is_mobikul_available', '=', True), ('company_id', 'in', [1, False])] 




