import java.util.*;

class Solution {
    static int[] intCount;
    public int solution(int[] arr) {
        int answer = 1;
        int max = Arrays.stream(arr)
            .max()
            .getAsInt();
        intCount = new int[max + 1];
        
        for(int num: arr){
            primeFac(num);
            // System.out.println(Arrays.toString(intCount));
        } 
        
        for(int i = 2; i <= max; i++){
            if(intCount[i] > 0) answer *= Math.pow(i, intCount[i]);
        }
        
        return answer;
    }
    
    public static void primeFac(int num){
        Map<Integer, Integer> map = new HashMap<>();
        
        while(num > 1){
            int N = (int) Math.sqrt(num);
            int n = 0;
            for(int i = 2; i <= N; i++){
                if(num % i == 0){
                    n = i; 
                    break;
                }
            }
            
            if(n == 0) n = num;
            map.put(n, map.getOrDefault(n, 0) + 1);
            num /= n;
        }
        
        for(Map.Entry<Integer, Integer> nums: map.entrySet()){
            int key = nums.getKey(), value = nums.getValue();
            intCount[key] = Math.max(intCount[key], value);
        }
    }
    
    
}