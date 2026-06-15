import java.util.*;

class Solution {
    Map<Integer, Integer> toppingMap = new HashMap<>();
    public int solution(int[] topping) {
        int N = topping.length;
        
        int[] prev = new int[N + 1];
        
        for(int i = 0; i < N; i++){
            if(!toppingMap.containsKey(topping[i])){
                toppingMap.put(topping[i], 1);
                prev[i+1] = prev[i] + 1;
            } else {
                prev[i+1] = prev[i];            
            }
        }
        
        int[] post = new int[N + 1];
        toppingMap = new HashMap<>();
        
        for(int i = N; i > 0; i--){
            if(!toppingMap.containsKey(topping[i-1])){
                toppingMap.put(topping[i-1], 1);
                post[i-1] = post[i] + 1;
            } else {
                post[i-1] = post[i];            
            }
        }
        
        int answer = 0;  
        for(int i = 1; i <= N; i++){
            if(prev[i] == post[i]) answer++;
        }
        return answer;
    }
}