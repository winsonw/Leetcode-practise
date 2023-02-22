class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        n = l //2 
        if l % 2 != 0:
            n+=1
        t = 0
        l -= 1
        
        for i in range(n):
            for j in range((l+1)//2):
                x = i
                y = j
                t = matrix[l-y][x]
                for k in range(4):
                    t,matrix[x][y] = (matrix[x][y], t)
                    x,y = (y,l-x)
                