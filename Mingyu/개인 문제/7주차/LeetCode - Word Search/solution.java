class Solution {
    int rows, cols;
    char[][] board;
    String word;

    int[] dr = {-1, 0, 1, 0};
    int[] dc = {0, 1, 0, -1};

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.word = word;
        this.rows = board.length;
        this.cols = board[0].length;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == word.charAt(0)) {
                    if (dfs(r, c, 0)) return true;
                }
            }
        }

        return false;
    }

    private boolean dfs(int r, int c, int idx) {
        if (idx == word.length()) return true;

        if (r < 0 || r >= rows || c < 0 || c >= cols) return false;

        if (board[r][c] != word.charAt(idx)) return false;

        char temp = board[r][c];
        board[r][c] = '#';

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (dfs(nr, nc, idx + 1)) return true;
        }

        board[r][c] = temp;

        return false;
    }
}