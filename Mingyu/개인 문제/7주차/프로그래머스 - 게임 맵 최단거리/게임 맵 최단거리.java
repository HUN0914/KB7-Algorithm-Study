import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};

        if (maps[0][0] == 0 || maps[n - 1][m - 1] == 0) return -1;

        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0});
        maps[0][0] = 1;

        while (!q.isEmpty()) {
            int[] node = q.poll();
            int r = node[0];
            int c = node[1];
            int dist = maps[r][c];

            if (r == n - 1 && c == m - 1) return dist;

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr >= 0 && nc >= 0 && nr < n && nc < m && maps[nr][nc] == 1) {
                    maps[nr][nc] = dist + 1;
                    q.offer(new int[]{nr, nc});
                }
            }
        }

        return -1;
    }
}