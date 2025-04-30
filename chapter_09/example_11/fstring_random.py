from random import seed, uniform

seed(2)
freq = [1e9 + 0.2e9 * n for n in range(6)]
val = [uniform(-1, 1) for _ in freq]

for f, v in zip(freq, val):
    print(f"{f:<15.3e}{v:< .3f}")
