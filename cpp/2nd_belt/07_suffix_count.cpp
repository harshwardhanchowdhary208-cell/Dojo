/*
Question:
You are given a list of words and a suffix string. Your task is to count
how many words in the list end with the given suffix.

A suffix is a group of characters present at the end of a word.

Print the total number of words that have the given suffix.

Input:
The first line contains an integer N — the number of words.
The next input contains N words followed by the suffix string.
*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        cin >> words[i];
    }

    string suffix;
    cin >> suffix;

    int count = 0;

    for (const string& word : words) {
        if (word.size() >= suffix.size() &&
            word.compare(word.size() - suffix.size(), suffix.size(), suffix) == 0) {
            count++;
        }
    }

    cout << count;

    return 0;
}
