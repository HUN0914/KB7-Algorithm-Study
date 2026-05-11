import java.util.*;

class Solution {
    public static int INF = Integer.MAX_VALUE;
    public static int N, m, k, answer;
    public static int[] dirt;
    public static boolean[] visited;
    public int solution(int n, int[] weak, int[] dist) {
        N = n;
        m = weak.length;
        k = dist.length;
        dirt = weak;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)-> b-a);
        answer = INF;
        boolean[] visited = new boolean[k];
        permutation(dist, visited, 0, new int[k]);
        return answer == INF ? -1 : answer;
    }
    
    public static void permutation(int[] dist, boolean[] visited, int idx, int[] friends){
        if(idx == k){
            for(int i = 0; i < m; i++) checkWall(i, friends);
            return;
        }
        
        for(int i = 0; i < k; i++){
            if(!visited[i]){
                visited[i] = true;
                friends[idx] = dist[i];
                permutation(dist, visited, idx+1, friends);
                visited[i] = false;
                friends[idx] = 0;
            }
        }
    }
    
    public static void checkWall(int idx, int[] friends){
        visited = new boolean[m];
        int cur = idx;
        int next = (cur + 1) % m;
        
        int cnt = 0;
        for(int i = 0; i < k; i++){
            int friend = friends[i];
            int move = 0;
            
            while(move <= friend){
                int d = dirt[next] < dirt[cur] ? dirt[next] - dirt[cur] + N : dirt[next] - dirt[cur];
                visited[cur] = true;
                move += d;
                cnt++;
                cur = (cur + 1) % m;
                next = (next + 1) % m;
            }
            
            if(cnt == m){
                answer = Math.min(i+1, answer);
                return;
            }
        }
    }
}