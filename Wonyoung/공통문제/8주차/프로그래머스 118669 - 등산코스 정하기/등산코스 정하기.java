import java.util.*;

class Solution {
    static int INF = Integer.MAX_VALUE;
    static int[] noRestTime;
    static boolean[] isGate, isPeek;
    static Map<Integer, List<int[]>> map = new HashMap<>();
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        for(int[] path: paths){
            int from = path[0], to = path[1], distance = path[2];
            map.computeIfAbsent(from, k -> new ArrayList<>()).add(new int[]{to, distance});
            map.computeIfAbsent(to, k -> new ArrayList<>()).add(new int[]{from, distance});
        }
        
        Arrays.sort(summits);
        isGate = new boolean[n+1];
        isPeek = new boolean[n+1];
        for(int gate: gates) isGate[gate] = true;
        for(int summit: summits) isPeek[summit] = true;
        
        int[] answer = {-1, INF};
        noRestTime = new int[n + 1];
        Arrays.fill(noRestTime, INF);

        dijkstra(gates);
        for(int summit: summits) if(answer[1] > noRestTime[summit]) answer = new int[]{summit, noRestTime[summit]};
        return answer;
    }
    
    public static void dijkstra(int[] gates){
        Deque<int[]> q = new ArrayDeque<>();
        for(int gate: gates){
            noRestTime[gate] = 0;
            q.offerLast(new int[]{gate, 0});
        } 
        
        while(!q.isEmpty()){
            int[] cur = q.pollFirst();
            for(int[] next: map.get(cur[0])){
                if(isGate[next[0]]) continue;
                
                int maxValue = Math.max(next[1], cur[1]);
                if(noRestTime[next[0]] > maxValue){
                    noRestTime[next[0]] = maxValue;
                    if(isPeek[next[0]]) continue;
                    q.offerLast(new int[]{next[0], maxValue});
                }
            }
        }

    }
}