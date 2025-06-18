import pandas as pd
import numpy as np

data = np.array([[1, 10, 100],
                 [2, 20, 200],
                 [3, 30, 300],
                 [4, 40, 400],
                 [5, 50, 500]])
columns = ["Foo", "Bar", "Baz"]
index = ["a", "b", "c", "d", "e"]
df = pd.DataFrame(data, index=index, columns=columns)
print(df)
