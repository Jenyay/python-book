from pathlib import Path
import os
import shutil

for n in range(1, 7):
    Path(f"myfile_{n}.txt").touch()

input("Файлы созданы. Нажмите Enter для их переименования.")

os.rename("myfile_1.txt", "new_myfile_1.txt")
os.replace("myfile_2.txt", "new_myfile_2.txt")
shutil.move("myfile_3.txt", "new_myfile_3.txt")
Path("myfile_4.txt").rename("new_myfile_4.txt")
Path("myfile_5.txt").replace("new_myfile_5.txt")
# Path("myfile_6.txt").move("new_myfile_6.txt")

print("Файлы переименованы.")
