#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

using grid = vector<vector<bool>>;

int get_surrounding_count(grid& roll_grid, int x, int y)
{
    int height = roll_grid.size();
    int width = roll_grid[0].size();

    int surrounding_count = 0;

    for (int dx = -1; dx <= 1; dx++)
    {
        for (int dy = -1; dy <= 1; dy++)
        {
            if (!(dx == 0 && dy == 0) && (x + dx >= 0) && (x + dx < width) && (y + dy >= 0) && (y + dy < height) && (roll_grid[y + dy][x + dx] == true))
            {
                surrounding_count++;
            }
        }
    }
    return surrounding_count;
}

int main()
{
    fstream puzzle_input("puzzle_input.txt");
    string line;

    grid roll_grid;

    while (getline(puzzle_input, line))
    {
        vector<bool> row;

        for (const char element : line)
        {
            if (element == '@')
            {
                row.push_back(true);
            }
            else
            {
                row.push_back(false);
            }
        }
        roll_grid.push_back(row);
    }

    int accessible_roll_count = 0;

    for (int y = 0; y < roll_grid.size(); y++)
    {
        for (int x = 0; x < roll_grid[y].size(); x++)
        {
            if (roll_grid[y][x] == true && get_surrounding_count(roll_grid, x, y) < 4)
            {
                accessible_roll_count++;
            }
        }
    }

    cout << accessible_roll_count << endl;
}