import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] dist = new int[N][N];
        
        for (int[] row: dist)
            Arrays.fill(row, N);
        for (int i = 0; i < N; i++) {
            dist[i][i] = 0;
        }

        for (int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());

            int A = Integer.parseInt(st.nextToken()) - 1;
            int B = Integer.parseInt(st.nextToken()) - 1;

            dist[A][B] = 1;
            dist[B][A] = 1;
        }
        
        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    dist[i][j] = Math.min(dist[i][k] + dist[k][j], dist[i][j]);
                    dist[j][i] = Math.min(dist[i][k] + dist[k][j], dist[i][j]);
                }
            }
        }
        
        int ret = 0;
        int min_sum = N * N;
        for (int i = 0; i < N; i++){
            int sum = Arrays.stream(dist[i]).sum();
            if (sum < min_sum) {
                ret = i + 1;
                min_sum = sum;
            }
        }

        System.out.println(ret);
    }    
}
