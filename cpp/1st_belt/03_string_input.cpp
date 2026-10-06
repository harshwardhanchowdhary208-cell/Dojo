/*
Question:
Read a string from the input and print it in the following form:

You entered: <input string>

The input string may contain uppercase letters, lowercase letters,
digits, spaces, and special characters.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
    string n;
    getline(cin, n);

    cout << "You entered: " << n;

    return 0;
}
