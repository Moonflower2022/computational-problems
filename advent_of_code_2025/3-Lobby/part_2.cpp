#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int argmax(vector<int>& array, int i1, int i2) {
    vector<int>::iterator max_iterator = max_element(array.begin() + i1, array.begin() + i2);
    return distance(array.begin(), max_iterator);
}

int main() {
    ifstream puzzle_input("puzzle_input.txt");
    string bank_string;

    long long total_joltage = 0;

    while (getline(puzzle_input, bank_string)) {
        vector<int> bank;
        for (const char battery : bank_string) {
            bank.push_back(battery - '0');
        }

        vector<int> good_batteries;

        int good_battery_index = -1;
        int good_battery;

        for (int i = 0; i <= 11; i++) {
            good_battery_index = argmax(bank, good_battery_index + 1, bank.size() - (11 - i));
            good_battery = bank[good_battery_index];
            good_batteries.push_back(good_battery);
            cout << good_battery;
            total_joltage += good_battery * pow(10, 11 - i);
        }

        cout << endl;
    }

    cout << total_joltage << endl;
}