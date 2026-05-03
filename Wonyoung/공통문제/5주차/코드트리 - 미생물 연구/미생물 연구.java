import java.util.*;
import java.io.*;

public class Main {
    public static int N, Q;
    public static int[][] board;
    public static boolean[][] visited; 
    public static int[][] dir = {{1,0},{-1,0},{0,1},{0,-1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());
        board = new int[N][N];

        for(int i = 0; i < Q; i++){
            st = new StringTokenizer(br.readLine());

            int r1 = Integer.parseInt(st.nextToken());
            int c1 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());

            // 1. 미생물 투입
            injectGerm(r1, c1, r2, c2, i+1);

            // 2. 배양용기 이동
            board = moveBoard(i+1);

            // 3. 실험 결과 기록
            System.out.println(recordResult(i+1));
        }
    }

    public static void injectGerm(int r1, int c1, int r2, int c2, int num){
        for(int i = c1; i < c2; i++){
            for(int j = r1; j < r2; j++){
                board[i][j] = num;
            }
        }

        for(int i = 1; i <= num - 1; i++){
            if(checkDivided(i)) removeGerm(i);
        }
    }

    public static boolean checkDivided(int num){
        visited = new boolean[N][N];
        
        int cnt = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(!visited[i][j] && board[i][j] == num){
                    if(cnt > 0) return true;
                    bfs(i,j,num);
                    cnt++;
                }
            }
        }
        return false;
    }

    public static void bfs(int i, int j, int num){
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offerLast(new int[]{i,j});
        visited[i][j] = true;

        while(!queue.isEmpty()){
            int[] cur = queue.pollFirst();
            for(int[] d: dir){
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if(inBoard(nr, nc) && !visited[nr][nc] && board[nr][nc] == num){
                    queue.offerLast(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            }
        }
    }

    public static void removeGerm(int num){
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(board[i][j] == num) board[i][j] = 0;
            }
        }
    }

    public static boolean inBoard(int r, int c){
        return 0 <= r && r < N && 0 <= c && c < N;
    }

    public static int[][] moveBoard(int num){
        int[] checkSize = new int[num + 1];

        // 가장 큰 미생물 무리 찾기
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(board[i][j] > 0) checkSize[board[i][j]]++;
            }
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt((int[] arr) -> -arr[0]).thenComparing((arr) -> arr[1]));
        for(int i = 1; i <= num; i++) pq.add(new int[]{checkSize[i], i});
        int[][] newBoard = new int[N][N];

        while(!pq.isEmpty()){
            int[] germ = pq.poll();
            PriorityQueue<int[]> germPos = new PriorityQueue<>(Comparator.comparingInt((int[] arr) -> arr[0]).thenComparing((arr) -> arr[1]));

            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    if(board[i][j] == germ[1]) germPos.add(new int[]{i,j}); 
                }
            }

            if(germPos.isEmpty()) continue;

            int diffX = 100, diffY = 100;
            outer:
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    if(isMovable(i, j, germPos, newBoard)){
                        int[] pos = germPos.peek();
                        diffX = i - pos[1];
                        diffY = j - pos[0];
                        break outer;
                    }
                }
            }

            if(diffX == 100 && diffY == 100) continue;

            while(!germPos.isEmpty()){
                int[] g = germPos.poll();
                newBoard[g[0] + diffY][g[1] + diffX] = germ[1];
            }
        }
        return newBoard;
    }

    public static boolean isMovable(int c, int r, PriorityQueue<int[]> germPos, int[][] board){
        int[] pos = germPos.peek();
        int diffX = c - pos[1], diffY = r - pos[0];

        for(int[] germ: germPos){
            int nr = germ[0] + diffY, nc = germ[1] + diffX; 
            if(!inBoard(nr, nc) || board[nr][nc] != 0) return false;
        }
        return true;
    }

    public static int recordResult(int num){
        int total = 0;
        boolean[][] neighbor = new boolean[num + 1][num + 1];
        int[] germSize = new int[num + 1];

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(board[i][j] > 0){
                    int a = board[i][j];
                    germSize[a]++;

                    for(int[] d: dir){
                        int nr = i + d[0], nc = j + d[1];
                        if(inBoard(nr, nc) && board[nr][nc] > 0 && board[nr][nc] != a){
                            int b = board[nr][nc];
                            neighbor[a][b] = true;
                            neighbor[b][a] = true;
                        }
                    }
                }
            }
        }

        for(int i = 1; i <= num; i++){
            for(int j = 1; j <= num; j++){
                if(neighbor[i][j]){
                    total += germSize[i]*germSize[j];
                    neighbor[i][j] = false;
                    neighbor[j][i] = false;
                }
            }
        }
        return total;
    }
}