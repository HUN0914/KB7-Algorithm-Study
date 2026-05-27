class Solution {
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        StringBuilder sb = new StringBuilder();

        char[] dirChar = {'d', 'l', 'r', 'u'};
        int[] dx = {1, 0, 0, -1};
        int[] dy = {0, -1, 1, 0};

        int minDist = dist(x, y, r, c);

        if (minDist > k) return "impossible";

        if ((k - minDist) % 2 == 1) return "impossible";

        int curX = x;
        int curY = y;

        for (int step = 0; step < k; step++) {
            for (int i = 0; i < 4; i++) {
                int nx = curX + dx[i];
                int ny = curY + dy[i];

                if (nx < 1 || nx > n || ny < 1 || ny > m) continue;

                int rem = k - step - 1;
                int nextDist = dist(nx, ny, r, c);

                if (nextDist <= rem && (rem - nextDist) % 2 == 0) {
                    sb.append(dirChar[i]);

                    curX = nx;
                    curY = ny;

                    break;
                }
            }
        }

        return sb.toString();
    }

    private int dist(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }
}