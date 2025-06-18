import pandas as pd

data = pd.read_csv("space_missions.csv")
print(data)
print(f"{type(data)=}")
