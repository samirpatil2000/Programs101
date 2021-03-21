

def checkPalindrome(s,left,right):
    count=0
    s=s[left:right+1]
    frequencies = {} 
    for char in s: 
        if char in frequencies: 
            frequencies[char] += 1
        else: 
            frequencies[char] = 1
                        
    for v in frequencies.values():
        if(v%2!=0):
            count+=1
    if((right+1-left)%2!=0):
        count-=1
    count=count//2
    return count        
        
s="abcda"



def canMakePaliQueries(s, queries):
    bool_list=[]
    for i in queries:
        print(checkPalindrome(s,i[0],i[1]),i[2])
        if(checkPalindrome(s,i[0],i[1])-i[2]<=0):
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list

queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
print(canMakePaliQueries(s,queries))

# print(checkPalindrome(s,0,3))

        
    
