class MyException(Exception):
    ...

def raise_error():
    raise MyException("Это MyException.")

if __name__ == "__main__":
    try:
        raise_error()
    except MyException as err:
        print("Что-то пошло не так.", err)
