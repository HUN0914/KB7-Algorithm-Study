class Solution {
    public int[] solution(int[] sequence, int k) {
        int n = sequence.length;

        int left = 0;
        int right = 0;
        int sum = 0;
        int ansL = 0;
        int ansR = n - 1;

        int minLength = Integer.MAX_VALUE;

        while (true) {
            if (sum >= k) {
                if (sum == k) {
                    int curLength = right - left;
                    if (curLength < minLength) {
                        minLength = curLength;
                        ansL = left;
                        ansR = right - 1;
                    }
                }
                sum -= sequence[left];
                left++;
            } else {
                if (right == n) break;

                sum += sequence[right];
                right++;
            }
        }

        return new int[]{ansL, ansR};
    }
}