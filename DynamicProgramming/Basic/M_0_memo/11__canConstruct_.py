def canConstruct(target_string,wordBank,memo={}):
    if target_string=="":
        return True
    if target_string in memo:
        return memo[target_string]
    if target_string in wordBank:
        return True
    print(target_string)
    for i in range(1,len(target_string)+1):
        
        if target_string[:i] in wordBank:
            if canConstruct(target_string[i:],wordBank,memo):
                memo[target_string]=True
                return True
    memo[target_string]=False
    return False
        
        
target_string="abcdef"
words=['ab','abc','cd','def','abcd']

target_string="eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
words=['e','ee','eee','eeee','eeeee','eeeeee']
# print(target_string[1:])
print(canConstruct(target_string,set(words)))
    
    