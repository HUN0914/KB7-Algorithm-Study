import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int N = prices.length;
        int[] answer = new int[N];
        
        Deque<int[]> stocks = new ArrayDeque<>();
        
        for(int i = 0; i < N; i++){
            if(stocks.isEmpty()){
                stocks.offerLast(new int[]{prices[i], i});
                continue;
            }
            
            if(stocks.peekLast()[0] > prices[i]){
                while(!stocks.isEmpty() && stocks.peekLast()[0] > prices[i]){
                    int[] stock = stocks.pollLast();
                    answer[stock[1]] = i - stock[1]; 
                }
            }
            
            stocks.offerLast(new int[]{prices[i], i});
        }
        
        while(!stocks.isEmpty()){
            int[] stock = stocks.pollLast();
            answer[stock[1]] = (N - 1) - stock[1]; 
        }
        
        return answer;
    }
}