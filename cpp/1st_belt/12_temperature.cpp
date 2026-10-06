/*
Question:
Write a program to read the temperature in centigrade and display a
suitable message according to the temperature state below.

Temp < 0: Freezing weather
Temp 0-10: Very cold weather
Temp 11-20: Cold weather
Temp 21-30: Normal in temp
Temp 31-40: It's hot
Temp > 40: It's very hot
*/

#include <iostream>
using namespace std;

int main() {
    int temp;
    cin >> temp;

    if (temp < 0) {
        cout << "Freezing weather";
    } else if (temp <= 10) {
        cout << "Very cold weather";
    } else if (temp <= 20) {
        cout << "Cold weather";
    } else if (temp <= 30) {
        cout << "Normal in temp";
    } else if (temp <= 40) {
        cout << "It's hot";
    } else {
        cout << "It's very hot";
    }

    return 0;
}
