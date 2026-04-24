import java.util.*;

class Solution {
    public static int N;
    public int solution(String[] want, int[] number, String[] discount) {
        N = number.length;
        int[] checked = new int[N]; 
        
        int answer = 0;
        for(int i = 0; i < 10; i++){
            if(Arrays.asList(want).contains(discount[i])){
                int index = Arrays.asList(want).indexOf(discount[i]);
                checked[index]++;
            }
        }
        
        if(signup(checked, number)) answer++;
        
        for(int i = 10; i < discount.length; i++){
            if(Arrays.asList(want).contains(discount[i-10])){
                int left = Arrays.asList(want).indexOf(discount[i-10]);
                checked[left]--;
            }
            
            if(Arrays.asList(want).contains(discount[i])){
                int index = Arrays.asList(want).indexOf(discount[i]);
                checked[index]++;
            }
            
            if(signup(checked, number)) answer++;    
        }
        
        return answer;
    }
    
    public static boolean signup(int[] checked, int[] number){
        for(int i = 0; i < N; i++){
            if(checked[i] < number[i]) return false;
        }
        return true;
    }
}