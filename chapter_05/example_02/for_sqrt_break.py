from math import sqrt

items = [25, 100, 4, 0, -9, 36]
result = []
for x in items:
    if x < 0:
        print("Ошибка! В списке есть отрицательные числа.")
        break
    else:
        result.append(sqrt(x))
else:
    print("result:", result)
