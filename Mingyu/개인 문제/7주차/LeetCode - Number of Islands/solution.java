public class Solution {
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public int numIslands(char[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int islands = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    islands++;
                }
            }
        }

        return islands;
    }

    private void dfs(char[][] grid, int r, int c) {
        int row = grid.length;
        int col = grid[0].length;

        if (r < 0 || r >= row || c < 0 || c >= col) return;
        if (grid[r][c] == '0') return;

        grid[r][c] = '0';

        for (int d = 0; d < 4; d++) {
            dfs(grid, r + dr[d], c + dc[d]);
        }
    }
}