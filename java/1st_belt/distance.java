/*
Challenge #3

Write a program to calculate the distance between two points in a 2D plane.

The distance between two points (x1, y1) and (x2, y2) in a plane is given by the formula:
D = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )

Where:
- (x1, y1) and (x2, y2) are the coordinates of the two points.
- D is the distance between the two points.

Input Format: 
The program will take four integer inputs: x1, y1, x2, y2, each on a separate line, 
representing the coordinates of two points.

Output Format: 
The program will output the distance between the two points, rounded to two decimal places.
*/

import java.util.Scanner;

public class Solution {
    public static double calculateDistance(double x1, double y1, double x2, double y2) {
        // Implement the formula here
        double distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        return distance; 
    }

    public static void mainFunction() {
        Scanner sc = new Scanner(System.in);

        double x1 = sc.nextDouble();
        double y1 = sc.nextDouble();
        double x2 = sc.nextDouble();
        double y2 = sc.nextDouble();

        double distance = calculateDistance(x1, y1, x2, y2);
        System.out.printf("%.2f\n", distance);

        sc.close();
    }

    public static void main(String[] args) {
        mainFunction();
    }
}
