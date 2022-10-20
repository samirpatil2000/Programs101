def canConstruct(target_string,wordBank,memo={}):
    if target_string=="":
        return 1
    if target_string in memo:return memo[target_string]
    if target_string in wordBank:
        memo[target_string]=1
        return 1
    print(target_string)
    count_=0
    for i in range(1,len(target_string)+1):     
        if target_string[:i] in wordBank:
            count_+=canConstruct(target_string[i:],wordBank,memo)
    memo[target_string]=count_
    return count_
        
        
target_string="abcdef"
words=['ab','abc','cd','def','abcd']

target_string="eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
words=['e','ee','eee','eeee','eeeee','eeeeee']


target_string="purple"
words=['purp','p','ur','le','purpl']
print(canConstruct(target_string,set(words)))
    
    