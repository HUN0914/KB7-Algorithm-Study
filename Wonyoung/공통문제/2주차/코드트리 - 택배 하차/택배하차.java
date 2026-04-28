import java.util.*;
import java.io.*;

public class Main {
    public static int N,M;
    public static Map<Integer, int[]> posts;
    public static int[] checked;
    public static int[][] truckSpace;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        checked = new int[N];
        posts = new HashMap<>();

        for(int i=0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            // 높이, 너비, 왼쪽 col, 시작 row(예정)
            int[] postInfo = new int[]{h, w, c-1, 0};
            posts.put(k, postInfo);

            // 1. k개의 택배를 떨어뜨린다.
            stackPost(k, h, w, c - 1);
        }

        // 2. 왼쪽/오른쪽 하차
        while(!posts.isEmpty()){
            left();
            right();
        }
    }

    public static void stackPost(int k, int h, int w, int c) {
        int stuckRow = 0;
        // 가장 높은 곳에 걸리는 위치를 탐색
        for(int i = c; i < c + w; i++) stuckRow = Math.max(stuckRow, checked[i]);

        // 해당 위치에 택배를 위치시킴
        for(int i = c; i < c + w; i++) checked[i] = stuckRow + h;
        int[] post = posts.get(k);
        post[3] = stuckRow;
        posts.put(k, post);
    }

    public static void left(){
        // 1. 각 택배를 탐색하여 왼쪽에서 뺄 수 있는 번호들을 조회
        List<Integer> remove = new ArrayList<>();

        for(Map.Entry<Integer, int[]> post : posts.entrySet()){
            // 1) 해당 택배의 정보를 추출
            int key = post.getKey();
            int[] info = post.getValue();
            boolean flag = true;

            // 2) 다른 택배를 순회하며 정보를 비교
            for(Map.Entry<Integer, int[]> otherPost : posts.entrySet()){
                int okey = otherPost.getKey();
                int[] oinfo = otherPost.getValue();
                if(key != okey && isLeftOverlapped(key, okey, info, oinfo)){
                    flag = false;
                    break;
                }
            }

            if(flag) remove.add(key);
        }

        // 2. 제거
        int minNum = 100;
        for(int num : remove) minNum = Math.min(num, minNum);
        int[] removeInfo = posts.get(minNum);
        int colStart = removeInfo[2], colEnd = removeInfo[2] + removeInfo[1];
        posts.remove(minNum);

        System.out.println(minNum);

        // 3. 재조정
        relocation();
    }

    public static void right(){
        // 1. 각 택배를 탐색하여 왼쪽에서 뺄 수 있는 번호들을 조회
        List<Integer> remove = new ArrayList<>();
        for(Map.Entry<Integer, int[]> post : posts.entrySet()){
            // 1) 해당 택배의 정보를 추출
            int key = post.getKey();
            int[] info = post.getValue();
            boolean flag = true;

            // 2) 다른 택배를 순회하며 정보를 비교
            for(Map.Entry<Integer, int[]> otherPost : posts.entrySet()){
                int okey = otherPost.getKey();
                int[] oinfo = otherPost.getValue();
                if(key != okey && isRigtOverlapped(key, okey, info, oinfo)){
                    flag = false;
                    break;
                }
            }
            if(flag) remove.add(key);
        }

        // 2. 제거
        int minNum = 100;
        for(int num : remove) minNum = Math.min(num, minNum);
        int[] removeInfo = posts.get(minNum);
        int colStart = removeInfo[2], colEnd = removeInfo[2] + removeInfo[1];
        posts.remove(minNum);

        System.out.println(minNum);

        // 3. 재조정
        relocation();

    }

    public static void relocation(){
        truckSpace = new int[N][N];
        for(Map.Entry<Integer, int[]> post : posts.entrySet()){
            // 1) 해당 col에 걸리는 택배에 대한 위치 정보를 추출
            int key = post.getKey();
            int[] loc = post.getValue();
            // 높이, 너비, 왼쪽 col, 시작 row
            int h = loc[0], w = loc[1], c = loc[2], r = loc[3];

            for(int i = r; i < r + h; i++){
                for(int j = c; j < c + w; j++){
                    truckSpace[i][j] = key;
                }
            }
        }

        // 2. 중복을 없애기 위해 row 기준 위에서부터
        // 각 택배들을 순회하면서 나아갈 수 있는지에 대한 검사
        boolean[] checkPost = new boolean[101];
        for(int i = 1; i < N; i++){
            for(int j = 0; j < N; j++){
                if(truckSpace[i][j] > 0){
                    int num = truckSpace[i][j];
                    if(!checkPost[num]){
                        checkAndMovePost(num);
                        checkPost[num] = true;
                    }
                }
            }
        }
    }


    public static void checkAndMovePost(int key){
        int[] loc = posts.get(key);
        // 높이, 너비, 왼쪽 col, 시작 row
        int h = loc[0], w = loc[1], c = loc[2], r = loc[3];

        // 1) 각 화물 입장에서 가장 적게 나아갈 수 있는 높이 구하기(minHeight)
        int minHeight = 50;
        for(int i=c; i < c+w; i++){
            int cnt = 0;
            for(int j = r-1; j >= 0; j--){
                if(truckSpace[j][i] != 0) break;
                cnt++;
            }
            minHeight = Math.min(cnt, minHeight);
        }

        // 이동할 수 있는 빈 공간이 있다면
        if(minHeight > 0){
            posts.put(key, new int[]{h, w, c, r - minHeight});
            for(int i=c; i < c+w; i++){
                for(int j=r; j < r+h; j++){
                    truckSpace[j-minHeight][i] = truckSpace[j][i];
                    truckSpace[j][i] = 0;
                }
            }
        }
    }

    // right - 택배의 경로에 다른 택배가 걸리는지 여부
    public static boolean isRigtOverlapped(int key, int okey, int[] info, int[] oinfo){
        // 높이, 너비, 왼쪽 col, 시작 row
        int sr = info[3], er = info[3] + info[0];
        int sc = info[2], ec = N-1;
        int osr = oinfo[3], oer = oinfo[3] + oinfo[0];
        int osc = oinfo[2], oec = oinfo[2] + oinfo[1];

        if(oec > sc && ((osr <= sr && sr < oer) || (oer >= er && er > osr))) return true;
        return false;
    }

    // left - 택배의 경로에 다른 택배가 걸리는지 여부
    public static boolean isLeftOverlapped(int key, int okey, int[] info, int[] oinfo){
        // 높이, 너비, 왼쪽 col, 시작 row
        int sr = info[3], er = info[3] + info[0];
        int sc = 0, ec = info[2] + info[1];
        int osr = oinfo[3], oer = oinfo[3] + oinfo[0];
        int osc = oinfo[2], oec = oinfo[2] + oinfo[1];

        if(osc < ec && ((osr <= sr && sr < oer) || (oer >= er && er > osr))) return true;
        return false;
    }
}