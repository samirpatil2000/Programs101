def nonrepeating(n):
    nor = {}
    i = 0
    while i < len(n) and n[i] not in nor:
        nor.add(n[i])
        i += 1
    
        
    while i < len(n):
        
        