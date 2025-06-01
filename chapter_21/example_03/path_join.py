import os.path as op

root = "data"
for n in range(1, 43):
    for m in range(1, 452):
        filename = op.join(root, f"{n:03g}", f"data_{m:03g}.dat")
        # Что-то делаем с файлом...
