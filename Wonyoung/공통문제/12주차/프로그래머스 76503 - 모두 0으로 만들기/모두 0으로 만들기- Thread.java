import java.util.*;

class Solution {
    static long answer;
    static int n;
    static long[] values;
    static boolean[] visited;
    static Map<Integer, List<Integer>> graph;

    public long solution(int[] a, int[][] edges) {
        // 1. 일단 a 합이 0이 되야함.
        long sum = Arrays.stream(a).sum();
        if (sum != 0) return -1L;

        answer = 0L;
        values = Arrays.stream(a).asLongStream().toArray();
        n = a.length;
        visited = new boolean[n];
        graph = new HashMap<>();

        for (int[] edge : edges) {
            int f = edge[0], t = edge[1];
            graph.computeIfAbsent(f, k -> new ArrayList<>()).add(t);
            graph.computeIfAbsent(t, k -> new ArrayList<>()).add(f);
        }

        // 재귀횟수제한을 넣는 경우 - Java의 쓰레기 같은 면
        long stackSize = 128 * 1024 * 1024;
        Thread thread = new Thread(null, new Runnable() {
            @Override
            public void run() {
                dfs(0);
            }
        }, "DFS-Thread", stackSize);

        try {
            thread.start();
            thread.join(); // DFS 스레드가 정답을 다 구할 때까지 대기
        } catch (InterruptedException e) {
            return -1L;
        }

        return answer;
    }

    public static long dfs(int index) {
        long value = values[index];
        visited[index] = true;

        List<Integer> row = graph.get(index);

        for (int i = 0; i < row.size(); i++) {
            int child = row.get(i);

            if (!visited[child]) {
                value += dfs(child);
            }
        }
        answer += Math.abs(value);
        return value;
    }

}