

def memLeak(memory1: int, memory2: int):
    i=1
    while i:
        print(memory1,memory2,i)
        if i<=max(memory2,memory1):
            if memory2>memory1:
                memory2-=i
            else:
                memory1-=i
            i+=1
        else:
            return [i,memory1,memory2]
    return [i,memory1,memory2]


print(memLeak(8,11))
    