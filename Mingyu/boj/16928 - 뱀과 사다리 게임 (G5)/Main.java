import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // ladder
        int m = Integer.parseInt(st.nextToken()); // snake

        int[] teleport = new int[101]; // TP space (ladder + snake)
        for (int i = 0; i < n + m; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            teleport[from] = to;
        }

        int[] dist = new int[101];
        Arrays.fill(dist, -1);

        Queue<Integer> q = new ArrayDeque<>();
        q.offer(1); // start
        dist[1] = 0;

        while (!q.isEmpty()) {
            int cur = q.poll();

            if (cur == 100) break;

            for (int dice = 1; dice <= 6; dice++) {
                int next = cur + dice; // dice can be 1 to 6

                if (next > 100) continue;

                if (teleport[next] != 0) { // teleport if ladder or snake
                    next = teleport[next];
                }

                if (dist[next] != -1) continue;

                dist[next] = dist[cur] + 1;
                q.offer(next);
            }
        }

        System.out.println(dist[100]);
    }
}