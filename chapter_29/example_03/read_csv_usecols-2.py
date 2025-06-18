import pandas as pd


data = pd.read_csv("space_missions.csv", usecols=[0, 2, 4, 5, 7, 8])
print(data.info())
print()
print(data)
