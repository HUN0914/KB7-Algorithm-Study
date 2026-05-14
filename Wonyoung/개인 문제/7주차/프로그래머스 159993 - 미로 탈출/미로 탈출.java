import java.util.*;

class Solution {
    public static int[][] directions = {{1,0},{-1,0},{0,-1},{0,1}};
    public static int[] start, lever, exit;
    public static char[][] miro;
    public static int N, M;
    public int solution(String[] maps) {
        N = maps.length;
        M = maps[0].length();
        miro = new char[N][M];
        
        for(int i =0; i < N; i++){
            for(int j = 0; j < M; j++){
                miro[i][j] = maps[i].charAt(j);
                if(maps[i].charAt(j) == 'S') start = new int[]{i,j};
                if(maps[i].charAt(j) == 'L') lever = new int[]{i,j};
                if(maps[i].charAt(j) == 'E') exit = new int[]{i,j};
            }
        }
        
        int toLever = bfs(start, lever), toExit = bfs(lever, exit);
        if(toLever == -1 || toExit == -1) return -1;
        return toLever + toExit;
    }
    
    
    public static int bfs(int[] start, int[] end){
        int[][] visited = new int[N][M];
        Deque<int[]> q = new ArrayDeque<>();
        visited[start[0]][start[1]] = 1;
        q.offerLast(start);
        
        while(!q.isEmpty()){
            int[] cur = q.pollFirst();
            if(cur[0] == end[0] && cur[1] == end[1]) return visited[end[0]][end[1]] - 1;
            
            for(int[] dir: directions){
                int nr = cur[0] + dir[0], nc = cur[1] + dir[1];
                if(inMiro(nr, nc) && visited[nr][nc] == 0 && miro[nr][nc] != 'X'){
                    visited[nr][nc] = visited[cur[0]][cur[1]] + 1;
                    q.offerLast(new int[]{nr, nc});
                }
            }
        }
        return -1;
    }
    
    public static boolean inMiro(int r, int c){
        return 0 <= r && r < N && 0 <= c && c < M;
    }
}