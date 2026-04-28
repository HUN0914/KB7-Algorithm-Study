import java.io.*;
import java.util.*;

public class Main {
    static class Knight {
        int r, c, h, w;
        int nowHp;
        int originHp;

        Knight(int r, int c, int h, int w, int hp) {
            this.r = r;
            this.c = c;
            this.h = h;
            this.w = w;
            this.nowHp = hp;
            this.originHp = hp;
        }

        boolean isAlive() {
            return nowHp > 0;
        }
    }

    static int L, N, Q;
    static int[][] board; // 0: blank, 1: trap, 2: wall
    static Knight[] knights;

    // 0: up, 1: right, 2: down, 3: left
    // (ex) dr[0], dc[0]: move ↑
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        // initializing board, placing traps and walls
        board = new int[L + 1][L + 1];
        for (int r = 1; r <= L; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 1; c <= L; c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        // placing knights
        knights = new Knight[N + 1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            knights[i] = new Knight(r, c, h, w, k);
        }

        // execute commands
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            tryMove(idx, d);
        }

        // calculate sum of damage
        int answer = 0;
        for (int i = 1; i <= N; i++) {
            if (knights[i].isAlive()) {
                answer += knights[i].originHp - knights[i].nowHp;
            }

        }

        System.out.println(answer);
    }

    static void tryMove(int idx, int d) {
        if (!knights[idx].isAlive()) return; // dead knight cannot move

        // init BFS
        boolean[] pushed = new boolean[N + 1];
        Queue<Integer> q = new ArrayDeque<>();
        pushed[idx] = true;
        q.offer(idx);

        while (!q.isEmpty()) {
            int cur = q.poll();
            Knight now = knights[cur];
            if (!canIMove(now, d)) return;

            int nr = now.r + dr[d];
            int nc = now.c + dc[d];

            for (int next = 1; next <= N; next++) {
                if (pushed[next]) continue;
                if (!knights[next].isAlive()) continue;
                if (isOverlap(nr, nc, now.h, now.w, knights[next])) {
                    pushed[next] = true;
                    q.offer(next);
                }
            }
        }

        // move all knights at the same time
        for (int i = 1; i <= N; i++) {
            if (pushed[i]) {
                knights[i].r += dr[d];
                knights[i].c += dc[d];
            }
        }

        // only pushed knights take damage, moved knight is immune
        for (int i = 1; i <= N; i++) {
            if (pushed[i] && i != idx && knights[i].isAlive()) {
                int damage = trappedCnt(knights[i]);
                knights[i].nowHp -= damage;
            }
        }
    }

    static boolean canIMove(Knight k, int d) {
        int nr = k.r + dr[d];
        int nc = k.c + dc[d];

        for (int r = nr; r < nr + k.h; r++) {
            for (int c = nc; c < nc + k.w; c++) {
                if (r < 1 || r > L || c < 1 || c > L) return false; // out of board
                if (board[r][c] == 2) return false; // wall
            }
        }

        return true;
    }

    static boolean isOverlap(int ar, int ac, int ah, int aw, Knight b) {
        // Knight A's new position
        int ar1 = ar;
        int ac1 = ac;
        int ar2 = ar + ah - 1;
        int ac2 = ac + aw - 1;

        // Knight B's position
        int br1 = b.r;
        int bc1 = b.c;
        int br2 = b.r + b.h - 1;
        int bc2 = b.c + b.w - 1;

        return (ar1 <= br2) && (br1 <= ar2) && (ac1 <= bc2) && (bc1 <= ac2); // row overlapped && column overlapped T/F
    }

    static int trappedCnt(Knight k) {
        int cnt = 0;

        for (int r = k.r; r < k.r + k.h; r++) {
            for (int c = k.c; c < k.c + k.w; c++) {
                if (board[r][c] == 1) { // trap
                    cnt++;
                }
            }
        }

        return cnt;
    }
}