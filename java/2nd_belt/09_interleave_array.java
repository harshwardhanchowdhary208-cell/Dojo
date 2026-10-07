/*
Question:
Given two arrays of equal length, interleave their elements in alternating
order.

Example:
A = [1, 3, 5]
B = [2, 4, 6]
Output: 1 2 3 4 5 6

Input:
Two arrays of equal size.

Output:
Print the interleaved array elements.
*/

import java.util.Scanner;

public class InterleaveArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] a = new int[n];
        int[] b = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            b[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            System.out.print(a[i] + " ");
            System.out.print(b[i] + (i == n - 1 ? "" : " "));
        }
        System.out.println();

        sc.close();
    }
}
