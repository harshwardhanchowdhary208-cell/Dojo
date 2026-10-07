/*
Question:
A number is an Armstrong number if the sum of each digit raised to the
power of the number of digits equals the original number.

Example:
153 = 1^3 + 5^3 + 3^3 = 153

Input:
A single integer N.

Output:
Print "Armstrong" if the number is Armstrong, otherwise print "Not Armstrong".
*/

import java.util.Scanner;

public class ArmstrongNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int original = n;
        int digits = 0;
        int temp = n;

        while (temp != 0) {
            digits++;
            temp /= 10;
        }

        int sum = 0;
        temp = n;

        while (temp != 0) {
            int digit = temp % 10;
            int power = 1;

            for (int i = 0; i < digits; i++) {
                power *= digit;
            }

            sum += power;
            temp /= 10;
        }

        System.out.println(sum == original ? "Armstrong" : "Not Armstrong");
        sc.close();
    }
}
