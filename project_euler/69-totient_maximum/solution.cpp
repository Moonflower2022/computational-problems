#include <iostream>
#include <stdio.h>
#include <chrono>
#include <numeric>
#include <algorithm>

using namespace std;
using namespace std::chrono;

int phi(int n)
{
    // Initialize result as n
    int result = n; 
 
    // Consider all prime factors of n 
    // and subtract their multiples 
    // from result
    for(int i = 2; i * i <= n; i++)
    {
        
        // Check if p is a prime factor.
        if (n % i == 0) 
        {
            
            // If yes, then update n and result
            while (n % i == 0)
                n /= i;
                
            result -= result / i;
        }
    }
 
    // If n has a prime factor greater than sqrt(n)
    // (There can be at-most one such prime factor)
    if (n > 1)
        result -= result / n;
        
    return result;
}

int main()
{
    auto start = high_resolution_clock::now(); // Record the start time
    
    float biggest = 0.;
    int index = 0;
    for (int i = 10; i <= 1000000; i++)
    {
        if ((float)i / phi(i) > biggest)
        {
            biggest = (float)i / phi(i);
            index = i;
        }
    }
    
    auto end = high_resolution_clock::now(); // Record the end time
    auto duration = duration_cast<milliseconds>(end - start);

    cout << "Running Time (ms): " << duration.count() << endl;
    cout << "Biggest: " << biggest << endl;
    cout << "Index: " << index << endl;
}