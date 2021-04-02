
def nextGreatestLetter(letters,target):
    i=0
    # cout=0
    while(i<len(letters) and ord(target)>=ord(letters[i])):
        i+=1
    if(i==len(letters)):
        return ord(letters[i-1])-ord("a"),letters[i-1]
    return ord(letters[i])-ord("a"),letters[i]


letters = ["c", "f", "j"]
target = "k"

# print(ord(target)-ord("a"))
print([ord(i)-ord("a") for i in letters],ord(target)-ord("a"))
print(nextGreatestLetter(letters,target))
