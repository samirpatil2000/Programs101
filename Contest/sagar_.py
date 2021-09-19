# s=input()
# n=int(input())

def fun(N,s):
    A=B=0
    for i in s:
        if A==N-1:
            return "Team A Won"
        if B==N-1:
            return "Team B Won"
        if i=="a":
            A+=1
        else:
            B+=1
    if A>B:
        return "Team A Won"
    return "Team B Won"

n,s=5,"aaaabbabb"
print(fun(n,s))

