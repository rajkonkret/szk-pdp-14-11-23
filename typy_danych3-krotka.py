# krotka - niemutowalna (po utworzeniu nie można zmienić zawartości krotki)
# jest wydajniejsza jesli chodzi o działanie
# moze byc jednoelementowa
tupla = ("Radek")  # <class 'str'> nawiasy nie zmieniły typu na tuple(nadal str)
tupla = "Radek",  # tupla jednoelementowa , po dodaniu (,) mamy typ tuple, nie musi byc nawiasu
print(type(tupla))  # <class 'tuple'>
print(len(tupla))  # 1
x = 36, 6
print(type(x))  # <class 'tuple'>
tupla2 = "Tomek", "Asia", "Zbyszek", "Marcin"
print(type(tupla2))  # <class 'tuple'><class 'tuple'>
tupla3 = (43, 55, 22.34, 11, 200)
print(type(tupla3))  # <class 'tuple'>

print(tupla2.index("Tomek"))  # indeks 0 bo pierwszy element
print(tupla2.count("Asia"))  # indeks 1
# 14:30

# rozpakowanie krotki
a, b = 1, 2  # po prawej stronie mamy krotkę
print(a)
print(b)

tp = 1, 2, 3
print(type(tp))  # <class 'tuple'>

# a, b = tp  # ValueError: too many values to unpack (expected 2) - za mało zmiennych
a, *b = tp  # * - worek na pozostałe dane (moze byc tylko jedna gwiazdka *)
print(a, b)  # 1 [2, 3]
print(tupla2)  # ('Tomek', 'Asia', 'Zbyszek', 'Marcin')
imie1, imie2, imie3, imie4 = tupla2
imie1, *imie2, imie3 = tupla2
print(imie1)  # Tomek
print(imie2)  # ['Asia', 'Zbyszek']
print(imie3)  # Marcin

tupla4 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a, *b, c = tupla4
print(a)
print(b)
print(c)
# 1
# [2, 3, 4, 5, 6, 7, 8]
# 9

lista = list(tupla2)
print(lista)  # ['Tomek', 'Asia', 'Zbyszek', 'Marcin']
print(type(lista))  # <class 'list'>
