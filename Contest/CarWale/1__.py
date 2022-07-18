
from itertools import count


def make_num_odd(num):
    count_ = 0
    if num&1 == 1:
        # making odd to even 
        while num & 1 == 1:
            num = int(num / 2)
            count_ += 1
    else:
        # making even to odd
        while num & 1 != 1:
            num = int(num / 2)
            count_ += 1
    return count_, num
def get_minimum_operation(items_count, items):
    operation_count = 0
    for i in range(len(items) - 1):
        print(items[i], items[i + 1], items[i] % 2 , items[i + 1] % 2)
        if items[i] % 2 != items[i + 1] % 2:
            continue
        count_, num = make_num_odd(items[i + 1])
        operation_count += count_
        items[i + 1] = num
    print(items)
    return operation_count



items = [4, 10, 10, 6, 2]
items = [6, 5, 9, 7, 3]
items = [4, 10, 10, 6, 3]
print(get_minimum_operation(0, items))