class Solution {
    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            // number to binary
            String bin = Long.toBinaryString(numbers[i]);

            /*
             * find minimum size of perfect binary tree
             * 10^15 = 50 bits -> max 63 nodes
             * perfect binary tree's number of nodes can be
             * -> 1, 3, 7, 15, 31, 63, ... , 2^n - 1
             */
            int size = 1;
            while (size < bin.length()) {
                size = size * 2 + 1;
            }

            // add zeros to binary string
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < size - bin.length(); j++) {
                sb.append('0');
            }
            sb.append(bin);
            String tree = sb.toString();
            
            // check if this tree can be answer
            answer[i] = check(tree, 0, tree.length() - 1, false) ? 1 : 0;
        }

        return answer;
    }

    private boolean check(String tree, int left, int right, boolean parentIsZero) {
        // no nodes to check
        if (left > right) return true;

        // root of tree
        int mid = (left + right) / 2;
        char cur = tree.charAt(mid);

        // parent = 0, cur = 1 is impossible
        if (parentIsZero && (cur == '1')) return false;

        // current node -> new parent node
        boolean curIsZero = (cur == '0');

        // recursion
        return check(tree, left, mid - 1, curIsZero)
            && check(tree, mid + 1, right, curIsZero);
    }
}