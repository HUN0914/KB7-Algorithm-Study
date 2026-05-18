class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }

    private int dfs(int[] numbers, int target, int idx, int sum) {
        if (idx == numbers.length) return sum == target ? 1 : 0;

        int plus = dfs(numbers, target, idx + 1, sum + numbers[idx]);

        int minus = dfs(numbers, target, idx + 1, sum - numbers[idx]);

        return plus + minus;
    }
}