from pathlib import Path
import shutil

shutil.rmtree("src", ignore_errors=True)

src_dir_full = Path("src", "data", "example_001")
src_dir_full.mkdir(parents=True, exist_ok=True)
file = src_dir_full / "myfile.txt"
file.touch()

dst_dir = Path("dst")
shutil.rmtree(dst_dir, ignore_errors=True)
dst_dir.mkdir(parents=True, exist_ok=True)

input("Директории созданы. Нажмите Enter для их переноса.")

src_data = Path("src", "data")

src_data.move(Path("dst", "data"))
# src_data.move_into("dst")
