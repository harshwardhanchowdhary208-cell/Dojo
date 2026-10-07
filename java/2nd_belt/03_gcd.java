/*
Question:
Write a program to find the greatest common divisor (GCD) of two integers.

Input:
Two integers A and B.

Output:
Print the GCD of A and B.
*/

import java.util.Scanner;

public class GCD {
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(gcd(a, b));
        sc.close();
    }
}
