dist = 0.1
time = 250e-12
speed = dist / time

assert speed > 0
assert speed <= 299792458, "Скорость не должна превышать скорость света"

print("Скорость равна:", speed, "м/с")
