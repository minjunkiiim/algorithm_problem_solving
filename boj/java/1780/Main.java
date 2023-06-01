import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class Main {
    
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int r1 = 0;
        int r2 = N;
        int c1 = 0;
        int c2 = N;

        int[] ret = search(arr, r1, r2, c1, c2);
        for (int i = 0; i < 3; i++)
            System.out.println(ret[i]);
    }

    public static int[] search(int[][] arr, int r1, int r2, int c1, int c2) {
        int[] ret = new int[] {0, 0, 0};
        
        int num = arr[r1][c1];
        boolean flag = true;
        for (int i = r1; i < r2; i++) {
            for (int j = c1; j < c2; j++) {
                if (arr[i][j] != num) {
                    flag = false;
                    break;
                }
            }
            if (!flag)
                break;
        }

        if (flag) {
            ret[num + 1]++;
            return ret;
        }

        int k = (r2 - r1) / 3;
        for (int r = r1; r < r2; r += k) {
            for (int c = c1; c < c2; c += k) {
                int[] s = search(arr, r, r + k, c, c + k);
                for (int i = 0; i < 3; i++) {
                    ret[i] += s[i];
                }
            }
        }

        return ret;
    }
}
