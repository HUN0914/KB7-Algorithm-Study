import java.util.*;
import java.io.*;

public class Main {
    public static int L, N, Q, answer;
    public static int[][] chess, warriorField;
    // 위: 0, 오른쪽: 1, 아래: 2, 왼쪽: 3
    public static int[][] directions = {{-1,0},{0,1},{1,0},{0,-1}};
    public static Map<Integer, int[]> warriors;
    public static Map<Integer, Integer> dameges;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        warriors = new HashMap<>();
        dameges = new HashMap<>();

        L = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        chess = new int[L][L];
        for(int i = 0; i < L; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < L; j++) chess[i][j] = Integer.parseInt(st.nextToken());
        }

        int warrior = 0;
        warriorField = new int[L][L];
        while(N-- > 0){
            st = new StringTokenizer(br.readLine());

            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            ++warrior;
            for(int i = r-1; i < r - 1 + h; i++){
                for(int j = c-1; j < c-1 + w; j++){
                    warriorField[i][j] = warrior;
                }
            }

            warriors.put(warrior, new int[]{r-1,c-1,h,w,k});
        }

        while(Q-- > 0){
            st = new StringTokenizer(br.readLine());

            int id = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            // 명령을 내리는 함수 - 얘가 살아있나?
            if(warriors.containsKey(id) && command(id, d)){
                // 이동            
                moveWarrior(id, d, true);
            }
        }
        // 남은 기사들의 깎인 체력 총 합을 구한다.
        for(Map.Entry<Integer, Integer> damege: dameges.entrySet()) answer += damege.getValue();
        System.out.println(answer);
    }

    public static boolean command(int id, int d){
        int[] loc = warriors.get(id);
        int r = loc[0], c = loc[1], h = loc[2], w = loc[3], k = loc[4];
        int nr = directions[d][0], nc = directions[d][1];

        boolean flag = true;

        for(int i = r; i < r + h; i++){
            for(int j = c; j < c + w; j++){
                if(!inChess(i + nr, j + nc) || chess[i + nr][j + nc] == 2){
                    return false;
                }

                // 다른 기사와 부딪치는 경우
                if(warriorField[i + nr][j + nc] > 0 && warriorField[i + nr][j + nc] != id){
                    flag = command(warriorField[i + nr][j + nc], d);
                }

                if(!flag) return false;
            }
        }

        return flag;
    }

    public static void moveWarrior(int id, int d, boolean cmd){
        int[] loc = warriors.get(id);
        int r = loc[0], c = loc[1], h = loc[2], w = loc[3], k = loc[4];
        int nr = directions[d][0], nc = directions[d][1];

        // 다른 기사와 부딪치는 경우
        for(int i = r; i < r + h; i++){
            for(int j = c; j < c + w; j++){
                if(warriorField[i + nr][j + nc] > 0 && warriorField[i + nr][j + nc] != id){
                    moveWarrior(warriorField[i + nr][j + nc], d, false);
                }
            }
        }

        for(int i = r; i < r + h; i++){
            for(int j = c; j < c + w; j++){
                warriorField[i][j] = 0;
            }
        }

        for(int i = r; i < r + h; i++){
            for(int j = c; j < c + w; j++){
                warriorField[i + nr][j + nc] = id;
            }
        }

        warriors.put(id, new int[]{r + nr, c + nc, h, w, k});

        // 이동 후 함정수만큼 체력 갈기 그리고 여부에 따라 지우기 -> 정지해 있는 상태에선 밟고 있어도 체력이 안 갈린다.
        // 명령을 받은 기사의 경우, 체력이 갈리지 않음
        if(!cmd){
            int remove = downHP(id);
            if(remove > 0){
                int value = dameges.getOrDefault(id, 0);
                dameges.put(id, value + remove);
            }
        }
    }

    public static int downHP(int id){
        int cnt = 0;
        int[] loc = warriors.get(id);
        int r = loc[0], c = loc[1], h = loc[2], w = loc[3], k = loc[4];
        
        for(int i = r; i < r + h; i++){
            for(int j = c; j < c + w; j++){
                if(chess[i][j] == 1) cnt++;
            }
        }

        if(k <= cnt){
            warriors.remove(id);
            dameges.remove(id);

            for(int i = r; i < r + h; i++){
                for(int j = c; j < c + w; j++){
                    warriorField[i][j] = 0;
                }
            }
            return -1;
        }

        warriors.put(id, new int[]{r, c, h, w, k - cnt});
        return cnt;
    }

    public static boolean inChess(int r, int c){
        return 0 <= r && r < L && 0 <= c && c < L;
    }
}