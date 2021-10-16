def maxNormalSubstring(P, Q, K):
     
    if (K == 0):
        return 0
    
    N=len(P)
   
    count = 0
   

    left, right = 0, 0

    ans = 0
   
    while (right < N):
   
        while (right < N and count <= K):
   
            pos = ord(P[right]) - ord('a')

            if (Q[pos] == '0'):
   
                if (count + 1 > K):
                    break
                else:
                    count += 1
   
            right += 1
   
            # update answer with substring length
            if (count <= K):
                ans = max(ans, right - left)
   
        while (left < right):
   
            # get position of character
            pos = ord(P[left]) - ord('a')
   
            left += 1
   
            # check if character is
            # normal then decrement count
            if (Q[pos] == '0'):
                count -= 1
   
            if (count < K):
                break
   
    return ans
P = "giraffe"
Q = "01111001111111111011111111"

K = 2


print(maxNormalSubstring(P,Q,K))