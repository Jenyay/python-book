import pandas as pd


data = pd.read_csv("space_missions.csv",
                   header=0,
                   names=["Организация", "Дата", "Аппарат",
                          "Миссия", "Бюджет", "Успех"],
                   usecols=[0, 2, 4, 5, 7, 8],
                   )
print(data.info())
print()
print(data)
