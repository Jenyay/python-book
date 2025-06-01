import os.path as op

file_basename = op.basename(__file__)
cwd_dir = op.dirname(__file__)

print(f"{op.exists(__file__)=}")
print(f"{op.isfile(__file__)=}")
print(f"{op.isdir(__file__)=}")

print()
print(f"{op.exists(file_basename)=}")
print(f"{op.isfile(file_basename)=}")
print(f"{op.isdir(file_basename)=}")

print()
print(f"{op.exists(cwd_dir)=}")
print(f"{op.isfile(cwd_dir)=}")
print(f"{op.isdir(cwd_dir)=}")

print()
print(f"{op.exists('.')=}")
print(f"{op.isfile('.')=}")
print(f"{op.isdir('.')=}")

print()
print(f"{op.exists('..')=}")
print(f"{op.isfile('..')=}")
print(f"{op.isdir('..')=}")

print()
print(f"{op.exists('invalid.txt')=}")
print(f"{op.isfile('invalid.txt')=}")
print(f"{op.isdir('invalid.txt')=}")
