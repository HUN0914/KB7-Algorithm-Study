import java.util.*;

class Solution {
    static class Edge {
        int to;
        int weight;

        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    static class State {
        int node;
        int intensity;

        State(int node, int intensity) {
            this.node = node;
            this.intensity = intensity;
        }
    }

    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        List<Edge>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] path : paths) {
            int a = path[0];
            int b = path[1];
            int w = path[2];

            graph[a].add(new Edge(b, w));
            graph[b].add(new Edge(a, w));
        }

        boolean[] isGate = new boolean[n + 1];
        for (int gate : gates) {
            isGate[gate] = true;
        }

        boolean[] isSummit = new boolean[n + 1];
        for (int summit : summits) {
            isSummit[summit] = true;
        }
        
        // minimum intensity to arrive node i
        int[] minIntensity = new int[n + 1];
        Arrays.fill(minIntensity, Integer.MAX_VALUE);

        PriorityQueue<State> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.intensity, b.intensity)
        );

        for (int gate : gates) {
            minIntensity[gate] = 0;
            pq.offer(new State(gate, 0));
        }

        // start dijkstra
        while (!pq.isEmpty()) {
            State cur = pq.poll();

            int now = cur.node;
            int intensity = cur.intensity;

            // ignore old info
            if (intensity > minIntensity[now]) continue;
            
            // only one summit
            if (isSummit[now]) continue;

            for (Edge edge : graph[now]) {
                int next = edge.to;
                int weight = edge.weight;

                // should not go to gate
                if (isGate[next]) continue;

                // intensity to arrive node next is max(intensity, weight)
                int nextIntensity = Math.max(intensity, weight);
                
                // update if find better route (low intensity)
                if (nextIntensity < minIntensity[next]) {
                    minIntensity[next] = nextIntensity;
                    pq.offer(new State(next, nextIntensity));
                }
            }
        }

        Arrays.sort(summits);

        int ansSummit = 0;
        int ansIntensity = Integer.MAX_VALUE;

        for (int summit : summits) {
            if (minIntensity[summit] < ansIntensity) {
                ansSummit = summit;
                ansIntensity = minIntensity[summit];
            }
        }

        return new int[]{ansSummit, ansIntensity};
    }
}