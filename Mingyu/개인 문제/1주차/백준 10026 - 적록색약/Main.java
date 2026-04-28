import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static char[][] grid;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());
        grid = new char[n][n];
        for (int i = 0; i < n; i++) {
            grid[i] = br.readLine().toCharArray();
        }

        boolean isBlind = false;
        for (int k = 0; k < 2; k++) {
            boolean[][] visited = new boolean[n][n];
            int cnt = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (visited[i][j]) continue;

                    bfs(i, j, visited, isBlind);
                    cnt++;
                }
            }

            sb.append(cnt);
            if (k == 0) sb.append(" ");

            isBlind = !isBlind;
        }

        System.out.println(sb);
    }

    static void bfs(int sr, int sc, boolean[][] vis, boolean isBlind) {
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{sr, sc});
        vis[sr][sc] = true;

        char startColor = grid[sr][sc];

        while (!q.isEmpty()) {
            int[] cur = q.poll();

            for (int d = 0; d < 4; d++) {
                int nr = cur[0] + dr[d];
                int nc = cur[1] + dc[d];

                if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                if (vis[nr][nc]) continue;
                if (!isSame(startColor, grid[nr][nc], isBlind)) continue; // not same color - > skip

                vis[nr][nc] = true;
                q.offer(new int[]{nr, nc});
            }
        }
    }

    static boolean isSame(char c1, char c2, boolean isBlind) {
        if (!isBlind) return c1 == c2; // normal person, c1 == c2 -> true, else false
        if (c1 == 'B' || c2 == 'B') return c1 == c2; // blind person, c1 == c2 == blue -> true
        return true; // blind person, red and green are same -> true
    }
}