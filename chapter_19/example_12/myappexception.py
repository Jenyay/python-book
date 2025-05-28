class MyAppException(Exception): ...

class FooException(MyAppException): ...

class BarException(MyAppException): ...

if __name__ == "__main__":
    exceptions = [FooException("Это FooException."),
                  BarException("Это BarException.")]

    for exception in exceptions:
        try:
            raise exception
        except MyAppException as err:
            print("Поймано MyAppException.", err)
        except FooException as err:
            print("Поймано FooException.", err)
