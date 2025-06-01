from pathlib import Path
import shutil

src_file = "myfile.txt"
Path(src_file).touch()

dir_full = Path("examples", "data", "example_001")
dir_full.mkdir(parents=True, exist_ok=True)

dst_file_1 = "myfile_1.txt"
dst_file_2 = "myfile_2.txt"

shutil.copyfile(src_file, dir_full / dst_file_1)
shutil.copy(src_file, dir_full / dst_file_2)
shutil.copy(src_file, dir_full)

assert (dir_full / src_file).exists()
assert (dir_full / dst_file_1).exists()
assert (dir_full / dst_file_2).exists()

print("Файлы скопированы")
