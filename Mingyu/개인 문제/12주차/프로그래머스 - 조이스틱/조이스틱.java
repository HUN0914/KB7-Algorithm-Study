class Solution {
    public int solution(String name) {
        int n = name.length();
        int answer = 0;
        int move = n - 1;

        for (int i = 0; i < n; i++) {
            char c = name.charAt(i);
            
            int up = c - 'A';
            int down = 'Z' - c + 1;

            answer += Math.min(up, down);

            int next = i + 1;

            while (next < n && name.charAt(next) == 'A') {
                next++;
            }

            int goRightThenLeft = i * 2 + n - next;
            
            int goLeftThenRight = (n - next) * 2 + i;

            move = Math.min(move, goRightThenLeft);
            move = Math.min(move, goLeftThenRight);
        }

        return answer + move;
    }
}