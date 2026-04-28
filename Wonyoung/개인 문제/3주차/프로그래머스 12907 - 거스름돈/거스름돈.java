import java.util.*;

class Solution {
    public int solution(int n, int[] money) {
        int[] dp = new int[n+1];
        dp[0] = 1;

        for(int coin: money){
            for(int i=1; i<= n; i++){
                if(i < coin) continue;
                dp[i] = (dp[i] + dp[i - coin]) % 1000000007;
            }
        }

        int answer = dp[n];
        return answer;
    }
}