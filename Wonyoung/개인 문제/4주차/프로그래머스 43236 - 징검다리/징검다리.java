import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int M = rocks.length;
        int[] distanceRock = new int[M + 1];
        Arrays.sort(rocks);
        
        for(int i = 0; i <= M; i++){
            if(i == 0){
                distanceRock[i] = rocks[i];
            } else if (i == M){
                distanceRock[i] = distance - rocks[i-1];
            } else {
                distanceRock[i] = rocks[i] - rocks[i-1];
            }
        }
        
        int start = 1, end = (int) 1e9;
        int answer = 0;
        while(start <= end){
            int middle = (start + end) / 2;
            int cnt = 0;
            int d = 0;
            
            for(int dr: distanceRock){
                d += dr;
                
                if(d < middle){
                    cnt++;
                } else {
                    d = 0;
                }
            }
            
            if(cnt > n){
                end = middle - 1;
            } else if (cnt <= n){
                answer = middle;
                start = middle + 1;
            }
            
        }
        
        return answer;
    }
}