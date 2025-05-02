def append_count(lst=[]):
    lst.append(len(lst))
    return lst

foo = append_count()
print(f"1) {foo=}")

bar = append_count()

print(f"2) {foo=}")
print(f"{bar=}")
print(f"{foo is bar=}")
