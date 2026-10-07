/*
Question:
Print the following pattern using loops:

55555
55555
55555
55555
55555

Input:
A single integer N denoting the number of rows.

Output:
Print the pattern of repeated 5s.
*/

import java.util.Scanner;

public class Pattern55555 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.println("55555");
        }

        sc.close();
    }
}
