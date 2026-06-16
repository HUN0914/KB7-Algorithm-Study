import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);

        int left = 1;
        int right = distance;

        // maximum value of minimum gap
        int answer = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2; 
            
            // num of removed rocks
            int removed = 0;
            // rock keeped just before
            int prev = 0; 

            for (int rock : rocks) {
                int gap = rock - prev;

                if (gap < mid) {
                    // should be removed
                    removed++;
                } else {
                    // keep this rock
                    prev = rock;
                }
            }
            
            // compare final prev <-> distance 
            if (distance - prev < mid) removed++;

            if (removed <= n) {
                // can be candidate
                answer = mid;
                // large gap possible?
                left = mid + 1;
            } else {
                // too many rocks to remove
                right = mid - 1;
            }
        }

        return answer;
    }
}