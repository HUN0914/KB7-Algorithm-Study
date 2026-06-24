import java.util.*;

class Solution {
    public int solution(String dirs) {
        int answer = 0;
        int[] loc = new int[]{0,0};
        
        Map<Character, int[]> dir = new HashMap<>();
        dir.put('U', new int[]{0,1});
        dir.put('D', new int[]{0,-1});
        dir.put('L', new int[]{-1,0});
        dir.put('R', new int[]{1,0});
        
        Map<String, Integer> lineMap = new HashMap<>();
        
        for(char d: dirs.toCharArray()){
            int r = loc[0], c = loc[1];
            int nr = dir.get(d)[0], nc = dir.get(d)[1];
            
            if(!inMap(r + nr, c + nc)) continue;
            
            String newKey1 = r + "," + c + "," + (r+nr) + "," + (c+nc);
            String newKey2 = (r+nr) + "," + (c+nc) + "," + r + "," + c;

            if(!lineMap.containsKey(newKey1) || !lineMap.containsKey(newKey2)){
                lineMap.put(newKey1, 1);
                lineMap.put(newKey2, 1);
                answer++;
            }
            loc = new int[]{r + nr, c + nc};
        }
        
        
        return answer;
    }
    
    public static boolean inMap(int r, int c){
        return -5 <= r && r <= 5 && -5 <= c && c <= 5;
    }
}