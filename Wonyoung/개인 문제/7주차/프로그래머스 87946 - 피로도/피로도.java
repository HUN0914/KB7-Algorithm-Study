import java.util.*;

class Solution {
    static int N, K, answer;
    static int[][] stages;
    public int solution(int k, int[][] dungeons) {
        N = dungeons.length;
        K = k;
        stages = dungeons;
        boolean[] visited = new boolean[N];
        int[] order = new int[N];
        permutation(order, visited,0);
        return answer;
    }
    
    public static void permutation(int[] order, boolean[] visited, int m){
        if(m == N){
            answer = Math.max(answer, exploreDungeons(order));
            return;
        }
        
        for(int i = 0; i < N; i++){
            if(!visited[i]){
                visited[i] = true;
                order[m] = i;
                permutation(order, visited, m + 1);
                visited[i] = false;
                order[m] = 0;
            }
        }
    }
    
    public static int exploreDungeons(int[] order){
        int hp = K;
        for(int i = 0; i < N; i++){
            int idx = order[i];
            if(hp < stages[idx][0]) return i;
            hp -= stages[idx][1];
        }
        return N;
    }
}