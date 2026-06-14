import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);
        int[] newArr = new int[rocks.length + 2];
        int m = newArr.length;
        newArr[0] = 0;
        newArr[m - 1] = distance;
        for(int i = 1; i < m -1; i++) newArr[i] = rocks[i-1];

        int answer = 0;
        int start = 1, end = distance;
        while(start <= end){
            // 각 바위 사이의 거리에서 허용되는 가장 작은 간격을 정하고
            int middle = (start + end) / 2;
            int cnt = 0;
            int d = 0;

            for(int i = 1; i < m; i++){
                d += newArr[i] - newArr[i-1];

                if(d >= middle){
                    d = 0; continue;
                }
                // 그 간격보다 작을 때마다 바위를 제거한다.
                cnt++;
            }

            // i. n보다 작거나 같으면 통과 -> 간격 범위를 높여서 좁히기
            if(cnt <= n){
                answer = middle;
                start = middle + 1;
                // ii. n보다 크면 실패 -> 간격 범위를 낮춰서 좁히기
            } else {
                end = middle - 1;
            }
        }
        return answer;
    }
}