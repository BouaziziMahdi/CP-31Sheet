package JaggedSwaps;

import java.util.*;

public class Main {
    public static int kid(int[] array, int n) {
        int res = Math.abs(array[0]);
        for (int x : array) {
            if (Math.abs(x) < res) {
                res = Math.abs(x);
            }
        }
        return res;
    }

    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();      
        int[] array = new int[n];

        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        System.out.println(kid(array, n));
    }
}
