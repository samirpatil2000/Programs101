

def game(s):
    dict_={}
    for ch in s:
        if ch in dict_:
            dict_[ch]+=1
        else:
            dict_[ch]=1
    
    
    odd_count=0
    for value in dict_.values():
        if value%2!=0 and odd_count==1:
            return print("No")
        elif value%2!=0 and odd_count==0:
            odd_count+=1
    
    return print("Yes")



s="cdcdcdcdeeeef"
game(s) 