import java.util.*;

class Solution {
    public static int N,M;
    public static int INF = Integer.MAX_VALUE;
    public static int[][][] visited;
    public static int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    public int solution(int n, int m, int[][] hole) {
        N = n;
        M = m;
        visited = new int[M][N][2];
        for(int[] h: hole){
            int r = h[1] - 1, c = h[0] - 1;
            visited[r][c][0] = INF;
            visited[r][c][1] = INF;
        }
        
        bfs();
        return visited[M-1][N-1][1] == 0 ?  -1 : visited[M-1][N-1][1] - 1; 
    }
    
    public static void bfs(){
        Deque<int[]> q = new ArrayDeque<>();
        q.offerLast(new int[]{0,0,0});
        visited[0][0][0] = 1;
        visited[0][0][1] = 1;
        
        while(!q.isEmpty()){
            int[] cur = q.pollFirst();
            int used = cur[2];
            
            for(int[] dir: directions){
                int nr = cur[0] + dir[0], nc = cur[1] + dir[1];
                // 그냥 뛰기
                if(inBoard(nr, nc) && visited[nr][nc][used] == 0){
                    q.offerLast(new int[]{nr, nc, used});
                    visited[nr][nc][used] = visited[cur[0]][cur[1]][used] + 1;
                }
                
                // 신비로운 신발 사용 가능하면 +1칸 시전하기
                if(used == 0){
                    nr += dir[0];
                    nc += dir[1];
                    if(inBoard(nr, nc) && visited[nr][nc][used + 1] == 0){
                        q.offerLast(new int[]{nr, nc, used + 1});
                        visited[nr][nc][used + 1] = visited[cur[0]][cur[1]][used] + 1;
                    }
                }
            }
        }
    }
    
    public static boolean inBoard(int r, int c){
        return 0 <= r && r < M && 0 <= c && c < N;
    }
}