from pathlib import Path

src_file = Path("myfile.txt")
src_file.touch()

dir_full = Path("examples", "data", "example_001")
dir_full.mkdir(parents=True, exist_ok=True)

dst_file_1 = "myfile_1.txt"
dst_file_2 = "myfile_2.txt"

src_file.copy(dir_full / dst_file_1)
src_file.copy(dir_full / dst_file_2)
src_file.copy_into(dir_full)

assert (dir_full / src_file).exists()
assert (dir_full / dst_file_1).exists()
assert (dir_full / dst_file_2).exists()

print("Файлы скопированы")
