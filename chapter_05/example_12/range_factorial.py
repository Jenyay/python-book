n = 8
factorial = 1
for i in range(n + 1):
    if i < 2:
        continue
    factorial *= i
print("Факториал равен", factorial)
