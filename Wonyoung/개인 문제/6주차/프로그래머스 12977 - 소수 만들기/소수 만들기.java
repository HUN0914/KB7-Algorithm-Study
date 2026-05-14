import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int n = nums.length;
        int answer = 0;
        
        for(int i = 0; i < n-2; i++){
            for(int j = i+1; j < n-1; j++){
                for(int k = j+1; k < n; k++){
                    int num = nums[i] + nums[j] + nums[k];
                    if(isPrime(num)) answer++;
                }
            }
        }
        
        return answer;
    }
    
    public static boolean isPrime(int num){
        int N = (int) Math.sqrt(num);
        for(int i = 2; i <= N; i++){
            if(num % i == 0) return false;
        }
        return true;
    }
}