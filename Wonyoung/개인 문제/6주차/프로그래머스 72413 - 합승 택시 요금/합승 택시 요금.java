import java.util.*;

class Solution {
    public static int answer;
    public static int INF = Integer.MAX_VALUE;
    public static int[][] routes;
    // s: 출발 지점, a: 도착 지점(a), b: 도착 지점(b) 
    public int solution(int n, int s, int a, int b, int[][] fares) {
        answer = INF;
        routes = new int[n+1][n+1];
        
        for(int[] fare: fares){
            int c = fare[0], d = fare[1], f = fare[2];
            routes[c][d] = f;
            routes[d][c] = f;
        }
        
        int[] distS = dijkstra(s, n);
        int[] distA = dijkstra(a, n);
        int[] distB = dijkstra(b, n);
        
        for(int i = 1; i <= n; i++){
            int sx = distS[i];
            int xa = distA[i];
            int xb = distB[i];
            answer = Math.min(answer, sx + xa + xb);
        }

        return answer;
    }
    
    public static int[] dijkstra(int start, int n){
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt((int[] arr) -> arr[1]));
        int[] visited = new int[n+1];
        Arrays.fill(visited, INF);
        pq.add(new int[]{start, 0});
        visited[start] = 0;
            
        while(!pq.isEmpty()){
            int[] pos = pq.poll();
            int cur = pos[0], distance = pos[1];
            
            for(int next = 1; next <= n; next++){
                int cost = routes[cur][next];
                if(cost > 0 && visited[next] > distance + cost){
                    pq.add(new int[]{next, distance + cost});
                    visited[next] = distance + cost;
                }
            }
        }
                
        return visited;
    }
}