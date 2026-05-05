class Solution {
    int[] dp = new int[100001];

    public int solution(int n) {
        return fibo(n);
    }

    private int fibo(int n) {
        if (n <= 1) {
            return n;
        }

        if (dp[n] != 0) {
            return dp[n] % 1234567;
        }

        return dp[n] = (fibo(n - 2) + fibo(n - 1)) % 1234567;
    }
}