import java.util.*;

class Solution {
    static int n;
    static Map<Character, Character> map = new HashMap<>();
    public int solution(String s) {
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        n = s.length();
        
        int answer = 0;
        for(int i = 0; i < n; i++){
            int start = i;
            if(isRight(s, start)) answer++;
        }
        
        return answer;
    }
    
    static boolean isRight(String s, int start){
        Deque<Character> q = new ArrayDeque<>();
        
        for(int i = start; i < start + n; i++){
            int idx = i % n;
            char c = s.charAt(idx);
            
            if(q.isEmpty()){
                if(map.containsKey(c)) return false;
                q.offerLast(c);
                continue;
            }
            
            if(!map.containsKey(c)){
                q.offerLast(c);
                continue;
            }
            
            if(map.get(c) != q.peekLast()) return false;
            q.pollLast();
        }
        
        return q.isEmpty();
    }
}