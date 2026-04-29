import java.io.*;
import java.util.*;

public class Main {
    static long a, b, c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        a = Long.parseLong(st.nextToken());
        b = Long.parseLong(st.nextToken());
        c = Long.parseLong(st.nextToken());

        System.out.println(pow(a, b));
    }

    static long pow(long a, long b) {
        if (b == 1) {
            return a % c;
        }

        long half = pow(a, b / 2);

        long result = (half * half) % c;

        if (b % 2 == 1) {
            result = (result * (a % c)) % c;
        }

        return result;
    }
}