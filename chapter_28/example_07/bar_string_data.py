import matplotlib.pyplot as plt

dates = ["Янв.", "Фев.", "Март", "Апр.", "Май", "Июнь", 
         "Июль", "Авг.", "Сент.", "Окт.", "Нояб.", "Дек."]
visitors = [10_748, 12_610, 15_245, 14_468, 14_897, 10_441,
            8_904, 9_301, 11_272, 14_083, 12_788, 11_748]

plt.bar(dates, visitors)
plt.grid()
plt.tight_layout()
plt.show()
