# for - petla iterujaca
# po kolei podstawia pod zadana zmienna wartosci z kolekcji*
import random

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
