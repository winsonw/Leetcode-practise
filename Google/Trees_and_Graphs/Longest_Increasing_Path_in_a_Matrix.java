class Solution {
    public static final int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[][] cache = new int[m][n];
        int maximum = 1;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                dfs(i, j, matrix, cache);
                maximum = Math.max(maximum, cache[i][j]);
            }
        }
        // for (int[] line:cache){
        //     for (int num:line){
        //         System.out.print(num+" ");
        //     }
        //     System.out.println();
        // }
        return maximum;
    }
    
    private int dfs(int x, int y, int[][] matrix, int[][] cache){
        if (cache[x][y] != 0) {
            return cache[x][y];
        }
        int current_max = 1;
        for (int[] dir:dirs){
            int new_x = x+dir[0], new_y = y+dir[1];
            if (!(new_x < 0 || new_y < 0 || new_x>= matrix.length || new_y>= matrix[0].length)){
                if (matrix[new_x][new_y] > matrix[x][y]){
                    current_max = Math.max(current_max, 1 + dfs(new_x, new_y, matrix, cache));
                }
            }
        }
        cache[x][y] = current_max;
        return current_max;
    }
}