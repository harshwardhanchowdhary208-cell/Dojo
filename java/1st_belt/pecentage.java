/*
Challenge #5

You are given the marks obtained by a student and the total (maximum) marks. 
Your task is to calculate the percentage scored and print it rounded to two decimal places.

The percentage is calculated using the formula:
percentage = (marks_obtained / total_marks) * 100

Use floating-point division, not integer division.

Input Format:
- A single line containing two space-separated integers marks_obtained and total_marks

Output Format:
- Print the percentage scored, rounded to two decimal places.
*/

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Read marks_obtained and total_marks
        int marks_obtained = sc.nextInt();
        int total_marks = sc.nextInt();
        
        // Calculate and print percentage to 2 decimal places
        float percentage = ((float)marks_obtained / total_marks) * 100.0f;
        System.out.printf("%.2f\n", percentage);
    }
}
