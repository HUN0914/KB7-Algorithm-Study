import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n + 1];
        for (int day = 0; day < n; day++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int time = Integer.parseInt(st.nextToken());
            int profit = Integer.parseInt(st.nextToken());

            dp[day + 1] = Math.max(dp[day + 1], dp[day]);

            int endDay = day + time;

            if (endDay <= n) {
                dp[endDay] = Math.max(dp[endDay], dp[day] + profit);
            }
        }

        System.out.println(dp[n]);
    }
}