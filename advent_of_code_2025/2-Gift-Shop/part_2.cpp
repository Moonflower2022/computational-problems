#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>

using namespace std;

long long get_number_length(long long number) {
    long long length = 0;
    while (number) {
        number /= 10;
        length++;
    }
    return length;
}

long long get_repetition_divisor(long long id_length, long long length) {
    long long repetition_count = id_length / length;

    long long divisor = 0;
    long long power = 1;
    for (long long i = 0; i < repetition_count; i++) {
        divisor += power;
        for (long long j = 0; j < length; j++) {
            power *= 10;
        }
    }
    return divisor;
}

bool is_fake(long long id) {
    long long number_length = get_number_length(id);

    for (long long length = 1; length <= number_length / 2; length++) {
        if (
            number_length % length == 0 &&
            number_length / length >= 2 &&
            id % get_repetition_divisor(number_length, length) == 0
        ) {
            cout << "  found fake:" << id << endl;
            return true;
        }        
    }
    return false;
}

int main() {

    ifstream puzzle_input("puzzle_input.txt");

    string line;
    getline(puzzle_input, line);

    stringstream ss(line);

    vector<pair<long long, long long>> id_ranges;

    string pair_str;
    while (getline(ss, pair_str, ',')) {
        long long dash_location = pair_str.find('-');
        long long start = stoll(pair_str.substr(0, dash_location));
        long long end = stoll(pair_str.substr(dash_location + 1));
        id_ranges.push_back({start, end});
    }

    long long fake_sum = 0;
    for (const auto& range : id_ranges) {
        for (long long id = range.first; id <= range.second; id++) {
            if (is_fake(id)) {
                fake_sum += id;
            }
        }
    }
    cout << fake_sum << endl;

    return 0;
}