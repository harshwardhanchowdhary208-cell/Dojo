/*
Question:
Write a program that takes N integers as input and checks whether the
sequence is in ascending order.

A sequence is considered ascending if every element is less than or equal
to the next element.

Input:
The first line contains an integer N.
The second line contains N space-separated integers.

Output:
Print "Yes" if the sequence is ascending, otherwise print "No".
*/

import java.util.Scanner;

public class AscendingOrder {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        boolean ascending = true;
        for (int i = 1; i < n; i++) {
            if (arr[i] < arr[i - 1]) {
                ascending = false;
                break;
            }
        }

        System.out.println(ascending ? "Yes" : "No");
        sc.close();
    }
}
