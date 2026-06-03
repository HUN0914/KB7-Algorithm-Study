import java.util.*;

class Solution {
    static int[] parent;
    static int answer;
    public int solution(int n, int[][] costs) {
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt((int[] k) -> k[2]));
        for(int[] cost: costs) q.add(cost);
        
        parent = new int[n];
        for(int i = 0; i < n; i++) parent[i] = i;
        
        answer = 0;
        while(!q.isEmpty()){
            int[] bridge = q.poll();
            int from = bridge[0], to = bridge[1], cost = bridge[2];
            union(from, to, cost);
            
            int cnt = 0;
            for(int i = 0; i < n; i++) if(parent[i] == i) cnt++;
            
            if(cnt == 1) return answer;
        }
        return answer;
    }
    
    public static void union(int a, int b, int cost){
        int A = find(a);
        int B = find(b);
        
        if(A != B){
            parent[B] = A;
            answer += cost;
        }
    }
    
    public static int find(int x){
        if(x == parent[x]){
            return x;
        } else {
            return find(parent[x]);
        }
    }
}