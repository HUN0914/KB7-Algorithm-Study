import java.util.*;

class Solution {
    static int n, m;
    static char[][] board;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public int solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        board = new char[n][m];

        int sr = 0, sc = 0;
        int lr = 0, lc = 0;

        for (int r = 0; r < n; r++) {
            board[r] = maps[r].toCharArray();

            for (int c = 0; c < m; c++) {
                if (board[r][c] == 'S') {
                    sr = r;
                    sc = c;
                } else if (board[r][c] == 'L') {
                    lr = r;
                    lc = c;
                }
            }
        }

        int toLever = bfs(sr, sc, 'L');
        if (toLever == -1) return -1;

        int toExit = bfs(lr, lc, 'E');
        if (toExit == -1) return -1;

        return toLever + toExit;
    }

    private int bfs(int startR, int startC, char target) {
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> q = new ArrayDeque<>();

        q.offer(new int[]{startR, startC, 0});
        visited[startR][startC] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0];
            int c = cur[1];
            int dist = cur[2];

            if (board[r][c] == target) return dist;

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                if (visited[nr][nc]) continue;
                if (board[nr][nc] == 'X') continue;

                visited[nr][nc] = true;
                q.offer(new int[]{nr, nc, dist + 1});
            }
        }

        return -1;
    }
}