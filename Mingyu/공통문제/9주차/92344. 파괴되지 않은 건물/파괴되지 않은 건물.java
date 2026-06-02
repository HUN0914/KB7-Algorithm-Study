class Solution {
    public int solution(int[][] board, int[][] skill) {
        int n = board.length;
        int m = board[0].length;
        
        // save damage of each cell (board[i][j] += damage[i][j])
        int[][] damage = new int[n + 1][m + 1];

        for (int[] s : skill) {
            int r1 = s[1];
            int c1 = s[2];
            int r2 = s[3];
            int c2 = s[4];
            int degree = s[5];
            
            // type -> s[0] == 1: damage (-degree -> -s[5])
            // type -> s[0] == 2: heal (degree -> s[5])
            int value = (s[0] == 1) ? -s[5] : s[5];

            damage[r1][c1] += value; // start point of damage applied
            damage[r1][c2 + 1] -= value; // end point of damage applied (column)
            damage[r2 + 1][c1] -= value; // end point of damage applied (row)
            damage[r2 + 1][c2 + 1] += value; // adjust because end point applied twice
        }

        // apply damage to row direction
        for (int r = 0; r <= n; r++) {
            for (int c = 1; c <= m; c++) {
                damage[r][c] += damage[r][c - 1];
            }
        }

        // apply damage to column direction
        for (int c = 0; c <= m; c++) {
            for (int r = 1; r <= n; r++) {
                damage[r][c] += damage[r - 1][c];
            }
        }

        int answer = 0;

        // sum of survived buildings
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (board[r][c] + damage[r][c] > 0) answer++;
            }
        }

        return answer;
    }
}