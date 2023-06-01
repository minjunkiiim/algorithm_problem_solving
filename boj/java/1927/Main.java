import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    class Heap {
        public int size;
        public int[] arr;

        Heap(int N) {
            this.size = 0;
            this.arr = new int[N];
        }
        private int parent(int x) {
            return (x + 1) / 2 - 1;
        }
        private int left(int x) {
            return (x + 1) * 2 - 1;
        }
        private int right(int x) { 
            return (x + 1) * 2;
        }
        public void insert(int x) {
            arr[size++] = x;

            int curr = size - 1;
            int p = parent(curr);
            while (curr > 0 || arr[curr] < arr[p]) {
                int tmp = arr[curr];
                arr[curr] = arr[p];
                arr[p] = tmp;
                
                curr = p;
                p = parent(curr);
            }
        }

        public int pop() {
            int popped = arr[0];

            arr[0] = arr[--size];

            int curr = 0;
            
            return popped;
        }
    } 
    public static void main(String args[]) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        Heap heap = new Heap(N);

        for (int n = 0; n < N; n++) {
            int x = Integer.parseInt(br.readLine());

            if (x == 0) {
                System.out.println(Heap.pop());
            }
            else {
                Heap.add(x);
            }

        }
    }    
}
