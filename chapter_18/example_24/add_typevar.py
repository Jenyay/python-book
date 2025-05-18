from typing import TypeVar

T = TypeVar("T", float, str)

def add(a: T, b:T) -> T:
    return a + b

foo = add(10, 20.5)
bar = add("Привет, ", "typing")
spam = add("Привет, ", 42)
