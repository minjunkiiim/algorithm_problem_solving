import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int k = (int) Math.pow(2, N - 1);

        int ret = 0;
        while (k > 0) {
            if (r / k == 1) 
                ret += 2 * k * k;

            if (c / k == 1)
                ret += k * k;

            r %= k;
            c %= k;
            
            k /= 2;
        }

        System.out.println(ret);
    }
}
