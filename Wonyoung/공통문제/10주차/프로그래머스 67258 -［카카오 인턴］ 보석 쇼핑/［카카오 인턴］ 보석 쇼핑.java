import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        Set<String> gemSet = new HashSet<>();
        Map<String, Integer> gemMap = new HashMap<>();
        
        for(String gem: gems) gemSet.add(gem);
        
        int n = gems.length;
        int start = 0, end = -1;
        while(gemSet.size() > 0){
            String gem = gems[++end];
            gemSet.remove(gem);
            gemMap.put(gem, gemMap.getOrDefault(gem, 0) + 1);
        }
        
        int[] answer = new int[]{start + 1, end + 1};
        int range = end - start;
        
        while(end < n){
            while(start < end){
                String g = gems[start];
                if(gemMap.get(g) <= 1) break;
                gemMap.put(g, gemMap.get(g) - 1);
                start++;
            }
            
            if(end - start < range){
                answer = new int[]{start + 1, end + 1};
                range = end - start;
            }
            
            end++;
            if(end < n){
                String gend = gems[end];
                gemMap.put(gend, gemMap.getOrDefault(gend, 0) + 1);
            }
        }
        return answer;
    }
}