/*
Challenge #8
Let's learn how to find a specific letter in a name using a computer program.

Your Task:
Imagine you're counting the letters in a name from left to right, starting with 0. 
Your job is to find the letter that comes at the 4th spot. Here's how you can do it:

1. Ask for the Name: First, you'll ask the person to type in a name.
2. Find the Letter: Once you have the name, you'll use your magic tool to find the letter at the 4th spot.
3. Show the Letter: Finally, you'll show the letter you found to the person.

Example 1:
Input: Austin
Output: t
*/

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();
        char x = n.charAt(3);
        System.out.println(x);
    }
}
