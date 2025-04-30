from random import randint, seed

template = "%-8d %-8d %-8d"
seed(2)
for n in range(6):
    val1 = randint(-9999, 9999)
    val2 = randint(-9999, 9999)
    val3 = randint(-9999, 9999)
    print(template % (val1, val2, val3))
