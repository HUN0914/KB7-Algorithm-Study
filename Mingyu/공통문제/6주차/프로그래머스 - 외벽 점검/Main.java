class Solution {
    int[] dist;
    int[] extendWeak;
    boolean[] visited;
    int[] order;

    int wLen, dLen, minCnt;

    public int solution(int n, int[] weak, int[] dist) {
        this.dist = dist;
        this.wLen = weak.length;
        this.dLen = dist.length;
        this.minCnt = Integer.MAX_VALUE;
        
        // circular buffer -> linear array
        this.extendWeak = new int[wLen * 2];
        for (int i = 0; i < wLen; i++) {
            extendWeak[i] = weak[i];
            extendWeak[i + wLen] = weak[i] + n;
        }

        this.visited = new boolean[dLen];
        this.order = new int[dLen];

        permutation(0);

        return minCnt == Integer.MAX_VALUE ? -1 : minCnt;
    }

    // create all permutations of dist
    private void permutation(int depth) {
        // start checking validity if an order created
        if (depth == dLen) {
            check();
            return;
        }
        
        // create an order
        for (int i = 0; i < dLen; i++) {
            if (!visited[i]) {
                visited[i] = true;
                order[depth] = dist[i];
                permutation(depth + 1);
                visited[i] = false;
            }
        }
    }

    // check validity of this order
    private void check() {
        // each weak point can be start point
        for (int start = 0; start < wLen; start++) {
            int cnt = 1;

            // farthest point first friend can cover
            int cover = extendWeak[start] + order[cnt - 1];

            for (int i = start; i < start + wLen; i++) {
                if (extendWeak[i] > cover) {
                    cnt++; // next friend

                    if (cnt > dLen) {
                        break; // invalid order
                    }

                    // update point next friend can cover
                    cover = extendWeak[i] + order[cnt - 1];
                }
            }

            // update if cnt <= friends
            if (cnt <= dLen) {
                minCnt = Math.min(minCnt, cnt);
            }
        }
    }
}