import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.style.use('default')
cpp = pd.read_csv("fib_fast_cpp.csv")
python = pd.read_csv("fib_fast_py.csv")
cpp["time_ms"] = cpp["time_ms"].rolling(window=5, min_periods=1).median()
python["time_ms"] = python["time_ms"].rolling(window=5, min_periods=1).median()
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#333333')
ax.spines['bottom'].set_color('#333333')
ax.grid(True, color="#CCCCCC", linestyle="--", linewidth=1, alpha=0.7)
ax.set_axisbelow(True)
ax.plot(cpp["steps"], cpp["time_ms"], label="C++", color="#FF4444", linewidth=2.5)
ax.plot(python["steps"], python["time_ms"], label="Python", color="#4488FF", linewidth=2.5)
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
ax.set_xlabel("Steps", fontsize=12, fontweight='medium', color="#333333")
ax.set_ylabel("Time (ms)", fontsize=12, fontweight='medium', color="#333333")
ax.set_title("C++ vs Python Performance", fontsize=16, fontweight='bold', color="black", pad=15)
legend = ax.legend(loc="upper left", frameon=True, fontsize=11)
legend.get_frame().set_facecolor('white')
legend.get_frame().set_edgecolor('#CCCCCC')
ax.text(0.98, 0.02, "Hardware: Apple M2",
    transform=ax.transAxes,
    fontsize=10,
    color="#888888",
    style="italic",
    ha="right", va="bottom",
    bbox=dict(facecolor="white", alpha=0.9, edgecolor="none"))
plt.tight_layout()
plt.savefig("benchmark_fib_fast_bw.png", dpi=300, facecolor='white', edgecolor='none')
plt.show()