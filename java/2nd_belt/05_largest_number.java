/*
Question:
Given N integers, find the largest number in the list.

Input:
The first line contains an integer N.
The second line contains N integers.

Output:
Print the largest number.
*/

import java.util.Scanner;

public class LargestNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int largest = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            int value = sc.nextInt();
            if (value > largest) {
                largest = value;
            }
        }

        System.out.println(largest);
        sc.close();
    }
}
