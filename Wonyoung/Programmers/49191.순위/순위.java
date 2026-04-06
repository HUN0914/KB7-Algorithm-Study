import java.util.*;

class Solution {
    public static Map<Integer, List<Integer>> winner = new HashMap<>();
    public static Map<Integer, List<Integer>> loser = new HashMap<>();
    public static boolean[] checked;
    public int solution(int n, int[][] results) {
        
        for(int[] result: results){
            winner.computeIfAbsent(result[0], k -> new ArrayList<>()).add(result[1]); 
            loser.computeIfAbsent(result[1], k -> new ArrayList<>()).add(result[0]);
        }
        
        int answer = 0;
        for(int i = 1; i <= n; i++){
            int w = 0, l = 0;
            checked = new boolean[n+1];
            List<Integer> win = winner.get(i);
            List<Integer> lose = loser.get(i);
            
            findCounter(winner, i, win);
            findCounter(loser, i, lose);
            
            int cnt = 0;
            for(int j=1; j<= n; j++){
                if(checked[j]) cnt++;
            }
            
            if(cnt == n-1) answer++;
        }
        
        return answer;
    }
    
    public static void findCounter(Map<Integer, List<Integer>> map, int key, List<Integer> value){
        if(map.get(key) == null) return;
        
        for(int counter: value){
            if(!checked[counter]){
                checked[counter] = true;
                findCounter(map, counter, map.get(counter));
            }
        }
    }
}