import java.util.*;

class Solution {
    static long answer;
    static int n;
    static long[] values;
    static boolean[] visited;
    static Map<Integer, List<Integer>> graph;

    public long solution(int[] a, int[][] edges) {
        n = a.length;
        values = new long[n];
        long sum = 0;
        for(int i = 0; i < n; i++) {
            values[i] = a[i];
            sum += values[i];
        }
        if(sum != 0) return -1L;
        
        answer = 0L;
        graph = new HashMap<>();
        visited = new boolean[n];
        
        for(int[] edge: edges){
            int f = edge[0], t = edge[1];
            graph.computeIfAbsent(f, k -> new ArrayList<>()).add(t);
            graph.computeIfAbsent(t, k -> new ArrayList<>()).add(f);
        }
        
        iterativeDfs(0);
        return answer;
    }
    
    public static void iterativeDfs(int root) {
        List<Integer> order = new ArrayList<>();
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        
        Deque<Integer> stack = new ArrayDeque<>();
        
        visited[root] = true;
        stack.offerLast(root);
        
        while(!stack.isEmpty()) {
            int cur = stack.pollLast();
            order.add(cur); 
            
            List<Integer> row = graph.get(cur);
            if(row != null) {
                for(int i = 0; i < row.size(); i++) {
                    int next = row.get(i);
                    if(!visited[next]) {
                        visited[next] = true;
                        parent[next] = cur;
                        stack.offerLast(next);
                    }
                }
            }
        }

        for (int i = order.size() - 1; i >= 0; i--) {
            int cur = order.get(i);
            
            answer += Math.abs(values[cur]);
            
            if (parent[cur] != -1) {
                values[parent[cur]] += values[cur];
            }
        }
    }
}