import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static int[][] works;
    public static int minValue = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 최대 20개 중 10개를 선택 = 20C10 = 184,756개
        // 조합을 활용한 Bruto Force다. 
        N = Integer.parseInt(st.nextToken());
        works = new int[N][N];

        for(int i=0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++){
                works[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=0; i <= N / 2; i++){
            boolean[] checked = new boolean[N];
            collections(i, 0, checked);
        }

        System.out.println(minValue);

    }

    public static void collections(int index, int count, boolean[] checked){
        if(count == N/2){
            minValue = Math.min(minValue, calcDiff(checked));
        }

        for(int i = index + 1; i < N; i++){
            checked[i] = true;
            collections(i, count+1, checked);
            checked[i] = false;
        }
    }
    
    public static int calcDiff(boolean[] checked){
        List<Integer> morning = new ArrayList<>();
        List<Integer> dinner = new ArrayList<>();
        for(int i=0; i < N; i++){
            if(checked[i]){
                morning.add(i);
            } else {
                dinner.add(i);
            }
        }

        int morningSum = 0, dinnerSum = 0;
        for(int j=0; j< N/2; j++){
            for(int k=0; k < N/2; k++){
                if(j == k) continue;

                int a = morning.get(j);
                int b = morning.get(k);
                morningSum += works[a][b];

                int c = dinner.get(j);
                int d = dinner.get(k);
                dinnerSum += works[c][d];
            }
        }

        return Math.abs(morningSum - dinnerSum);
    }

}