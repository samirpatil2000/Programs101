def bigSorting(unsorted):
    sort_=[int(i) for i in unsorted]
    sort_.sort()
    
    return sort_


arr=['1','2','3084193741082938','308419374108293812303479849857341718340192371','100','200','3084193741082937','111']

print(bigSorting(arr))

