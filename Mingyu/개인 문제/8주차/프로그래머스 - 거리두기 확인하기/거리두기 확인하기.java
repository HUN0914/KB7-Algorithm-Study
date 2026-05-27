import java.util.*;

class Solution {
    int[] dr = {-1, 0, 1, 0};
    int[] dc = {0, 1, 0, -1};

    public int[] solution(String[][] places) {
        int[] answer = new int[5];

        for (int i = 0; i < 5; i++) {
            answer[i] = isOk(places[i]) ? 1 : 0;
        }

        return answer;
    }

    private boolean isOk(String[] place) {
        for (int r = 0; r < 5; r++) {
            for (int c = 0; c < 5; c++) {
                if (place[r].charAt(c) == 'P') {
                    if (!bfs(place, r, c)) return false;
                }
            }
        }
        
        return true;
    }

    private boolean bfs(String[] place, int startR, int startC) {
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[5][5];

        q.offer(new int[]{startR, startC, 0});
        visited[startR][startC] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();

            int r = cur[0];
            int c = cur[1];
            int dist = cur[2];

            if (dist == 2) continue;

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                int nd = dist + 1;
                
                if (nr < 0 || nr >= 5 || nc < 0 || nc >= 5) continue;

                if (visited[nr][nc]) continue;

                char next = place[nr].charAt(nc);

                if (next == 'X') continue;

                if (next == 'P') return false;

                visited[nr][nc] = true;
                q.offer(new int[]{nr, nc, nd});
            }
        }

        return true;
    }
}