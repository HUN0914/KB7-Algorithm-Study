import java.util.*;

class Solution {
    public static int MAX = 10000000;
    public int solution(int k, int[] tangerine) {
        PriorityQueue<Integer> oranges = new PriorityQueue<>((a,b) -> b - a);
        
        Map<Integer, Integer> orangeMap = new HashMap<>();
        for(int t: tangerine){
            int value = orangeMap.getOrDefault(t, 0);
            orangeMap.put(t, value + 1);
        }
        
        for(Map.Entry<Integer, Integer> orange: orangeMap.entrySet()){
            oranges.add(orange.getValue());
        }
        
        int orangeCnt = 0;
        int answer = 0;
        
        while(orangeCnt < k){
            orangeCnt += oranges.poll();
            answer++;
        }
        
        return answer;
    }
}