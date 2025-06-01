from pathlib import Path

dir_full = Path("examples", "data", "example_001")
dir_full.mkdir(parents=True, exist_ok=True)
assert dir_full.is_dir()
