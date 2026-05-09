import java.util.*;

class Solution {
    public static int[][] tree;
    public static int[] inform;
    public static int answer;
    public int solution(int[] info, int[][] edges) {
        int N = info.length;
        tree = new int[N][2];
        inform = info;
        for(int i = 0; i < N; i++) Arrays.fill(tree[i], -1);
        
        for(int[] edge: edges){
            int parent = edge[0], child = edge[1];
            if(tree[parent][0] == -1){
                tree[parent][0] = child;
            } else {
                tree[parent][1] = child;
            } 
        }
        
        List<Integer> member = new ArrayList<>();
        member.add(0);
        collectSheep(0, member, 0, 0);
        return answer;
    }
    
    
    public static void collectSheep(int loc, List<Integer> member, int sheep, int wolf){      
        int kind = inform[loc];
        
        switch(kind){
            case 1: wolf++; break;
            case 0: sheep++; break;     
        }
        
        if(sheep <= wolf) return;
        answer = Math.max(answer, sheep);
        
        List<Integer> list = new ArrayList<>(member);
        list.remove(Integer.valueOf(loc));
        
        int left = tree[loc][0], right = tree[loc][1];
        if(left > -1) list.add(left);
        if(right > -1) list.add(right);
        
        for(int next: list){
            collectSheep(next, list, sheep, wolf);
        }
    }
}