import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[][] timetable = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            timetable[i][0] = Integer.parseInt(st.nextToken());
            timetable[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(timetable, (o1, o2) -> {
            if (o1[1] != o2[1]) return Integer.compare(o1[1], o2[1]); // end time of meeting 
            return Integer.compare(o1[0], o2[0]);
        });

        int end = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (timetable[i][0] < end) continue; // cannot add meeting

            end = timetable[i][1]; // add meeting
            cnt++;
        }

        System.out.println(cnt);
    }
}