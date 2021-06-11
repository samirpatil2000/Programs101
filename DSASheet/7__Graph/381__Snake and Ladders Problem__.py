from typing import List
import collections
class Solution:
    def findCordinate(self,num,n):
        r, c = divmod(num-1, n)
        if r % 2 == 0:
            return n-1-r, c
        else:
            return n-1-r, n-1-c
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)            
        seen = set()
        queue = collections.deque()
        queue.append((1, 0))
        while queue:
            label, step = queue.popleft()
            r, c = self.findCordinate(label,n)
            if board[r][c] != -1:
                label = board[r][c]
            if label == n*n:
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n*n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step+1))
        return -1
    
sol=Solution()
board=[
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]
    ]
print(sol.snakesAndLadders(board))                    
                    
            
            