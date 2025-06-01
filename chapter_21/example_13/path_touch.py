from pathlib import Path

filename = "myfile.txt"
file_path = Path(filename)
file_path.touch()
assert file_path.exists()
