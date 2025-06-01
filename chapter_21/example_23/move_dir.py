import os
import shutil
from pathlib import Path

shutil.rmtree("src", ignore_errors=True)

src_dir_full = Path("src", "data", "example_001")
src_dir_full.mkdir(parents=True, exist_ok=True)
file = src_dir_full / "myfile.txt"
file.touch()

dst_dir = Path("dst")
shutil.rmtree(dst_dir, ignore_errors=True)
dst_dir.mkdir(parents=True, exist_ok=True)

input("Директории созданы. Нажмите Enter для их переноса.")

# os.rename(Path("src", "data"), Path("dst", "data"))
# os.replace(Path("src", "data"), Path("dst", "data"))
# shutil.move(Path("src", "data"), Path("dst", "data"))
# Path("src", "data").rename(Path("dst", "data"))
Path("src", "data").replace(Path("dst", "data"))
