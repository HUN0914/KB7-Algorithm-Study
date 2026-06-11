import java.util.*;

class Solution {
    static Map<String, Integer> count = new HashMap<>();
    public int solution(int cacheSize, String[] cities) {        
        int answer = 0;
        int n = cities.length;
        
        for(int i = 0; i < n; i++){
            if(cacheSize == 0){
                answer += 5;
                continue;
            }
            
            String city = cities[i].toLowerCase();
            
            if(count.containsKey(city)){
                count.put(city, i);
                answer++;
                continue;
            }
            
            if(count.size() < cacheSize){
                count.put(city, i);
            } else {
                int lru = n;
                String cand = "";
                
                for(Map.Entry<String, Integer> c: count.entrySet()){
                    String name = c.getKey();
                    int value = c.getValue();
                    
                    if(lru > value){
                        cand = name;
                        lru = value;
                    }
                }
                
                count.remove(cand);
                count.put(city, i);
            }
            
            answer += 5;
        }
        
        return answer;
    }
}