#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath> 
#include <chrono>

const double PI = std::acos(-1);
void loop_shape(int total_steps, int radius, double offset) {

    int i = 0;
    while (i <= total_steps){

        
        double theta = (i / (double)total_steps) * 2.0 * PI + offset;

        double x = radius * std::cos(theta);
        double y = radius * std::sin(theta);

    i += 1;
    }
}

int main(){
    std::ofstream outfile("results.csv");
    outfile << std::fixed << std::setprecision(6);
    outfile << "steps,time_ms\n";

    for (int steps = 100; steps <= 1000000; steps += 1000) {
        auto start = std::chrono::high_resolution_clock::now();
        loop_shape(steps, 10, 0.0);
        auto end = std::chrono::high_resolution_clock::now();

        double ms = std::chrono::duration<double, std::milli>(end - start).count();
        outfile << steps << "," << ms << "\n";
    }
    return 0;
}