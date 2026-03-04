import time

def fast_doubling(n):
    if n == 0:
        return (0, 1)
    
    a, b = fast_doubling(n // 2)
    
    c = a * (b * 2 - a)
    d = a * a + b * b
    
    if n % 2 != 0:
        return (d, c + d)
    else:
        return (c, d)

with open("fib_fast_py.csv", "w") as outfile:
    outfile.write("steps,time_ms\n")

    for i in range(1000, 1000001, 1000):
        start = time.perf_counter()

        result = fast_doubling(i)[0]
        
        end = time.perf_counter()
        ms = (end - start) * 1000
        
        outfile.write(f"{i},{ms:.6f}\n") 
    outfile.flush()