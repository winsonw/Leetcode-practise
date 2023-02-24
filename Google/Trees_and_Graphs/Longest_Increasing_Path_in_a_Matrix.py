class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        
        def dfs(x, y, last):
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > last:
                if visited[x][y] == 0: 
                    data = list(map(dfs, (x+1, x-1, x, x), (y, y, y+1, y-1), [matrix[x][y]]*4 ))
                    visited[x][y] = 1 + max(data)
                return visited[x][y]
                
            return 0
        
        
        return max([max([dfs(i,j, -1) for j in range(n)]) for i in range(m)])