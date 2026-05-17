class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        boolean[] visited = new boolean[n];

        Queue<Integer> q = new ArrayDeque<>();

        q.offer(0);
        visited[0] = true;

        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int key : rooms.get(cur)) {
                if (!visited[key]) {
                    visited[key] = true;
                    q.offer(key);
                }
            }
        }

        for (boolean v : visited) {
            if (!v) {
                return false;
            }
        }

        return true;
    }
}