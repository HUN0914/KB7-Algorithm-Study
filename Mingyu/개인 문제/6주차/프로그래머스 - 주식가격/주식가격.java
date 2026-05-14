import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && prices[stack.peek()] > prices[i]) {
                int prev = stack.pop();
                answer[prev] = i - prev;
            }

            stack.push(i);
        }

        while (!stack.isEmpty()) {
            int prev = stack.pop();
            answer[prev] = n - 1 - prev;
        }

        return answer;
    }
}