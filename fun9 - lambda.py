# lambda - uproszcona forma funkcje
# moze byc zdefiniowana w miejscu uzycia

odejmij = lambda a, b: a - b  # z załozenia ma return
print(odejmij(9, 8))


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


# spróbujcie przerobic na lambde
oblicz_vat2 = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat2(1000))
print(oblicz_vat2(1000, 23))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(8))
print(wiek(16))
print(wiek(30))


def zmien(x):
    return x * 2


for i in [1, 2, 3, 4, 5]:
    print(zmien(i))

for i in range(1, 6):
    print(i * 2)
lista = [1, 2, 3, 4, 20, 30, 55, 100]

# map() - bieze kazdy elemnt z kolekcji, wykonuje na nim działanie wg zadanej funkcji
print(f"Zastosowanie map() {list(map(zmien, lista))}")  # Zastosowanie map() [2, 4, 6, 8, 40, 60, 110, 200]
print(f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")  # Zastosowanie map() [2, 4, 6, 8, 40, 60, 110, 200]
# itertools
# filter() - filtrowanie danych wg funkcji
print(f"Zastosowanie filter() {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter() [1, 2]
print(f"Zastosowanie filter() {list(filter(lambda x: x > 20, lista))}")
# Zastosowanie filter() [30, 55, 100]
# wieksze od 3, mniejsze od 40
print(f"Zastosowanie filter() {list(filter(lambda x: 3 < x < 40, lista))}")
# Zastosowanie filter() [4, 20, 30]
# x > 3 and x < 40 -> 3 < x < 40
