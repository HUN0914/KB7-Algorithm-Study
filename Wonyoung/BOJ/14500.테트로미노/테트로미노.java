import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static int N, M, answer;
    public static int[][] grid;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        grid = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] stick = {{0, 0}, {0, 1}, {0, 2}, {0, 3}};
        int[][] rectangle = {{0, 0}, {0, 1}, {1, 0}, {1, 1}};
        int[][] tBlock = {{0, 0}, {0, 1}, {0, 2}, {1, 1}};
        int[][] zBlock = {{0, 0}, {1, 0}, {1, 1}, {2, 1}};
        int[][] lBlock = {{0, 0}, {1, 0}, {2, 0}, {2, 1}};

        // 이거 뭔데!!!!!!!!!!!!
        int[][] zBlockSymmetry = {{0, 0}, {1, 0}, {1, -1}, {2, -1}};
        int[][] lBlockSymmetry = {{0, 0}, {1, 0}, {2, 0}, {2, -1}};
        // 이거 뭔데!!!!!!!!!!!!

        List<int[][]> blocks = new ArrayList<>(Arrays.asList(stick, rectangle, tBlock, zBlock, zBlockSymmetry, lBlock, lBlockSymmetry));

        for (int[][] block : blocks) tetromino(block);
        System.out.println(answer);
    }

    public static void tetromino(int[][] block) {
        for (int k = 0; k < 4; k++) {
            // 1. 값 비교를 하고
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    answer = Math.max(answer, calcPoint(block, i, j));
                }
            }
            // 2. 돌리기
            block = rotateBlock(block);
        }
    }

    public static int calcPoint(int[][] block, int x, int y) {
        int cnt = 0;
        for (int[] point : block) {
            int nr = x + point[0], nc = y + point[1];
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) return 0;
            cnt += grid[nr][nc];
        }
        return cnt;
    }

    public static int[][] rotateBlock(int[][] block) {
        int[][] newBlock = new int[4][2];
        int r1 = 0, c1 = 0;

        for (int i = 0; i < 4; i++) {
            int r2 = block[i][0], c2 = block[i][1];
            int rr = r1 + c2 - c1, cc = c1 + r1 - r2;
            newBlock[i][0] = rr;
            newBlock[i][1] = cc;
        }
        return newBlock;
    }
}
