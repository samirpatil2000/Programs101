#User function Template for python3
# import heapq


class Solution:
    def sortedMatrix(self, N, mat):
        import heapq
        arr = []
        heapq.heapify(arr)
        for i in range(N):
            for j in range(N):
                heapq.heappush(arr, mat[i][j])
    
        result = []
        i = 0 
        while i < (N):
            row = []
            for _ in range(N):
                row.append(heapq.heappop(arr))
            i += 1
            result.append(row)
        return result
    

sol = Solution()
N=4
Mat=[[10,20,30,40],
[15,25,35,45],
[27,29,37,48] ,
[32,33,39,50]]
print(sol.sortedMatrix(N,Mat))
print(*[3, 4, 6, 7])