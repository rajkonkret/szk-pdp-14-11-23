class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # print(5 / 0)
    # raise ZeroDivisionError("Nie dziel prze zero")
    raise MyException("Moj bład")
except ZeroDivisionError:
    print("Nie dzielimy przez zero")
# MyException: Moj bład
except MyException:
    print("Rzucono wyjątek MyException")  # Rzucono wyjątek MyException

x = 0
try:
    if x == 0:
        # print("X nie moze byc 0")
        raise MyException("X nie może być 0")
except MyException:
    print("Drogi użytkowniku x nie może byc 0")
