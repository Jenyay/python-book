def append_count(lst=[]):
    lst.append(len(lst))
    return lst

foo = append_count()
bar = append_count()
spam = append_count([10, 20, 30])

print(f"{foo=}")
print(f"{bar=}")
print(f"{spam=}")
