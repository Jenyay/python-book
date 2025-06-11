import numpy as np

data = np.loadtxt('example_26_07.csv',
                  delimiter=',', quotechar='"',
                  converters=lambda x: float(x.replace(",", ".")))
print(data)
