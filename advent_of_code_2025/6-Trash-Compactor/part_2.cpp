#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{
    fstream puzzle_input("puzzle_input.txt");

    vector<pair<bool, int>> operations;
    string line_string;

    vector<string> character_map;

    while (getline(puzzle_input, line_string))
    {
        bool is_numbers_line = false;

        for (const char element : line_string) {
            if (isdigit(element)) is_numbers_line = true;
        }

        if (is_numbers_line)
        {
            character_map.push_back(line_string);
        }
        else
        {
            for (int i = 0; i < line_string.size(); i++)
            {
                if (line_string[i] == '*')
                {
                    operations.push_back({true, i});
                }
                else if (line_string[i] == '+')
                {
                    operations.push_back({false, i});
                }
            }
        }
    }

    int length = line_string.size();
    int height = character_map.size();

    long long total = 0;

    for (int operation_i = 0; operation_i < operations.size(); operation_i++)
    {
        bool is_end = operation_i == operations.size() - 1;
        int start_i = operations[operation_i].second;
        int end_i = is_end ? length : operations[operation_i + 1].second;

        // NOTE: end is not inclusive!

        long long count = operations[operation_i].first ? 1 : 0;

        for (int i = start_i; i < end_i; i++)
        {
            if (!is_end && i == end_i - 1) {
                continue;
            }

            long long number = 0;

            string number_string = "";

            for (int j = 0; j < height; j++)
            {
                if (isdigit(character_map[j][i]))
                {
                    number_string += character_map[j][i];
                }
            }

            number = stoll(number_string);

            if (operations[operation_i].first)
            {
                if (number != 0) {
                    count *= number;
                }
            }
            else
            {
                count += number;
            }
        }

        total += count;
    }

    cout << total << endl;

    return 0;
}