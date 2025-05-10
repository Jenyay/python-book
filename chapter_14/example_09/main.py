class Foo:
    ...

class Bar(Foo):
    ...

class Baz:
    ...

class Spam(Bar, Baz):
    ...


spam = Spam()

print(type(spam))
print(spam.__class__)

print(type(spam)==Spam)

print(isinstance(spam, Spam))
print(isinstance(spam, Foo))
print(isinstance(spam, Baz))

print(issubclass(Spam, Foo))
print(issubclass(Spam, Bar))
print(issubclass(Spam, Baz))

print(issubclass(Spam, Spam))
print(issubclass(Bar, Baz))

print(isinstance(spam, object))
print(issubclass(Foo, object))
