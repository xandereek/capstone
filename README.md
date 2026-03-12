# High School Capstone

This is my Senior Capstone, aiming to measure the performance differences between C++ and Python across various algorithms. Specifically, it tests trigonometric functions through circle calculation, the naive Fibonacci sequence, and fast Fibonacci (fast doubling).


## Key findings

In all cases, C++ outperformed Python by a substantial margin. For algorithms like naive Fibonacci, C++ is the only viable solution as you scale. However, in other cases like fast Fibonacci, Python offers compelling speeds and may be the better choice, depending on whether the difference of a few milliseconds actually matters for your project.

### Results
---

![benchmark_circle.png](benchmark_circle.png)
*In this case, the algorithm is linear, resulting in a small performance difference at the start. As the numbers scale up, both languages remain relatively quick for non-performance-critical applications.*

---

![benchmark_fib.png](benchmark_fib.png)
*Since naive Fibonacci scales exponentially, C++ becomes the only viable option if you must use this specific algorithm, unless performance doesn't matter at all.*

---

![benchmark_fib_fast.png](benchmark_fib_fast.png)
*Fast Fibonacci is orders of magnitude quicker than the naive algorithm, making Python perfectly viable in situations where a few milliseconds don't count.*

## How to run

### C++

>[!IMPORTANT]
>This project was developed and tested entirely on macOS. Depending on your compiler and environment, the C++ code may require modifications to compile successfully on Windows

First, compile the circle C++ using the following command:
```bash
clang++ -o circle circle.cpp
```

Then for the Fibonacci files, use the following command instead:
```bash
clang++ fast_fibonacci-o fast_fibonacci.cpp -lgmp -lgmpxx
```
### Python
Python is easy and will run crossplatform just run (changing the file name as needed):
```bash
python3 circle.py
```
