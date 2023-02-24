class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        count = 0 
        def remove_attached_land(row,col):
            if 0 <= row < n and 0 <= col < m and grid[row][col] == "1":
                grid[row][col] = '0'
                # map(remove_attached_land, [row, row, row-1, row+1], [col-1, col+1, col, col])
                remove_attached_land(row, col+1)
                remove_attached_land(row, col-1)
                remove_attached_land(row+1, col)
                remove_attached_land(row-1, col)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    remove_attached_land(i, j)
        return count

                        
                    
                    
                        
                        