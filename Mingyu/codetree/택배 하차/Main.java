import java.io.*;
import java.util.*;

public class Main {
    // Box Object 
    static class Box {
        int k, h, w, r, c;
        boolean removed;

        Box(int k, int h, int w, int r, int c) {
            this.k = k;
            this.h = h;
            this.w = w;
            this.r = r;
            this.c = c;
            this.removed = false;
        }
    }

    static int N, M;
    static int[][] board;
    static Map<Integer, Box> boxes = new HashMap<>(); // list of boxes
    static List<Integer> ids = new ArrayList<>(); // list of number of boxes
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N][N];

        // initialize boxes and put into board
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken()) - 1; // column: 1-indexed -> 0-indexed

            Box box = new Box(k, h, w, 0, c); // start (0, c), top of board
            boxes.put(k, box);
            ids.add(k);

            fallAndPlace(k);
        }

        // remove left / right and fall boxes
        for (int i = 0; i < M; i += 2) {
            removeLeft();
            fallAll();

            removeRight();
            fallAll();
        }

        System.out.print(sb);
    }

    // set box into board
    static void setBox(int id) {
        Box b = boxes.get(id);
        for (int i = b.r; i < b.r + b.h; i++) {
            for (int j = b.c; j < b.c + b.w; j++) {
                board[i][j] = id;
            }
        }
    }

    // remove box from board
    static void clearBox(int id) {
        Box b = boxes.get(id);
        for (int i = b.r; i < b.r + b.h; i++) {
            for (int j = b.c; j < b.c + b.w; j++) {
                board[i][j] = 0;
            }
        }
    }

    // fall boxes and place to new position
    static void fallAndPlace(int id) {
        Box b = boxes.get(id);

        while (canFitAt(b.r + 1, b.c, b.h, b.w)) {
            b.r++;
        }
        setBox(id);
    }

    // check whether or not we can place h * w box to (nr, nc)
    static boolean canFitAt(int nr, int nc, int h, int w) {
        if (nr < 0 || nc < 0 || nr + h > N || nc + w > N) return false;

        for (int i = nr; i < nr + h; i++) {
            for (int j = nc; j < nc + w; j++) {
                if (board[i][j] != 0) return false;
            }
        }
        return true;
    }

    // apply gravity to all boxes
    static void fallAll() {
        boolean moved;
        do {
            moved = false;
            for (int id : ids) {
                Box b = boxes.get(id);
                if (b.removed) continue;

                clearBox(id);
                int oldR = b.r;
                while (canFitAt(b.r + 1, b.c, b.h, b.w)) {
                    b.r++;
                }
                setBox(id);

                if (b.r != oldR) moved = true;
            }
        } while (moved);
    }

    static boolean canExitLeft(int id) {
        Box b = boxes.get(id);
        if (b.removed) return false;

        for (int i = b.r; i < b.r + b.h; i++) {
            for (int j = 0; j < b.c; j++) {
                if (board[i][j] != 0) return false;
            }
        }
        return true;
    }

    static boolean canExitRight(int id) {
        Box b = boxes.get(id);
        if (b.removed) return false;

        for (int i = b.r; i < b.r + b.h; i++) {
            for (int j = b.c + b.w; j < N; j++) {
                if (board[i][j] != 0) return false;
            }
        }
        return true;
    }

    static void removeLeft() {
        int target = Integer.MAX_VALUE;

        for (int id : ids) {
            Box b = boxes.get(id);
            if (!b.removed && canExitLeft(id)) {
                target = Math.min(target, id);
            }
        }

        if (target != Integer.MAX_VALUE) { // find box to remove
            removeBox(target);
        }
    }

    static void removeRight() {
        int target = Integer.MAX_VALUE;

        for (int id : ids) {
            Box b = boxes.get(id);
            if (!b.removed && canExitRight(id)) {
                target = Math.min(target, id);
            }
        }

        if (target != Integer.MAX_VALUE) { // find box to remove
            removeBox(target);
        }
    }

    static void removeBox(int id) {
        Box b = boxes.get(id);
        clearBox(id);
        b.removed = true;
        sb.append(id).append('\n');
    }
}