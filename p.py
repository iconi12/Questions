import numpy as np
import matplotlib.pyplot as plt

def A(n): return 20 * n
def B(n): return 2 * n * np.log2(n)
def C(n): return n * n

for n in [10, 100, 1000, 10000]:
    print(n, A(n), round(B(n), 2), C(n))

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Full range, log-log scale
n = np.linspace(2, 10000, 5000)
for f, name in [(A, "A: 20n"), (B, "B: 2n log2 n"), (C, "C: n^2")]:
    ax[0].plot(n, f(n), label=name)
ax[0].set_xscale("log"); ax[0].set_yscale("log")
ax[0].set_title("Full range (log-log)"); ax[0].legend()

# Zoomed in to show the B-C crossings
ns = np.linspace(1.5, 6, 1000)
ax[1].plot(ns, B(ns), label="B"); ax[1].plot(ns, C(ns), label="C")
ax[1].set_title("B vs C, small n"); ax[1].legend()
plt.xlabel("n"); plt.show()

# Intersection points (sign change of B - C)
d = B(ns) - C(ns)
print("B-C crossings ≈", ns[np.where(np.diff(np.sign(d)) != 0)[0]])