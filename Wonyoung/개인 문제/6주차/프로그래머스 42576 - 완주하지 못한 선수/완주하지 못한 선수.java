import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        for(String complete: completion){
            map.put(complete, map.getOrDefault(complete, 0) + 1);
        }
        
        for(String runner: participant){
            if(!map.containsKey(runner) || map.get(runner) == 0){
                return runner;
            } else {
                map.put(runner, map.get(runner) - 1);
            }
        }
        
        String answer = "";
        return answer;
    }
}