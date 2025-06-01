import os

sep = os.sep
root = "data"
for n in range(1, 43):
    for m in range(1, 452):
        filename = f"{root}{sep}{n:03g}{sep}data_{m:03g}.dat"
        # Что-то делаем с файлом...
