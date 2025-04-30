from random import seed, uniform

width = 15
prec = 3

seed(2)
freq = [1e9 + 0.2e9 * n for n in range(6)]
val = [uniform(-1, 1) for _ in freq]

for f, v in zip(freq, val):
    print(f"{f:<{width}.{prec}e}{v:< .{prec}f}")
