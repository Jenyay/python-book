import pandas as pd

data = {"Foo": [1, 2, 3, 4, 5],
        "Bar": [10, 20, 30, 40, 50],
        "Baz": [100, 200, 300, 400, 500]}
index = ["a", "b", "c", "d", "e"]
df = pd.DataFrame(data, index=index)
print(df)
