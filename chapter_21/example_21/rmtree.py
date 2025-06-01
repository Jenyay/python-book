from pathlib import Path
import shutil

dir_full = Path("examples", "data", "example_001")
dir_full.mkdir(parents=True, exist_ok=True)
file = dir_full / "myfile.txt"
file.touch()

input("Директории созданы. Нажмите Enter для их удаления.")
examples_dir = Path("examples")
shutil.rmtree(examples_dir)

assert not examples_dir.exists()
print("Директории удалены.")
