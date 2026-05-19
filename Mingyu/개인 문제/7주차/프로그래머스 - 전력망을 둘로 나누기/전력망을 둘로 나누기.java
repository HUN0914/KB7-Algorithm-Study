import java.util.*;

class Solution {
    static List<Integer>[] graph;
    static boolean[] visited;

    public int solution(int n, int[][] wires) {
        graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] wire : wires) {
            int a = wire[0];
            int b = wire[1];

            graph[a].add(b);
            graph[b].add(a);
        }

        int answer = Integer.MAX_VALUE;

        for (int[] wire : wires) {
            int cutA = wire[0];
            int cutB = wire[1];

            visited = new boolean[n + 1];

            int cnt = dfs(cutA, cutA, cutB);

            int rem = n - cnt;
            int diff = Math.abs(cnt - rem);

            answer = Math.min(answer, diff);
        }

        return answer;
    }

    private int dfs(int cur, int cutA, int cutB) {
        visited[cur] = true;

        int cnt = 1;

        for (int next : graph[cur]) {
            if ((cur == cutA && next == cutB) || (cur == cutB && next == cutA)) continue;

            if (!visited[next]) cnt += dfs(next, cutA, cutB);
        }

        return cnt;
    }
}