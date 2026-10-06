/*
Question:
Write a program that takes the user's choice as input and prints the
corresponding snack from the vending machine. If the choice is invalid,
print "Invalid choice!".

The vending machine has the following "delights":

1: Broccoli-flavoured ice cream
2: Chocolate-covered onions
3: Spicy marshmallows
4: Fizzy pickle juice
5: Exit (to save yourself from regret)

Input Format:
A single integer between 1 and 5 representing the user's choice.

Output Format:
The snack name corresponding to the selected choice, or "Invalid choice!"
if the input is outside the range 1-5.
*/

#include <iostream>
#include <string>
using namespace std;

string vendingMachine(int choice) {
    switch (choice) {
        case 1:
            return "Broccoli-flavoured ice cream";
        case 2:
            return "Chocolate-covered onions";
        case 3:
            return "Spicy marshmallows";
        case 4:
            return "Fizzy pickle juice";
        case 5:
            return "Exit";
        default:
            return "Invalid choice!";
    }
}

int main() {
    int choice;
    cin >> choice;

    cout << vendingMachine(choice);

    return 0;
}
