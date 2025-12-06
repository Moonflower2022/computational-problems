#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int argmax(vector<int>& array, int i1, int i2) {
    vector<int>::iterator max_iterator = max_element(array.begin() + i1, array.begin() + i2);
    return distance(array.begin(), max_iterator);
}

int main() {
    ifstream puzzle_input("puzzle_input.txt");
    string bank_string;

    int total_joltage = 0;

    while (getline(puzzle_input, bank_string)) {
        vector<int> bank;
        for (const char battery : bank_string) {
            bank.push_back(battery - '0');
        }
        
        int first_number_index = argmax(bank, 0, bank.size() - 1);
        int first_number = bank[first_number_index];

        int second_number_index = argmax(bank, first_number_index + 1, bank.size());
        int second_number = bank[second_number_index];

        cout << first_number << second_number << endl;

        total_joltage += 10 * first_number + second_number;
    }

    cout << total_joltage << endl;
}