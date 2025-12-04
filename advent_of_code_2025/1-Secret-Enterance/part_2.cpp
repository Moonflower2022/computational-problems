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
        for (int j = 0; j < abs(offsets[i]); ++j) {
            if (offsets[i] > 0) {
                pointer++;
            } else {
                pointer--;
            }

            if (pointer % 100 == 0) {
                times_visited_zero++;
            }
        }
    }
    cout << "Times visited zero: " << times_visited_zero << endl;
    return 0;
}