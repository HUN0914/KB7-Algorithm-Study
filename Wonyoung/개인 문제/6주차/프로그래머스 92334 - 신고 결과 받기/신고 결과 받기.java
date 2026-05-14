import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String, Set<String>> result = new HashMap<>();
        Map<String, Integer> idIndex = new HashMap<>();

        for(int i = 0; i < id_list.length; i++){
            result.put(id_list[i], new HashSet<>());
            idIndex.put(id_list[i], i);
       }
        
        for(String log: report){
            String[] content = log.split(" ");
            String fromId = content[0], toId = content[1];
            Set<String> list = result.get(toId);
            list.add(fromId);
            result.put(toId, list);
        }
                
        int[] answer = new int[id_list.length];
        for(Map.Entry<String, Set<String>> resultId : result.entrySet()){
            if(resultId.getValue().size() >= k){
                for(String str: resultId.getValue()){
                    answer[idIndex.get(str)]++;
                }
            }
        }
        
        return answer;
    }
}