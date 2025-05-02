# Функция без параметров. Возвращает None.
def hello_world():
    print("Hello, world!")

# Функция с одним параметром. Возвращает None.
def hello(name):
    print(f"Hello, {name}!")

# Функция с двумя параметрами.
def add(a, b):
    c = a + b
    return c

# Функция с двумя параметрами.
# Возвращает кортеж из двух значений.
def add_sub(a, b):
    s = a + b
    d = a - b
    return (s, d)

# Вызов созданных функций
hello_world()
hello("Guido")
foo = add(4, 2)
bar, baz = add_sub(4, 2)
