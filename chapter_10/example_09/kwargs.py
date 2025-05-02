def calculate(x, **kwargs):
    print(f"{kwargs=}")
    result = x
    if 'mul' in kwargs:
        result *= kwargs['mul']

    if 'add' in kwargs:
        result += kwargs['add']
    return result

print(f'{calculate(5)=}\n\n')
print(f'{calculate(10, mul=2)=}\n\n')
print(f'{calculate(10, add=5)=}\n\n')
print(f'{calculate(10, add=5, mul=2)=}\n\n')
print(f'{calculate(x=10, mul=2, add=5)=}')
