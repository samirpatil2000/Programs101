import math, time
class Solution:
    
    def find_prime_in_range(self, M, N):
        is_prime = [True for i in range(N + 1)]
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(math.sqrt(N)) + 1):
            if is_prime[i] == True:
                for j in range(i * i, N + 1, i):    
                    is_prime[j] = False
        return [index for index in range(M, N + 1) if is_prime[index]]
M=2
N=5
t1 = time.time()
print(Solution().find_prime_in_range(M, N))
print("Total Time: ", time.time() - t1)