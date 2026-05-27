import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> q = new ArrayDeque<>();
        
        int[] cnt = new int[10];

        for (int i = 0; i < priorities.length; i++) {
            q.offer(new int[]{i, priorities[i]});
            cnt[priorities[i]]++;
        }

        int order = 0;

        while (!q.isEmpty()) {

            int[] cur = q.poll();
            int idx = cur[0];
            int priority = cur[1];

            int maxPriority = 9;
            while (maxPriority > 0 && cnt[maxPriority] == 0) {
                maxPriority--;
            }

            if (priority < maxPriority) q.offer(cur); 
            else {
                order++;
                
                cnt[priority]--;

                if (idx == location) return order;
            }
        }

        return -1;
    }
}