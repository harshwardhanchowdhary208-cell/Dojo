/*
Question:
Print the following pattern using loops:

1
12
123
1234
12345

Input:
A single integer N representing the number of rows.

Output:
Print the pattern of increasing numbers.
*/

import java.util.Scanner;

public class Pattern12345 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }
            System.out.println();
        }

        sc.close();
    }
}
