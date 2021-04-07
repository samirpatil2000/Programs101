
def searchWord(s):
    word="hackerrank"
    i=0
    j=0
    while(i<len(word) and j<len(s)):
        if(s[j]==word[i]):
            i+=1
            j+=1
        else:
            j+=1
    if(len(word)==i):
        return "YES"
    return "NO"

s="rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"
print(searchWord(s))
    