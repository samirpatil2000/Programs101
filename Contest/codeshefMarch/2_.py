import sys
from sys import stdin,stdout


t=int(stdin.readline())

def get_string(): return sys.stdin.readline().strip()

for _ in range(t):

    string = get_string()
    def findPair(string):
        n=len(string)
        count=0
        i=0
        while(i<n):
            if(string[i]=='1'):
                count+=1
                while(i<n and string[i]=='1'):
                    i+=1
            i+=1
        return count
    
    print(findPair(string))
