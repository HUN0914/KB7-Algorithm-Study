import java.util.*;

class Solution {
    static Map<String, Integer> str1Set = new HashMap<>();
    static Map<String, Integer> str2Set = new HashMap<>();
    
    public int solution(String str1, String str2) {
        makeSet(str1Set, str1);
        makeSet(str2Set, str2);

        if(str1Set.size() == 0 && str2Set.size() == 0) return 1*65536;
        
        Map<String, Integer> inter = new HashMap<>(str1Set);
        Map<String, Integer> union = new HashMap<>(str1Set);
        
        for(Map.Entry<String, Integer> st2st: str2Set.entrySet()){
            String key = st2st.getKey();
            int value = st2st.getValue();
            
            if(inter.containsKey(key)){
                if(inter.get(key) == value){
                    inter.remove(key);
                } else {
                    inter.put(key, Math.abs(inter.get(key) - value));
                }
            } else {
                inter.put(key, value);
            }
            
            union.put(key, Math.max(union.getOrDefault(key, 0) ,value));            
        }
        

        int u = getTotal(union);
        int i = getTotal(inter);

        double answer = (double) (u - i) / u;

        return (int) (answer * 65536);
    }
    
    public static void makeSet(Map<String, Integer> strSet, String str){
        for(int i = 0; i < str.length() - 1; i++){
            String s1 = "";
            char c1 = str.charAt(i), c2 = str.charAt(i+1);
            
            if(isCharacter(c1) && isCharacter(c2)){
                s1 = ("" + c1 + c2).toLowerCase();
                strSet.put(s1, strSet.getOrDefault(s1, 0) + 1);
            }
        }        
    }
    
    public static boolean isCharacter(char c){
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
    }
    
    public static int getTotal(Map<String, Integer> set){
        int cnt = 0;
        for(Map.Entry<String, Integer> ss: set.entrySet()) cnt += ss.getValue();
        return cnt;
    }
}