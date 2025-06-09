import numpy as np

foo = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
result = None
for item in foo.flat:
    if item % 2 != 0:
        if result is None:
            result = item
        else:
            result = max(result, item)

print(result)
