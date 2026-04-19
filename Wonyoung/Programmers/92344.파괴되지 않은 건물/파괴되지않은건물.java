import java.util.*;

class Solution {   
    public int solution(int[][] board, int[][] skill) {
        int N = board.length;
        int M = board[0].length;
        
        int[][] prefix = new int[N+1][M+1];
        
        for(int[] turn : skill){
            int damage = turn[0] == 2 ? turn[5] : turn[5]*(-1);
            int r1 = turn[1], c1 = turn[2], r2 = turn[3], c2 = turn[4];
            
            prefix[r1][c1] += damage;
            prefix[r2 + 1][c1] -= damage;
            prefix[r1][c2 + 1] -= damage;
            prefix[r2 + 1][c2 + 1] += damage;
        }
        
        
        for(int i = 1; i <= N; i++){
            for(int j = 0; j <= M; j++){
                prefix[i][j] += prefix[i-1][j];
            }
        }
        
        for(int j = 1; j <= M; j++){
            for(int i = 0; i <= N; i++){
                prefix[i][j] += prefix[i][j - 1];
            }
        }
                
        
        int answer = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(board[i][j] + prefix[i][j] > 0) answer++;
            }
        }
        return answer;
    }
    
}