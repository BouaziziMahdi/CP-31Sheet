package SequenceGame;

import java.util.ArrayList;
import java.util.Scanner;

public class SequenceGame {


    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();  

        while (t-- > 0) {
            int n = sc.nextInt();       
            int[] b = new int[n];

            for (int i = 0; i < n; i++) {
                b[i] = sc.nextInt();
            }

            int[] a = buildSequence(b);

            System.out.println(a.length);
            for (int i = 0; i < a.length; i++) {
                if (i > 0) System.out.print(" ");
                System.out.print(a[i]);
            }
            System.out.println();
        }

        sc.close();
    }
    public static int[] buildSequence(int[] b) {
        ArrayList<Integer> res = new ArrayList<>();

        res.add(b[0]);

        for (int i = 1; i < b.length; i++) {
            res.add(b[i]);

            if (b[i] < b[i - 1]) {
                res.add(b[i]);
            }
        }
        int[] out = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            out[i] = res.get(i);
        }
        return out;
    }
}

