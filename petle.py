# for - petla iterujaca
# po kolei podstawia pod zadana zmienna wartosci z kolekcji*
import random
from itertools import zip_longest

for i in range(10):  # range(10) - wygenureje liczby od 0..9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # _  - niema zmienna
    pass
    # print(_)

for i in range(10):
    print(i * 2)

# przeniesc boiler code z zadania random i przerobic na pętle
# zbudowac liste liczb od 1 do 49
# losowac z listy choice
# zapisac wylosowana liczbe w zmiennej
# usunąc z listy
# wypisac
# i to wszystko opakowac pętlą for
lista = list(range(1, 50))
for i in range(6):
    wyn = random.choice(lista)
    lista.remove(wyn)
    print(wyn)

# hackerrank, codewise
# w3school
for i in range(10):  # 0..9
    if i % 2 == 0:
        print(i, "jest parzysta")

for i in range(1, 10):  # 1..9
    if i % 2 == 0:
        print(i, "jest parzysta")

# listy składane
lista3 = [j for j in range(10) if j % 2 == 0]
# to jest to samo
lista4 = []
for j in range(10):
    if j % 2 == 0:  # % - modulo - reszta z dzielenia
        lista4.append(j)

print(lista3)
print("lista4", lista4)
# [0, 2, 4, 6, 8]
# [0, 2, 4, 6, 8]
for i in range(0, 10, 2):  # start, stop, krok  0..9
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -2):  # pętla z ujemnym krokiem, idzie do tyłu
    print(i)
# 11:10

# lista4 [0, 2, 4, 6, 8]
for c in lista4:
    print(c)
    if c == 2:
        c += 1  # c = c + 1
    print(c)

a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a  - 1
print(a)  # 1
a *= 2  # a = a *2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0 - float
a %= 2  # a = a % 2
print(a)  # 1.0

imiona = ['Radek', 'Zenek', "Tomek"]
print(imiona)
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Zenek
# Tomek

# wyswietlic elementy z tej listy w postaci: 0 Radek
for p in imiona:
    print(imiona.index(p), p)  # 0 Radek

for i in range(len(imiona)):  # range(3) 0..2
    print(i, imiona[i])

# enumerate() - numeruje kolekcje i zwraca numer oraz element kolekcji
for p in enumerate(imiona):
    print(p)  # (2, 'Tomek')
# i, o = (2, 'Tomek') - rozpakownaie krotki
for i, o in enumerate(imiona):
    print(i, o)

# ludzie = ['Radek', 'Janek', 'Asia', 'Michał', "Tadek"]
# dla różnych długości list IndexError: list index out of range
ludzie = ['Radek', 'Janek', 'Asia', 'Michał', "Tadek", "Adam"]

wiek = [47, 67, 67, 45, 23]
# wypisac w postaci Radek 47
# dla różnych długości list IndexError: list index out of range
#
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])

# zip() - łaczenie kolekcji (połaczy w pary tylko te które maja pary), ominie pozostałe
for i in zip(ludzie, wiek):
    print(i)  # ('Tadek', 23) krotka
# rozpakowujemy krotke w petli
for l, w in zip(ludzie, wiek):
    print(l, w)

# wypisac w postaci 0 Radek 47
# uzyjemy enumerate()
for i in enumerate(zip(ludzie, wiek)):
    print(i)  # (4, ('Tadek', 23)) krotka w krotce
a, b = (4, ('Tadek', 23))
print(a, b)  # 4 ('Tadek', 23)
c, d = ('Tadek', 23)
print(c, d)  # Tadek 23
for i, (l, w) in enumerate(zip(ludzie, wiek)):
    # rozpakowanie wewnetrznej krotki umieszczzone w nawiasach (l,w)
    print(i, l, w)

zipped = zip_longest(ludzie, wiek, fillvalue='Nan')
# poniewaz zipped jest elementem typu iterator,
# musimy zapiusac go do np.: listy jesli chcemy wielokrotnie z niego korzystac
zipped_list = list(zipped)
print(zipped)  # <itertools.zip_longest object at 0x00000140A95B72E0>
for item in zipped:
    # wykorzystujemy iterator, po przejsciu ustawi wskaznik na nastepny po ostatnim(czyli pusty) element
    print(item)
# ('Radek', 47)
# ('Janek', 67)
# ('Asia', 67)
# ('Michał', 45)
# ('Tadek', 23)
# ('Adam', 'Nan')

# for i, w in zipped:
#     print(i, w)

print(zipped_list)  # [('Radek', 47), ('Janek', 67), ('Asia', 67), ('Michał', 45), ('Tadek', 23), ('Adam', 'Nan')]
