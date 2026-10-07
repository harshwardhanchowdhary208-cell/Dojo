/*
Question:
Given a string and a suffix, count how many times the suffix appears at
the end of the string.

Input:
A string S and a suffix X.

Output:
Print the number of times X appears as a suffix of S.
*/

import java.util.Scanner;

public class SuffixCount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String suffix = sc.next();

        int count = 0;
        int start = s.length();

        while (start >= suffix.length()) {
            String current = s.substring(start - suffix.length(), start);
            if (current.equals(suffix)) {
                count++;
                start -= suffix.length();
            } else {
                break;
            }
        }

        System.out.println(count);
        sc.close();
    }
}
