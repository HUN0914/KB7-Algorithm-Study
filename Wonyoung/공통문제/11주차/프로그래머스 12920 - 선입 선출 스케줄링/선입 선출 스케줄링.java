import java.util.*;

class Solution {
    public int solution(int n, int[] cores) {
        int max = Arrays.stream(cores).max().getAsInt();
        int m = cores.length;
        int start = 1, end = max * n / m;

        if (n <= cores.length) return n;

        int time = 0;
        // 모든 프로세스를 맡길 수 있는(완료 X) 시간 계산 - 이분 탐색
        while (start <= end) {
            int middle = (start + end) / 2;

            int sum = 0;
            for (int core : cores) {
                int done = middle % core == 0 ? middle / core : middle / core + 1;
                sum += done;
            }

            if (sum >= n) {
                end = middle - 1;
                time = middle;
            } else {
                start = middle + 1;
            }
        }

        // 직전 시간에 완료한 프로세스 계산
        int recent = time - 1;
        for (int i = 0; i < m; i++) {
            int value = recent / cores[i];
            int done = recent % cores[i] == 0 ? value : value + 1;
            n -= done;
        }

        // 가장 최근 시간에 수행되는 프로세스를 1번부터 n번까지 순회
        int idx = -1;
        for (int i = 0; i < m; i++) {
            // 직전에 프로세스가 완료됐다면 새 프로세스 수행
            if (recent % cores[i] == 0) {
                n--;
                idx = i;
            }

            // 모든 프로세스 수행된 경우 마무리
            if (n == 0) break;
        }

        return idx + 1;
    }
}