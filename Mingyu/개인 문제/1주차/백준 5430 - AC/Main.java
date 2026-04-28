import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tc = Integer.parseInt(br.readLine());

        while (tc-- > 0) { 
            String cmdList = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String arr = br.readLine();

            Deque<Integer> dq = new ArrayDeque<>();
            StringTokenizer st = new StringTokenizer(arr, "[],");

            while (st.hasMoreTokens()) {
                dq.offer(Integer.valueOf(st.nextToken()));
            }

            boolean reversed = false;
            boolean error = false;

            for (int i = 0; i < cmdList.length(); i++) {
                char cmd = cmdList.charAt(i);

                if (cmd == 'R') {
                    reversed = !reversed;
                } else {
                    if (dq.isEmpty()) {
                        error = true;
                        break;  
                    }

                    if (!reversed) dq.pollFirst();
                    else dq.pollLast();
                }
            }

            if (error) {
                sb.append("error\n");
            } else {
                sb.append('[');
                while (!dq.isEmpty()) {
                    sb.append(!reversed ? dq.pollFirst() : dq.pollLast());
                    if (!dq.isEmpty()) sb.append(',');
                }
                sb.append("]\n");
            }
        }

        System.out.println(sb);
    }
}