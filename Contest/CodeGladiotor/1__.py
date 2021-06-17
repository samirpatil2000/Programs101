# def main():

def dectector(V:str,B:str) -> bool:
    j=0
    for i in range(len(B)):
        while j<len(V):
            if V[j]==B[i]:
                j+=1
                break
            else:
                j+=1
        if j==len(V) and i!=len(B)-1:return "NEGATIVE"
    return "POSITIVE"

def main():
    V=input()
    t=int(input())
    while t:
        t-=1
        B=input()
        print(dectector(V,B))
        
        
    

V="coronavirus"
B="abcde"
B="crnas"
B="onarous"


# print(dectector(V,B))
main()
        
    
    