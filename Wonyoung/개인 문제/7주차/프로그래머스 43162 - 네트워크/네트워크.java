import java.util.*;

class Solution {
    public static boolean[] visited;
    public static int[][] graph;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        graph = computers;

        for(int i = 0; i < n; i++){
            if(!visited[i]){
                bfs(i, n);
                answer++;
            }
        }
        return answer;
    }
    
    public static void bfs(int start, int size){
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offerLast(start);
        visited[start] = true;

        while(!queue.isEmpty()){
            int cur = queue.pollFirst();
            for(int i = 0; i < size; i++){
                if(i != cur && !visited[i] && graph[cur][i] > 0){
                    visited[i] = true;
                    queue.offerLast(i);
                }
            }
        }
    }
}