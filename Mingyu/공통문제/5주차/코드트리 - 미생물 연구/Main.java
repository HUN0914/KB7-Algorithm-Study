import java.io.*;
import java.util.*;

public class Main {
    static int N, Q;
    static int[][] board;

    // board[y][x]
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    static class Cell {
        int y, x;

        Cell(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    static class Micro {
        int id;
        int area;
        int minY, minX; // top-left point
        List<Cell> cells = new ArrayList<>();

        Micro(int id) {
            this.id = id;
            this.area = 0;
            this.minY = Integer.MAX_VALUE;
            this.minX = Integer.MAX_VALUE;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        board = new int[N][N];

        for (int id = 1; id <= Q; id++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            insertMicro(id, x1, y1, x2, y2);
            removeSplitMicros();
            moveAllMicros();

            sb.append(calcScore()).append("\n");
        }

        System.out.print(sb);
    }

    // Step1. Insert Micro
    static void insertMicro(int id, int x1, int y1, int x2, int y2) {
        for (int y = y1; y < y2; y++) {
            for (int x = x1; x < x2; x++) {
                board[y][x] = id;
            }
        }
    }

    // Step2. Remove split Micros
    static void removeSplitMicros() {
        boolean[][] visited = new boolean[N][N];
        int[] componentCount = new int[Q + 1];

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (board[y][x] == 0 || visited[y][x]) continue;

                int id = board[y][x];
                bfs(y, x, visited, board);
                componentCount[id]++;
            }
        }

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                int id = board[y][x];

                if (id != 0 && componentCount[id] >= 2) {
                    board[y][x] = 0;
                }
            }
        }
    }

    // Step3. Move all Micros to next board
    static void moveAllMicros() {
        List<Micro> micros = getLiveMicros();

        micros.sort((a, b) -> {
            if (a.area != b.area) return b.area - a.area; // larger area
            return a.id - b.id; // smaller id
        });

        int[][] nextBoard = new int[N][N];

        for (Micro micro : micros) {
            placeMicro(nextBoard, micro);
        }

        board = nextBoard;
    }

    static void placeMicro(int[][] nextBoard, Micro micro) {
        for (int baseX = 0; baseX < N; baseX++) {
            for (int baseY = 0; baseY < N; baseY++) {
                if (canPlace(nextBoard, micro, baseY, baseX)) {
                    for (Cell cell : micro.cells) { // relative coordinate
                        int ny = baseY + (cell.y - micro.minY);
                        int nx = baseX + (cell.x - micro.minX);
                        nextBoard[ny][nx] = micro.id;
                    }
                    return;
                }
            }
        }
    }

    static boolean canPlace(int[][] nextBoard, Micro micro, int baseY, int baseX) {
        for (Cell cell : micro.cells) { // relative coordinate
            int ny = baseY + (cell.y - micro.minY);
            int nx = baseX + (cell.x - micro.minX);

            if (ny < 0 || ny >= N || nx < 0 || nx >= N || nextBoard[ny][nx] != 0) return false;
        }

        return true;
    }

    // Step4. Calculate score
    static long calcScore() {
        int[] area = new int[Q + 1];
        boolean[][] adj = new boolean[Q + 1][Q + 1];

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                int a = board[y][x];
                if (a == 0) continue;

                area[a]++; // Calculate each Micro's area

                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];

                    if (ny >= 0 && ny < N && nx >= 0 && nx < N) {
                        int b = board[ny][nx];
                        if (b != 0 && a != b) { // adjacent to another micro
                            adj[Math.min(a, b)][Math.max(a, b)] = true; // micro A is adjacent to B
                        }
                    }
                }
            }
        }

        long score = 0;
        for (int a = 1; a <= Q; a++) {
            for (int b = a + 1; b <= Q; b++) {
                if (adj[a][b]) {
                    score += (long) area[a] * area[b];
                }
            }
        }

        return score;
    }

    // get list of live micros in board
    static List<Micro> getLiveMicros() {
        List<Micro> result = new ArrayList<>();
        boolean[][] visited = new boolean[N][N];

        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                if (board[y][x] == 0 || visited[y][x]) continue;

                result.add(bfs(y, x, visited, board));
            }
        }

        return result;
    }

    static Micro bfs(int startY, int startX, boolean[][] visited, int[][] targetBoard) {
        int id = targetBoard[startY][startX];
        Micro micro = new Micro(id);

        Queue<Cell> q = new ArrayDeque<>();
        q.offer(new Cell(startY, startX));
        visited[startY][startX] = true;

        while (!q.isEmpty()) {
            Cell cur = q.poll();

            micro.cells.add(cur);
            micro.area++;
            micro.minY = Math.min(micro.minY, cur.y);
            micro.minX = Math.min(micro.minX, cur.x);

            for (int d = 0; d < 4; d++) {
                int ny = cur.y + dy[d];
                int nx = cur.x + dx[d];

                if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
                if (visited[ny][nx]) continue;
                if (targetBoard[ny][nx] != id) continue;

                visited[ny][nx] = true;
                q.offer(new Cell(ny, nx));
            }
        }

        return micro;
    }
}