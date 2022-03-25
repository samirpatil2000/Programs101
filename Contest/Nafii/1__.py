def fun(samDaily, keilyDaily, diff):
    days = 1
    samSolved = samDaily + diff
    keilySolved = keilyDaily
    if diff == 0:
        if samDaily == keilyDaily:
            return -1
    
    if samDaily > keilyDaily:
        return -1
    if samSolved < keilySolved:
        return days
    while samSolved >= keilySolved:
        samSolved += samDaily
        keilySolved += keilyDaily
        days += 1
        if samSolved < keilySolved:
            return days
    return -1
    
list_ = [3, 5, 5]
# list_ = [3, 5, 1]
list_ = [100, 100, 0]
print(fun(*list_))