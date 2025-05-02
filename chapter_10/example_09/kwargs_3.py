def calculate(x, **kwargs):
    print(f"{kwargs=}")
    return x * kwargs.get('mul', 1) + kwargs.get('add', 0)

print(f'{calculate(5)=}\n\n')
print(f'{calculate(10, mul=2)=}\n\n')
print(f'{calculate(10, add=5)=}\n\n')
print(f'{calculate(10, add=5, mul=2)=}\n\n')
print(f'{calculate(x=10, mul=2, add=5)=}')
