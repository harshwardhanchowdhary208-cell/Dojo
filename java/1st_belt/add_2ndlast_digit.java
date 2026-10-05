/*
Challenge #11

Imagine you have two numbers num1 and num2.
Your task is to find the second-to-last digit of each number.
If the numbers are valid, you'll add these two special digits together. 
But if either number is too small to have a second-to-last digit, you'll say it's an "Invalid number".

Steps:
1. Choose two numbers.
2. Check if these numbers are valid.
3. Find the second-to-last digit of each number.
4. Add these digits together.
5. If either number is too small (either of the number is less than 10 or a negative number), print it's an "Invalid number".

Example 1:
Input:
123423
123456

Output:
7
*/

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Read the two input numbers
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        
        // Check if either number is less than 10 or negative
        if (n1 < 10 || n2 < 10) {
            System.out.println("Invalid number");
        } else {
            // Find the second-to-last digit of each number
            int digit1 = (n1 / 10) % 10;
            int digit2 = (n2 / 10) % 10;
            
            // Add the digits together and print the sum
            int sum = digit1 + digit2;
            System.out.println(sum);
        }
        
        sc.close();
    }
}
