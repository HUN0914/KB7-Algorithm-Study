import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        Deque<String> queue = new ArrayDeque<>();
        Map<String, Integer> index = new HashMap<>();
        int[] visited = new int[words.length];
        for(int i = 0; i < words.length; i++) index.put(words[i], i);
        queue.offerLast(begin);
        
        while(!queue.isEmpty()){
            String word1 = queue.pollFirst();
            
            for(int i = 0; i < words.length; i++){
                String word2 = words[i];
                if(!word1.equals(word2) && visited[i] == 0 && isTransfer(word1, word2, word2.length())){
                    visited[i] = visited[index.getOrDefault(word1, 0)] + 1;
                    if(word2.equals(target)) return visited[i];
                    queue.offerLast(word2);
                }
            }
        }
        
        return 0;
    }
    
    public static boolean isTransfer(String word1, String word2, int length){
        int cnt = 0;
        for(int i = 0; i < length; i++){
            char c1 = word1.charAt(i), c2 = word2.charAt(i);
            if(c1 != c2) cnt++;
        }
        
        return cnt == 1;
    }
}