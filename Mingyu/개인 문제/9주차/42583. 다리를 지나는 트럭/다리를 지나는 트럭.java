import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new ArrayDeque<>();

        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }

        int time = 0;
        int currentWeight = 0;
        int truckIdx = 0;

        while (truckIdx < truck_weights.length) {
            time++;

            currentWeight -= bridge.poll();

            if (currentWeight + truck_weights[truckIdx] <= weight) {
                bridge.offer(truck_weights[truckIdx]);
                currentWeight += truck_weights[truckIdx];
                truckIdx++;
            } else {

                bridge.offer(0);
            }
        }

        return time + bridge_length;
    }
}