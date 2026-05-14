import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        for(int[] line: edge){
            int from = line[0], to = line[1];
            graph.computeIfAbsent(from, k -> new ArrayList<>()).add(to);
            graph.computeIfAbsent(to, k -> new ArrayList<>()).add(from);
        }
        
        int[] visited = new int[n+1];
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offerLast(1);
        visited[1] = 1;
        
        while(!queue.isEmpty()){
            int cur = queue.pollFirst();
            for(int next: graph.get(cur)){
                if(visited[next] == 0){
                    visited[next] = visited[cur] + 1;
                    queue.offerLast(next);
                }
            }
        }
        
        int max = Arrays.stream(visited).max().getAsInt();
        int answer = 0;
        for(int d: visited){
            if(d == max) answer++;
        }
        
        return answer;
    }
}