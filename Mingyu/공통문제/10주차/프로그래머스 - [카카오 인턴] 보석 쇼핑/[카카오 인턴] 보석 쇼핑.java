import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        Set<String> gemTypes = new HashSet<>(Arrays.asList(gems));
        int totalTypes = gemTypes.size();

        // number of each gem included in window ex) DIA -> 3, RUBY -> 1
        Map<String, Integer> window = new HashMap<>();

        int left = 0;
        int answerStart = 0;
        int answerEnd = gems.length - 1;
        
        // expand window
        for (int right = 0; right < gems.length; right++) {
            String rightGem = gems[right];
            
            window.put(rightGem, window.getOrDefault(rightGem, 0) + 1);

            // if current window include all types, reduce window 
            while (window.size() == totalTypes) {
                if (right - left < answerEnd - answerStart) {
                    answerStart = left;
                    answerEnd = right;
                }

                String leftGem = gems[left];
                int count = window.get(leftGem);
                if (count == 1) {
                    // remove type from window too
                    window.remove(leftGem);
                } else {
                    // decrease only number of gem
                    window.put(leftGem, count - 1);
                }

                left++;
            }
        }

        return new int[] { answerStart + 1, answerEnd + 1 };
    }
}