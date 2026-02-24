import pandas as pd
import matplotlib.pyplot as plt

cpp = pd.read_csv("results.csv")
python = pd.read_csv("python_results.csv")

fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
ax.set_facecolor("white")

ax.grid(True, color="#e0e0e0", linewidth=0.8)
ax.set_axisbelow(True)

ax.plot(cpp["steps"], cpp["time_ms"], label="C++", color="#388c46", linewidth=1.5)
ax.plot(python["steps"], python["time_ms"], label="Python", color="#2d2d2d", linewidth=1.5)

ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

ax.set_xlabel("Steps")
ax.set_ylabel("Time (ms)")
ax.set_title("C++ vs Python Performance")
ax.legend()

plt.tight_layout()
plt.savefig("benchmark.png", dpi=150)
plt.show()