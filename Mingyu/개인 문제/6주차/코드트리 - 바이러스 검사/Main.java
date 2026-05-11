import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] cust = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            cust[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int ldr = Integer.parseInt(st.nextToken());
        int mbr = Integer.parseInt(st.nextToken());

        long answer = 0;

        for (int c : cust) {
            answer++;

            int rest = c - ldr;
            if (rest > 0) {
                answer += (rest + mbr - 1) / mbr;
            }
        }

        System.out.println(answer);
    }
}