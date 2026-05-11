import java.util.*;

class Solution {

    public int solution(int[] people, int limit) {
        Arrays.sort(people);

        int cnt = 0;
        int left = 0, right = people.length - 1;

        while (left <= right) {
            if (people[right--] + people[left] <= limit) left++;

            cnt++;
        }

        return cnt;
    }
}