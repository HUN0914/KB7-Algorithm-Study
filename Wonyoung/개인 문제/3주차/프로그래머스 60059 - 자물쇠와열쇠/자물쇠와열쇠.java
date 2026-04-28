import java.util.*;

class Solution {
    public static int M,N;
    public boolean solution(int[][] key, int[][] lock) {        
        M = key.length; 
        N = lock.length;
        
        int lockCnt = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(lock[i][j] == 0) lockCnt++;
            }
        }

        if(lockCnt == 0) return true;
        
        int[][] currentKey = key;
        for(int i = 0; i < 4; i++){
            for(int dr = -M + 1; dr < N; dr++){
                for(int dc = -M+1; dc < N; dc++){
                    if(isMatched(dr, dc, currentKey, lock, lockCnt)){
                        return true;
                    }
                }
            }
            currentKey = rotate90(currentKey);
        }
        
        return false;
    }
    
    
    public static int[][] rotate90(int[][] key){
        int[][] res = new int[M][M];
        for(int i = 0; i < M; i++){
            for(int j = 0; j < M; j++){
                res[j][M - 1 - i] = key[i][j];
            }
        }
        return res;
    }
    
    public static boolean isMatched(int dr, int dc, int[][] key, int[][] lock, int lockCnt){
        int cnt = 0;
        for(int i = 0; i < M; i++){
            for(int j = 0; j < M; j++){
                int nr = i + dr;
                int nc = j + dc;
                
                if(inBoard(nr, nc)){
                    if(key[i][j] == 1 && lock[nr][nc] == 1) return false;
                    
                    if(key[i][j] == 1 && lock[nr][nc] == 0) cnt++;
                }
            }
        }
        
        return cnt == lockCnt;
    }
    
    public static boolean inBoard(int r, int c){
        return 0 <= r && r < N && 0 <= c && c < N; 
    }
}