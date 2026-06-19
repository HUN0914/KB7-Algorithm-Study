import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int n = numbers.length;
        int[] answer = new int[n];
        Deque<int[]> dq = new ArrayDeque<>();
        
        for(int i = 0; i < n; i++){
            if(!dq.isEmpty() && dq.peekLast()[0] <numbers[i]){
                while(!dq.isEmpty() && dq.peekLast()[0] < numbers[i]){
                    int[] num = dq.pollLast();
                    answer[num[1]] = numbers[i];
                }
            }
            
            dq.offerLast(new int[]{numbers[i], i});
        }

        while(!dq.isEmpty()){
            int[] rest = dq.pollLast();
            answer[rest[1]] = -1;
        }
        
        return answer;
    }
}
