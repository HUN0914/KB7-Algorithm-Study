import java.util.*;
import java.util.stream.*;

class Solution {
    int[][] supoja = {
            {1, 2, 3, 4, 5},
            {2, 1, 2, 3, 2, 4, 2, 5},
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
    };

    public int[] solution(int[] answers) {
        int[] score = new int[supoja.length];

        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < supoja.length; j++) {
                if (answers[i] == supoja[j][i % supoja[j].length]) {
                    score[j]++;
                }
            }
        }

        int maxScore = Arrays.stream(score).max().getAsInt();

        return IntStream.range(0, score.length)
                        .filter(i -> score[i] == maxScore)
                        .map(i -> i + 1)
                        .toArray();
    }

}