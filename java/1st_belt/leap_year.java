/*
Challenge #3: Leap Year

You are given a year as input. A leap year is defined as a year that has 366 days. 
Write a program that outputs "leap year" if the input year is a leap year and "not leap year" otherwise.

A year is a leap year if it satisfies the following conditions:
- It is divisible by 4.
- If it is divisible by 100, it must also be divisible by 400.

Example 1:
Input: 2020
Output: leap year
*/

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int year = sc.nextInt();
            
            // A year is a leap year if it is divisible by 4, 
            // but not by 100 unless it is also divisible by 400.
            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                System.out.println("leap year");
            } else {
                System.out.println("not leap year");
            }
        }
        sc.close();
    }
} 
