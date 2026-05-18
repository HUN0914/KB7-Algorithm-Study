import java.util.*;

class Solution {
    Set<Integer> numSet = new HashSet<>();
    boolean[] visited;

    public int solution(String numbers) {
        visited = new boolean[numbers.length()];

        dfs(numbers, "");

        int answer = 0;

        for (int num : numSet) {
            if (isPrime(num)) {
                answer++;
            }
        }

        return answer;
    }

    private void dfs(String numbers, String cur) {
        if (!cur.isEmpty()) {
            numSet.add(Integer.parseInt(cur));
        }

        for (int i = 0; i < numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(numbers, cur + numbers.charAt(i));
                visited[i] = false;
            }
        }
    }

    private boolean isPrime(int num) {
        if (num < 2) return false;

        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }
}