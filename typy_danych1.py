wiek = 47
rok = 2023
temp = 36.6  # float
wiek2 = 37.5  # float
# x = 36,6 - to nie jest liczba

print(wiek2)
print(type(wiek2))  # <class 'float'>

print(5 * "Radek")  # RadekRadekRadekRadekRadek

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023232822540781017 flot
print(wiek // rok)  # 0 częśc całkowita z dzielenia
print(wiek % rok)  # 47 - reszta z dzielenia czyli modulo
print(5 % 2)  # 1 bo mamy 2 całe i reszty 1, 2 * 2 + 1 = 5

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# przy typie float pojawiają sie blędy zaokrąglenia
wynik = 0.2 + 0.7
print(f"{wynik:.1f}")  # przy wypisywaniu zaokrąglił 0.9
print(wynik)  # 0.8999999999999999

print(f"Spradzenie zmiennej {temp} {wiek}")
print(f"""
{temp}
    {wiek}""")

# typ logiczny
# True, False - w zaleznosci czy wyrażenie jest prawdziwe, czy fałszywe
# w pythonie obowiązkowo z duzej litery
czy_znasz_python = False
print(czy_znasz_python)
print(type(czy_znasz_python))  # <class 'bool'>
print(int(czy_znasz_python))  # 0
print(int(True))  # 1

x = 1
print(bool(x))  # rutowanie int na bool - True
x = 100
print(bool(x))  # True
x = 0
print(bool(x))  # False

x = 'radek'
print(bool(x))  # True
x = ''
print(bool(x))  # False
x = None  # None - nic (w inych językach null)
print(bool(x))  # False

a = 14
b = 3
print(f"Wynik porównania {a} > {b} = {a > b}")
print(f"Wynik porównania {a} < {b} = {a < b}")
print(f"Wynik porównania {a} == {b} = {a == b}")  # == porównanie
print(f"Wynik porównania {a} != {b} = {a != b}")  # != czy różne
print(f"Wynik porównania {a} >= {b} = {a >= b}")
print(f"Wynik porównania {a} <= {b} = {a <= b}")
# Wynik porównania 14 > 3 = True
# Wynik porównania 14 < 3 = False
# Wynik porównania 14 == 3 = False
# Wynik porównania 14 != 3 = True
# Wynik porównania 14 >= 3 = True
# Wynik porównania 14 <= 3 = False
