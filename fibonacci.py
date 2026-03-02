import time

def fib(n):
    a = 0
    b = 1
    for _ in range(1, n):
        c = a + b
        a = b
        b = c

with open("fib_results_python.csv", "w") as outfile:
    outfile.write("steps,time_ms\n")

    for i in range(1000, 1000000, 1000):
        start = time.perf_counter()

        fib(i)
        end = time.perf_counter()
        ms = (end - start) * 1000
        outfile.write(f"{i},{ms:.6f}\n") 
        outfile.flush()