
class Number:
    intergers = [5, 6, 7]
    for i in intergers:
        i * 2

# print(Number.i)
# print(Number.intergers)

num = [1, 2,  3, 4, 5]
new_list = [num[i] if num[i]&1 == 0 else num[i] * 2 for i in range(len(num)) ]
print(new_list)