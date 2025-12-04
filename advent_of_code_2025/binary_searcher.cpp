#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int low, high;
    cin >> low >> high;

    cout << "estimated # of steps: " << int(log2(high - low + 1)) + 1 << "\n";

    while (low <= high) {
        int mid = low + (high - low) / 2;
        cout << "Checking mid: " << mid << "\n";
        char direction;
        cin >> direction;
        if (direction == '<') {
            high = mid - 1;
        } else if (direction == '>') {
            low = mid + 1;
        } 
    }

    return 0;
}