#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <random>
using namespace std;

int simulate_slow(int k) {
    vector<int> numbers;
    for (int i = 1; i <= 3 * k + 1; i++) {
        numbers.push_back(i);
    }
    auto rng = default_random_engine {random_device{}()};
    shuffle(begin(numbers), end(numbers), rng);

    int total = 0;
    for (int i = 0; i < 3 * k + 1; i++) {
        total += numbers.at(i);
        if (total % 3 == 0) {
            return 0;
        }
    }
    return 1;
}

int simulate(int k) {
    vector<int> counts = {k + 1, k, k}; // 1, -1, 0
    return 0;
}

int main() {
    int k = 2;
    int iterations = 100000;

    int total = 0;

    for (int i = 0; i < iterations; i++) {
        total += simulate_slow(k);
    }

    cout << "ratio: " << (float) total / iterations << endl;
    cout << "total: " << total << endl;
    return 0;
}