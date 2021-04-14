
def maxPiles(piles):
    piles.sort()
    print(piles)
    right=len(piles)-1-2
    while(0<right):
        temp=piles[0]
        curr_left=0
        while(curr_left<right):
            piles[curr_left]=piles[curr_left+1]
            curr_left+=1
        piles[right]=temp
        right-=3
        print(piles)
    sum_=0
    i=1
    while(i<len(piles)):
        sum_+=piles[i]
        i+=3
    return sum_



def maxPiles_Opt(piles):
    piles.sort()
    right=len(piles)-1-1
    left=0
    sum_=0
    while(left<right):
        sum_+=piles[right]
        left+=1
        right-=2
    return sum_


piles = [9,8,7,6,5,1,2,3,4]
print(maxPiles_Opt(piles))