import java.util.*;

class Solution {
    static int N;
    static String NUMS;
    static Set<Integer> primes = new HashSet<>();
    public int solution(String numbers) {
        N = numbers.length();
        NUMS = numbers;
        boolean[] visited = new boolean[N];
        int[] order = new int[N];
        permutation(order, visited, 0);
        
        return primes.size();
    }
    
    public static void makeNumber(int[] order){
        String str = "";
        for(int i = 0; i < N; i++){
            str += String.valueOf(NUMS.charAt(order[i]));
            int value = Integer.parseInt(str);
            if(isPrime(value)) primes.add(value);
        }
    }
    
    public static boolean isPrime(int value){
        if(value < 2) return false;
        if(value <= 3) return true;
        
        int n = (int) Math.sqrt(value);
        for(int i = 2; i <= n; i++){
            if(value % i == 0) return false;
        }
        
        return true;
    }
    
    public static void permutation(int[] order, boolean[] visited, int m){
        if(m == N){
            makeNumber(order);
        }
        
        for(int i = 0; i < N; i++){
            if(!visited[i]){
                visited[i] = true;
                order[m] = i;
                permutation(order, visited, m + 1);
                visited[i] = false;
                order[m] = 0;
            }
        }
    }
}