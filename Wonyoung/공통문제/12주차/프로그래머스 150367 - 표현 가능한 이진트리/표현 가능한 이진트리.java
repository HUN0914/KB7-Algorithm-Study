import java.util.*;

class Solution {
    public int[] solution(long[] numbers) {
        int N = numbers.length;
        int[] answer = new int[N];
        
        for(int i = 0; i < N; i++){
            String binStr = Long.toBinaryString(numbers[i]);
            int len = binStr.length();
            
            String result = (len & (len + 1)) == 0 ? binStr 
                : "0".repeat(addZero(len)) + binStr;
            
            int length = result.length();
            answer[i] = isBinaryTree(result, length / 2 + 1, length / 2) ? 1: 0;
        }
        
        return answer;
    }
    
    public static int addZero(int len){
        int num = 1;
        while(num <= len) num *= 2;
        return num - 1 - len;
    }
    
    public static boolean isBinaryTree(String result, int size, int loc) {
        if (size == 1) return true;

        int newSize = size / 2;
        int leftIdx = loc - newSize;
        int rightIdx = loc + newSize;

        if (result.charAt(loc) == '0') {
            if (result.charAt(leftIdx) == '1' || result.charAt(rightIdx) == '1') {
                return false;
            }
        }

        boolean leftValid = isBinaryTree(result, newSize, leftIdx);
        boolean rightValid = isBinaryTree(result, newSize, rightIdx);

        return leftValid && rightValid;
    }
}