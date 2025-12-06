#include <iostream>
#include <cmath>

using namespace std;

int main() {
    string test = "1111";

    for (const char battery : test) {
        cout << battery << endl;
        cout << battery - '0' << endl;

    }
    cout << pow(10, 3) << endl;
}