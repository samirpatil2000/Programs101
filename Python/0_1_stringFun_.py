s="aabcbaa"
# a=dict.fromkeys(s,s.count())
# print(a)
# co=
# print(co)
sa={char:(s.count(char)) for char in s}
print(sa)

print(ord("a"),ord("A"))
print(chr(97))


def dicto():
    dict_={'a': 2, 'b': 1, 's': 1}
    dict_['a']-=1
    print(dict_['a'],dict_.values)
    dict_['k']=2
    print(dict_)
    return

# dicto()

def pangram():
    word_dict={chr(i):0 for i in range(65,91)}
    
    word_dict.update({chr(i):0 for i in range(97,123)})
    print(word_dict)
    
    
# pangram()
print(ord("A"),ord("Z"),chr(90),ord("z"))
print(chr(97+25))
print(0%25,"0%25")
print(chr(93).isalpha())

x,y=set("unn"),set("ny")
print(x.union(y))
print(x)



# print(" ".join([str(3),str(2),str(32),str(32)]))



print("3".isnumeric())

print(ord("a"),ord("A"),ord("z"),ord("Z"))

x = "Sam SAMIR "
print(len(x))
x = x.strip()
print(x, len(x))
x = x.split()
print(x)


class ProductService:
    def build_search_query(self, search_query: str, **kwargs):
        or_operator_count = 0
        product_ids = []
        search_queries = []
        for query in search_query.split(" "):
            or_operator_count += 1
            search_queries += [('name', 'ilike', query)]
            product_ids += self.get_product_ids(query, **kwargs)
        if or_operator_count:
            or_operator_count -= 1
        return product_ids, search_queries, or_operator_count

    def get_domain(self, search_query, **kwargs):
        domain = []
        product_ids, search_queries, or_operator_count = self.build_search_query(search_query, **kwargs)
        if product_ids:
            or_operator_count += 1
            domain += [('id', 'in', product_ids)]
        domain += search_queries
        return ['|'] * or_operator_count + domain