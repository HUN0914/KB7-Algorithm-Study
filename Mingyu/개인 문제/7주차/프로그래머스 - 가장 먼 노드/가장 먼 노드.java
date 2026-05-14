import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        List<Integer>[] graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] e : edge) {
            int a = e[0];
            int b = e[1];

            graph[a].add(b);
            graph[b].add(a);
        }

        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);

        Queue<Integer> q = new ArrayDeque<>();

        dist[1] = 0;
        q.offer(1);

        int maxDist = 0;

        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int next : graph[cur]) {
                if (dist[next] != -1) {
                    continue;
                }

                dist[next] = dist[cur] + 1;
                maxDist = Math.max(maxDist, dist[next]);

                q.offer(next);
            }
        }

        int answer = 0;

        for (int i = 1; i <= n; i++) {
            if (dist[i] == maxDist) {
                answer++;
            }
        }

        return answer;
    }
}