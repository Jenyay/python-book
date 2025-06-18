import pandas as pd

converters = {
    "Бюджет": (lambda price: 
              float(price.replace(",", ""))
              if price != "" else None),

    "Успех": lambda status: status.strip().lower() == "success"
}
data = pd.read_csv("space_missions.csv",
                   usecols=[0, 2, 4, 5, 7, 8],
                   header=0,
                   names=["Организация", "Дата", "Аппарат",
                          "Миссия", "Бюджет", "Успех"],
                   converters=converters,
                   parse_dates=["Дата"],
                   )
print(data.info())
print()
print(data)
