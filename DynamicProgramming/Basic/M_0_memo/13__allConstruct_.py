import collections

def allConstruct(target_string,words,memo={}):
    if target_string=="":
        return [collections.deque([])]
    if target_string in memo:return memo[target_string]
   
    
    result=[]
    for i in range(1,len(target_string)+1):
        
        if target_string[:i] in words:
            
            all_of_ways = allConstruct(target_string[i:],words,memo)
            
            # print(all_of_ways)
            
            for li in all_of_ways:
                li.appendleft(target_string[:i])
                
                result.append(li)
    # memo[target_string]=result
    return result

    
        
            
target_string="abcdef"
words=['ab','abc','cd','def','abcd','ef']

# target_string="eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
# words=['e','ee','eee','eeee','eeeee','eeeeee']


# target_string="purple"
# words=['purp','p','ur','le','purpl']

x=allConstruct(target_string,words)
# for i in x:i.reverse()
print(x)