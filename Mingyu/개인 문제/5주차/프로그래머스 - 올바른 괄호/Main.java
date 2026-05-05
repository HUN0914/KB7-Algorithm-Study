import java.util.*;

class Solution {
    boolean solution(String s) {                    
        Deque<Character> stack = new ArrayDeque<>();
        boolean isVPS = true;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                } else {
                    isVPS = false;
                    break;
                }
            }
        }

        if (!stack.isEmpty()) {
            isVPS = false;
        }

        return isVPS;
    }
}