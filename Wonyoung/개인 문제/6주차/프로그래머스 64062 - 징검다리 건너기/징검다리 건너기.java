import java.util.*;

class Solution {
    public int solution(int[] stones, int k) {
        int answer = 0;
        int start = 1, end = (int) 2e9;
        
        while(start <= end){
            int middle = (start + end) / 2;
            int jump = 1;
            boolean flag = true;
            
            for(int stone: stones){
                if(stone >= middle){
                    jump = 1;
                    continue;
                }
                
                jump++;
                
                if(jump > k){
                    flag = false;
                    break;
                }
            }
            
            if(!flag){
                end = middle - 1;
            } else {
                start = middle + 1;
                answer = middle;
            }
        }
        return answer;
    }
}