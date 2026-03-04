#include <iostream> 
#include <fstream>
#include <chrono>
#include <gmpxx.h>
#include <utility>

std::pair<mpz_class, mpz_class> fast_doubling(int n) {
    if (n == 0) {
        return {0, 1};
    }

    auto p = fast_doubling(n / 2);
    mpz_class a = p.first;
    mpz_class b = p.second;

    mpz_class c = a * (b * 2 - a);
    mpz_class d = a * a + b * b;

    if (n % 2 != 0) {
        return {d, c + d};
    } else {
        return {c, d};
    }
}
int main() {
    std::ofstream outfile("fib_fast_cpp.csv");
    outfile << std::fixed << std::setprecision(6);
    outfile << "steps,time_ms\n";

    for (int i = 1000; i <= 1000000; i += 1000) {
        auto start = std::chrono::high_resolution_clock::now();

        mpz_class result = fast_doubling(i).first;

        auto end = std::chrono::high_resolution_clock::now();
        double ms = std::chrono::duration<double, std::milli>(end - start).count();
        outfile << i << "," << ms << "\n";
    }
    outfile.close();
    return 0;
}