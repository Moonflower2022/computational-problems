#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    fstream puzzle_input("puzzle_input.txt");
    string line;

    vector<pair<long long, long long>> fresh_ranges;

    int fresh_count = 0;

    while (getline(puzzle_input, line)) {
        if (line == "") {
            continue;
        }
        int dash_index = line.find("-");
        if (dash_index != string::npos) {
            long long starting_number = stoll(line.substr(0, dash_index));
            long long ending_number = stoll(line.substr(dash_index + 1));

            fresh_ranges.push_back({starting_number, ending_number});
        } else {
            long long ingredient_id = stoll(line);
            for (const pair<long long, long long> range : fresh_ranges) {
                if (ingredient_id >= range.first && ingredient_id <= range.second) {
                    fresh_count++;
                    break;
                }
            }
        }
    }

    cout << fresh_count << endl;
}