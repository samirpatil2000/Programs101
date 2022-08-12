from typing import List


class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        import collections
        init_color = image[sr][sc]
        queue = collections.deque()
        queue.append([sr, sc])
        while queue:
            temp = queue.popleft()
            print(queue)
            if image[temp[0]][temp[1]] == color:
                continue
            image[temp[0]][temp[1]] = color
            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i in range(4):
                nr = sr + dir[i][0]
                nc = sc + dir[i][1]
                if nr < 0 or nc < 0:
                    continue
                elif nr >= len(image) or nc >= len(image[0]):
                    continue
                elif image[nr][nc] == color or image[nr][nc] != init_color:
                    continue
                queue.append([nr, nc, image[nr][nc]])
                print(queue, sr, sc)
            
        return image
                     
                
        
            
sol = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(sol.floodFill(image, sr, sc, color))
        