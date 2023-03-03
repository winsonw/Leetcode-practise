from heapq import heappush, heappop
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # [print(line) for line in grid]  
        if grid[0][1] > 1 and grid[1][0] >1 :
            return -1
        m, n = len(grid), len(grid[0])
        visited = [[-1]* n for i in range(m)] 
        visited[0][0] = 0
        
        openList = []
        heappush(openList, (0, [0,0]))
        
        
        while openList:
            t, cord = heappop(openList)
            t += 1
            for dirs in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x, y  = cord[0] + dirs[0], cord[1] + dirs[1]
                # print(x,y)
                if 0 <= x < m and 0 <= y < n:
                    arrive = t
                    if grid[x][y] > t:
                        arrive += 2*math.ceil((grid[x][y] - t)/2)
                        
                    if visited[x][y] == -1 or visited[x][y] > arrive:
                        visited[x][y] = arrive
                        heappush(openList, (arrive, [x,y]))
                        # [print(line) for line in visited]
                        # print(openList)
                        
                        
        # print()
        # [print(line) for line in visited]
        
        return visited[m-1][n-1]