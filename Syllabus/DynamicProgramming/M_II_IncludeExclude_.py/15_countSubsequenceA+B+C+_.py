

def countSubsequence(string):
    a=0
    ab=0
    abc=0
    
    for i in range(len(string)):
        if string[i]=='a':
            a=a+a+1
        elif string[i]=='b':
            ab=ab+ab+a
        elif string[i]=='c':
            abc=abc+abc+ab
            
    return abc
    