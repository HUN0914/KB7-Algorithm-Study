public class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        int[] dr = {1, 1, 0, -1, -1, -1, 0, 1};
        int[] dc = {0, 1, 1, 1, 0, -1, -1, -1};

        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;

        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0});
        grid[0][0] = 1;

        while (!q.isEmpty()) {
            int[] node = q.poll();
            int r = node[0];
            int c = node[1];
            int dist = grid[r][c];

            if (r == n - 1 && c == n - 1) return dist;

            for (int d = 0; d < 8; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr >= 0 && nc >= 0 && nr < n && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = dist + 1;
                    q.offer(new int[]{nr, nc});
                }
            }
        }

        return -1;
    }
}