



def paintFence(n,k):
    last2_same=k
    last2_diff=k*(k-1)
    total_=last2_diff+last2_same
    for i in range(3,n+1):
        print(last2_same,last2_diff,total_)
        # temp_last2_same=last2_same
        # temp_last2_diff=last2_diff
        # temp_total_=total_
        last2_same=last2_diff
        last2_diff=total_*(k-1)
        total_=last2_same+last2_diff
        
    return total_

print(paintFence(5,3))

    