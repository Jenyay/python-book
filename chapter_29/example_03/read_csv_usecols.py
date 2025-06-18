import pandas as pd


data = pd.read_csv("space_missions.csv",
                   usecols=["Company", "Date", "Rocket",
                            "Mission", "Price", "MissionStatus"]
                   )
print(data.info())
print()
print(data)
