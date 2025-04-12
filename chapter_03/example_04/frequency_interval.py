freq_str = input("Введите частоту в ГГц: ")
freq = float(freq_str)

if freq < 1.0:
    print("Слишком низкая частота")
elif freq >= 1.0 and freq < 2.0:
    print("Это диапазон L")
elif freq >= 2.0 and freq < 4.0:
    print("Это диапазон S")
elif freq >= 4.0 and freq < 8.0:
    print("Это диапазон C")
elif freq >= 8.0 and freq < 12.0:
    print("Это диапазон X")
elif freq >= 12.0 and freq < 18.0:
    print("Это диапазон Ku")
elif freq >= 18.0 and freq < 26.5:
    print("Это диапазон K")
elif freq >= 26.5 and freq <= 40.0:
    print("Это диапазон Ka")
else:
    print("Слишком высокая частота")
