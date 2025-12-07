#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <set>

using namespace std;

using range_component = pair<long long, bool>;

void remove_nullified(vector<range_component> &range_components, set<int> &nullified_indices)
{
    vector<int> sorted_nullified_indices(nullified_indices.begin(), nullified_indices.end());
    sort(sorted_nullified_indices.begin(), sorted_nullified_indices.end());

    for (int i = 0; i < sorted_nullified_indices.size(); i++)
    {
        range_components.erase(range_components.begin() + (sorted_nullified_indices[i] - i));
    }
    nullified_indices.clear();
}

int main()
{
    fstream puzzle_input("puzzle_input.txt");
    string line;

    // bool represents whether it is a start component or not
    vector<pair<long long, bool>> range_components;

    while (getline(puzzle_input, line))
    {
        if (line == "")
        {
            break;
        }
        int dash_index = line.find("-");
        if (dash_index != string::npos)
        {
            long long starting_number = stoll(line.substr(0, dash_index));
            range_components.push_back({starting_number, true});

            long long ending_number = stoll(line.substr(dash_index + 1));
            range_components.push_back({ending_number, false});
        }
    }

    sort(range_components.begin(), range_components.end(), [](const range_component &pair1, const range_component &pair2)
         { if (pair1.first != pair2.first) {
        return pair1.first < pair2.first;
    }
    return pair1.second > pair2.second; });

    int running_count = 0;
    set<int> nullified_indicies;

    for (int i = 0; i < range_components.size(); i++)
    {
        if (range_components[i].second == true)
        {
            running_count++;
            if (running_count > 1)
            {
                nullified_indicies.insert(i);
            }
        }
        else
        {
            if (running_count > 1)
            {
                nullified_indicies.insert(i);
            }
            running_count--;
        }
    }

    remove_nullified(range_components, nullified_indicies);

    long long total_fresh_count = 0;
    long long range_start = -1;
    running_count = 0;

    for (int i = 0; i < range_components.size(); i++)
    {
        if (range_components[i].second == true)
        {
            running_count++;
            if (running_count == 1)
            {
                range_start = range_components[i].first;
            }
        }
        else
        {
            running_count--;
            if (running_count == 0)
            {
                total_fresh_count += range_components[i].first - range_start + 1;
            }
        }
    }

    cout << total_fresh_count << endl;
}