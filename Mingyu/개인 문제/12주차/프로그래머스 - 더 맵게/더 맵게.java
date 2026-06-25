import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int s : scoville) {
            pq.offer(s);
        }

        int cnt = 0;

        while (!pq.isEmpty() && pq.peek() < K) {
            
            if (pq.size() < 2) return -1;
            
            int first = pq.poll();
            int second = pq.poll();
            int mixed = first + second * 2;

            pq.offer(mixed);

            cnt++;
        }

        return cnt;
    }
}