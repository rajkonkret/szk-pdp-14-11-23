# funkcje
# wydzielony fragment kodu, ktory mozna wykonac w dowolnym czasie
# deklaracja funkcji - miejsce gdzie funkcja jest napisana ale nie wykonywana
# wywołanie funkcji - miejsce uruchomienia funkcji
a = 4
b = 8


def dodaj():  # deklaracja funkcji, musi byc zdekalrowany zanim zostanie uzyta.
    # funkcja bezargumentowa
    print(a + b)  # przyjęła argumenty z wyzszego zakresu (scopa)


def dodaj2(a, b):  # funkcja z argumentami a i b
    print(a + b)  # zdekalrowane lokalnie zmienne a i b


def odejmij(a, b, c=0):  # funkcja z argumentem domyślnym c
    print(a - b - c)


# nazwe i  nawiasy()
dodaj()  # 12 - wywołanie funkcji uruchamia ja
# podanie argumentów po pozycji (argumenty pozycyjne)
dodaj2(6, 7)  # 13 - musimy podac argumenty, nie maja wartości domyslnych
odejmij(9, 5)  # dwa argumenty, c przyjęte domyślne czyli 0
odejmij(6, 7, 8)  # trzy argumenty, c=8
odejmij(b=8, c=9, a=5)
odejmij(b=6, c=7, a=8)  # podanie argumentów po nazwie
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

print(dodaj())  # None
# print(dodaj() + dodaj2(7, 8))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

