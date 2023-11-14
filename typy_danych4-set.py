# set (zbiór)  - zbior nie prechowuje niepowtarzające sie elementy
# nie zachowuje kolejnosci przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} klamerka {}, nie zachował kolejności
print(type(zbior))  # <class 'set'>

zb2 = set()  # pusty set (zbiór)
print(zb2)  # set() - pusty zbiór

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# usunięcie pierwszego - zwraca usunięte
print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
print(zbior)  # {44, 18, 22, 55}
# usunięte elemnty:
# 33
# 66
# 777
# 11

# usunięcie po elemencie
zbior.remove(55)
print(zbior)  # {44, 18, 22}

zbior2 = {667, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {18, 52, 999, 11, 44, 667, 62}

print(zbior | zbior2)  # suma zbiorów {999, 11, 44, 18, 52, 22, 667, 62}
print(zbior & zbior2)  # częśc wspólna {18, 44}
print(zbior - zbior2)  # {22}
print(zbior2 - zbior)  # {999, 11, 52, 667, 62}
print(zbior2.difference(zbior))  # {999, 11, 52, 667, 62}
