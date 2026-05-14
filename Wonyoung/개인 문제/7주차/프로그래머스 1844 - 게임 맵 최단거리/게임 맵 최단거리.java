import java.util.*;

class Solution {
    public static int N, M;
    public static int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    public int solution(int[][] maps) {
        N = maps.length;
        M = maps[0].length;
        int[][] visited = new int[N][M];
        
        Deque<int[]> q = new ArrayDeque<>();
        q.offerLast(new int[]{0,0});
        visited[0][0] = 1;
        
        while(!q.isEmpty()){
            int[] cur = q.pollFirst();
            if(cur[0] == N-1 && cur[1] == M-1) return visited[N-1][M-1];
            
            for(int[] dir: directions){
                int nr = cur[0] + dir[0], nc = cur[1] + dir[1];
                if(inMaps(nr, nc) && visited[nr][nc] == 0 && maps[nr][nc] == 1){
                    visited[nr][nc] = visited[cur[0]][cur[1]] + 1;
                    q.offerLast(new int[]{nr, nc});
                }
            }
        }
        return -1;
    }
    
    public static boolean inMaps(int i, int j){
        return 0 <= i && i < N && 0 <= j && j < M;
    }
}