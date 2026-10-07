/*
Question:
Write a program to find the least common multiple (LCM) of two numbers.

Input:
Two integers A and B.

Output:
Print the LCM of A and B.
*/

import java.util.Scanner;

public class LCM {
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

        int lcm = (a / gcd(a, b)) * b;
        System.out.println(lcm);
        sc.close();
    }
}
