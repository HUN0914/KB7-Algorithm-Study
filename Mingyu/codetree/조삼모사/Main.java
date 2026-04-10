import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] map;
    static boolean[] selected;
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        selected = new boolean[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0, 0);
        System.out.println(ans);
    }

    static void dfs(int depth, int start) {
        // if N/2 tasks done in A.M.
        if (depth == N / 2) {
            calcDiff();
            return;
        }

        // making combination
        for (int i = start; i < N; i++) {
            selected[i] = true;
            dfs(depth + 1, i + 1);
            selected[i] = false;
        }
    }

    static void calcDiff() {
        int amDiff = 0;
        int pmDiff = 0;

        // only i < j case
        for (int i = 0; i < N - 1; i++) {
            for (int j = i + 1; j < N; j++) {
                if (selected[i] && selected[j]) { // task of A.M.
                    amDiff += map[i][j] + map[j][i];
                } else if (!selected[i] && !selected[j]) { // task of P.M.
                    pmDiff += map[i][j] + map[j][i];
                }
            }
        }

        ans = Math.min(ans, Math.abs(amDiff - pmDiff));
    }
}

