#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int main()
{
    vector<int> offsets;
    ifstream puzzle_input("puzzle_input.txt");
    string line;

    while (getline(puzzle_input, line)) {
        cout << stoi(line.substr(1, line.length())) << endl;
        int offset = stoi(line.substr(1, line.length()));
        
        if (line[0] == 'L') {
            offset *= -1;
        } 
        offsets.push_back(offset);
    }

    int pointer = 50;
    int times_visited_zero = 0;

    for (int i = 0; i < offsets.size(); ++i) {
        pointer += offsets[i];
        while (pointer < 0) {
            pointer += 100;
        }
        while (pointer >= 100) {
            pointer -= 100;
        }
        if (pointer == 0) {
            times_visited_zero++;
        }
    }
    cout << "Times visited zero: " << times_visited_zero << endl;
    return 0;
}