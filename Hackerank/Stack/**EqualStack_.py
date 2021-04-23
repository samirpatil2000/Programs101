# https://www.hackerrank.com/challenges/equal-stacks/problem
def equalStack(h1,h2,h3):
    s1,s2,s3=sum(h1),sum(h2),sum(h3)
    while h1 or h2 or h3:
        min_=min(s1,s2,s3)
        while s1>min_:
            s1-=h1.pop(0)
        while s2>min_:
            s2-=h2.pop(0)
        while s3 > min_:
            s3-=h3.pop(0)
        if s1==s2==s3:
            return s1
    return 0
    
h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]
print(equalStack(h1,h2,h3))
        
            
        
    