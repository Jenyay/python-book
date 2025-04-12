num = int(input("Введите целое число: "))
print("Простые множители для введенного числа:")
d = 2
while num > 1:
    if num % d == 0:
        print(d)
        num //= d
        continue
    d += 1
