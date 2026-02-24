import math
import time

PI = math.acos(-1)

def loop_shape(total_steps, radius, offset):
    i = 0
    while i <= total_steps:
        theta = (i / total_steps) * 2.0 * PI + offset
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        i += 1

with open("python_results.csv", "w") as outfile:
    outfile.write("steps,time_ms\n")
    steps = 100
    while steps <= 1000000:
        start = time.perf_counter()
        loop_shape(steps, 10, 0.0)
        end = time.perf_counter()
        ms = (end - start) * 1000
        outfile.write(f"{steps},{ms:.6f}\n")
        steps += 1000