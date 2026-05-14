import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for(char c: s.toCharArray()){
            if(c == '('){
                stack.offerLast(c);
            } else {
                if(stack.isEmpty()) return false;
                stack.pollLast();
            }
        }
        
        return stack.isEmpty();
    }
}