import java.util.*;

class Solution {
    static int N, answer;
    public int solution(int[] numbers, int target) {
        N = numbers.length;
        
        targetNumber(numbers, target, 0,0);
        return answer;
    }
    
    public static void targetNumber(int[] numbers, int target, int k, int sum){
        if(k == N){
            if(sum == target) answer++;
            return;
        }
        
        targetNumber(numbers, target, k+1, sum + numbers[k]);
        targetNumber(numbers, target, k+1, sum - numbers[k]);
    }
}