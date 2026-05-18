class Solution {
    int answer = 0;
    boolean[] visited;
    int[][] dungeons;

    public int solution(int k, int[][] dungeons) {
        this.dungeons = dungeons;
        this.visited = new boolean[dungeons.length];

        dfs(k, 0);

        return answer;
    }

    private void dfs(int ap, int cnt) {
        answer = Math.max(answer, cnt);

        for (int i = 0; i < dungeons.length; i++) {
            int cut = dungeons[i][0];
            int cost = dungeons[i][1];

            if (!visited[i] && ap >= cut) {
                visited[i] = true;
                dfs(ap - cost, cnt + 1);
                visited[i] = false;
            }
        }
    }
}