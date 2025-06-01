from pathlib import Path
import shutil

dir_src = Path("src")

# Создаем директорию src/data_001/
dir_src_data = dir_src / "data_001"
dir_src_data.mkdir(parents=True, exist_ok=True)

# Создаем файл src/data_001/myfile.txt
file_name = "myfile.txt"
src_file = dir_src_data / file_name
src_file.touch()

# Создаем директорию dst/
dir_dst = Path("dst")
dir_dst.mkdir(parents=True, exist_ok=True)

# Копируем директорию src/data_001/ в директорию dst
dir_dst_data = dir_dst / "data_001"
shutil.copytree(dir_src_data, dir_dst_data, dirs_exist_ok=True)

assert dir_dst_data.exists()
assert (dir_dst_data / file_name).exists()

print("Файлы скопированы")
