def calculate(x, **kwargs):
    print(f"{kwargs=}")
    result = x
    result *= kwargs.get('mul', 1)
    result += kwargs.get('add', 0)
    return result

print(f'{calculate(5)=}\n\n')
print(f'{calculate(10, mul=2)=}\n\n')
print(f'{calculate(10, add=5)=}\n\n')
print(f'{calculate(10, add=5, mul=2)=}\n\n')
print(f'{calculate(x=10, mul=2, add=5)=}')
