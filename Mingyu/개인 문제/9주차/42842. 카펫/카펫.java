class Solution {
    public int[] solution(int brown, int yellow) {

        for (int yh = 1; yh * yh <= yellow; yh++) {
            if (yellow % yh != 0) continue;

            int yw = yellow / yh;

            if (2 * yw + 2 * yh + 4 == brown) {
                return new int[]{yw + 2, yh + 2};
            }
        }

        return new int[]{};
    }
}