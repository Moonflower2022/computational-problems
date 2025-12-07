#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    fstream puzzle_input("puzzle_input.txt");
    string line;

    vector<bool> spoiled_lookup;

    int fresh_count = 0;

    while (getline(puzzle_input, line)) {
        if (line == "") {
            break;
        }
        int dash_index = line.find("-");
        if (dash_index != string::npos) {
            cout << line.substr(0, dash_index) << endl;
            long long starting_number = stoll(line.substr(0, dash_index));
            long long ending_number = stoll(line.substr(dash_index + 1));
            for (long long i = starting_number; i <= ending_number; i++) {
                spoiled_lookup[i] = 1;
            }
        } else {
            if (spoiled_lookup[stoll(line)] == 1) {
                fresh_count++;
            }
        }
    }

    cout << fresh_count << endl;
}