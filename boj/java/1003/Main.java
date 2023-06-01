import java.util.HashMap;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static HashMap<Integer, Integer[]> counts;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());

            counts = new HashMap<Integer, Integer[]>();
            counts.put(0, new Integer[] {1, 0});
            counts.put(1, new Integer[] {0, 1});

            System.out.println(Integer.toString(count_fib(n)[0]) + " " + Integer.toString(count_fib(n)[1]));
        }

    }

    static Integer[] count_fib(int n) {
        if (counts.containsKey(n))
            return counts.get(n);
        
        Integer[] r1 = count_fib(n - 1);
        Integer[] r2 = count_fib(n - 2);
        Integer[] ret = new Integer[] {
            r1[0] + r2[0],
            r1[1] + r2[1]
        };
        counts.put(n, ret);

        return ret;
    } 

}