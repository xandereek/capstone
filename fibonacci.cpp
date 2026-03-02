#include <iostream>
#include <gmpxx.h>
#include <fstream>
#include <chrono> 


void fib(int n) {
    mpz_class a = 0;
    mpz_class b = 1;
    mpz_class c;
    
    for (int i = 1; i < n; ++i) {
        c = a + b;
        a = b;
        b = c;
    }
}
int main() {
    std::ofstream outfile("fib_results.csv");
    outfile << std::fixed << std::setprecision(6);
    outfile << "steps,time_ms\n";

    for(int i = 1000; i < 1000000; i += 1000) {
        auto start = std::chrono::high_resolution_clock::now();

        fib(i);

        auto end = std::chrono::high_resolution_clock::now();
        double ms = std::chrono::duration<double, std::milli>(end - start).count();
        outfile << i << "," << ms << "\n";
    }
    return 0;
}