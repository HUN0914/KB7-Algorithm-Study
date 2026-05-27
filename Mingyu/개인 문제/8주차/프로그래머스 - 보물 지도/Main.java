import java.util.*;

class Solution {
    static class Node {
        int x;
        int y;
        int time;
        int used;

        Node(int x, int y, int time, int used) {
            this.x = x;
            this.y = y;
            this.time = time;
            this.used = used;
        }
    }

    public int solution(int n, int m, int[][] hole) {
        boolean[][] trap = new boolean[n + 1][m + 1];
        for (int[] h : hole) {
            int x = h[0];
            int y = h[1];
            trap[x][y] = true;
        }

        boolean[][][] visited = new boolean[n + 1][m + 1][2];
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        Queue<Node> q = new ArrayDeque<>();

        q.offer(new Node(1, 1, 0, 0));
        visited[1][1][0] = true;

        while (!q.isEmpty()) {
            Node cur = q.poll();
            
            if (cur.x == n && cur.y == m) return cur.time;

            for (int d = 0; d < 4; d++) {

                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];

                if (isInRange(nx, ny, n, m) && !trap[nx][ny] && !visited[nx][ny][cur.used]) {
                    visited[nx][ny][cur.used] = true;
                    q.offer(new Node(nx, ny, cur.time + 1, cur.used));
                }

                if (cur.used == 0) {
                    int jumpX = cur.x + dx[d] * 2;
                    int jumpY = cur.y + dy[d] * 2;
                    
                    if (isInRange(jumpX, jumpY, n, m) && !trap[jumpX][jumpY] && !visited[jumpX][jumpY][1]) {
                        visited[jumpX][jumpY][1] = true;
                        q.offer(new Node(jumpX, jumpY, cur.time + 1, 1));
                    }
                }
            }
        }

        return -1;
    }

    private boolean isInRange(int x, int y, int n, int m) {
        return x >= 1 && x <= n && y >= 1 && y <= m;
    }
}