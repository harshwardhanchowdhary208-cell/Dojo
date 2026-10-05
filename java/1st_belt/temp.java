/*
Challenge #1

Write a program that converts a temperature from Celsius to Fahrenheit or vice versa.

You need to convert a temperature based on the unit provided by the user (either Celsius or Fahrenheit). 
The program should ask the user to specify the temperature unit (Celsius or Fahrenheit) and then perform the conversion.

Formulas:
Celsius to Fahrenheit: F = (C * 9 / 5) + 32
Fahrenheit to Celsius: C = (F - 32) * 5 / 9

Input Format:
The first line of input contains a floating point number for temperature.
The second line of input contains the unit of the input temperature ('C' for Celsius or 'F' for Fahrenheit).

Output Format:
The program will output the converted temperature rounded to two decimal places.
*/

import java.util.Scanner;

public class Solution {
    public static void convertTemperature(float temp, char unit) {
        // Implement logic here
        if (unit == 'F') {
            float result = (temp - 32) * 5.0f / 9.0f;
            System.out.printf("%.2f\n", result);
        }
        else if (unit == 'C') {
            float result = (temp * 9.0f / 5.0f) + 32;
            System.out.printf("%.2f\n", result);
        }
    }

    public static void main(String[] args) {
        // Call the function after taking input
        Scanner scanner = new Scanner(System.in);
        float temp = scanner.nextFloat();
        char unit = scanner.next().charAt(0);
        convertTemperature(temp, unit);
    }
}
