#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    fstream puzzle_input("puzzle_input.txt");

    vector<vector<long long>> lines;
    string line_string;

    while (getline(puzzle_input, line_string)) {
        vector<long long> line;
        stringstream ss(line_string);
        string element_string;
        while (getline(ss, element_string, ' ')) {
            if (element_string == "") {
                continue;
            }

            if (element_string == "*") {
                line.push_back(-1);
            } else if (element_string == "+") {
                line.push_back(-2);
            } else {
                line.push_back(stoi(element_string));
            }
        }
        lines.push_back(line);
    }

    long long total = 0;

    for (long long i = 0; i < lines[0].size(); i++) {
        cout << lines[0][i] << " " << lines[1][i] << " " << lines[2][i] << " " << lines[3][i] << " " << lines[4][i] << endl;
        if (lines[4][i] == -1) {
            total += lines[0][i] * lines[1][i] * lines[2][i] * lines[3][i];
        } else {
            total += lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i];
        }
    }

    cout << total << endl;

    return 0;
}