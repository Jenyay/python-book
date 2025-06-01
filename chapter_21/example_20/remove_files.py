import os
from pathlib import Path

file_1 = Path("myfile_1.txt")
file_1.touch()

file_2 = Path("myfile_2.txt")
file_2.touch()

input("Файлы созданы. Нажмите Enter, чтобы их удалить.")

os.remove(file_1)
file_2.unlink()

assert not file_1.exists()
assert not file_2.exists()

print("Файлы удалены.")
