import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        int m = (int) (right - left);
        int[] answer = new int[m + 1];
        
        int cnt = 0;
        for(long i = left; i <= right; i++){
            long row = i / n, idx = i % n;
            long value = idx > row ? idx + 1 : row + 1;
            answer[cnt++] = (int) value;
        }
        
        return answer;
    }
}