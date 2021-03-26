

import time


def maxDepth(s):
    st=[]
    i=0
    max_depth=0
    while(i<len(s)):
        if(s[i]=='('):
            st.append(s[i])
            if(max_depth < len(s)):
                max_depth=len(s)
        elif(s[i]==')'):
            st.pop()
        i+=1
    return max_depth


s = "1+(2*3)/(2-1)"


start = time.time()
time.sleep(1)
print(maxDepth(s))
end = time.time()
print(end-start-1)
    