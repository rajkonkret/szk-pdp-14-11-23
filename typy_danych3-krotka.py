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
