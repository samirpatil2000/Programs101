def bitMask(n):
    rmsb_=n&-n
    print(bin(n),bin(-n))
    print(bin(rmsb_))
    return

bitMask(76)

print(1 << 1)