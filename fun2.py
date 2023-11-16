# funkcje zwracające wynik

def dodaj(a, b):
    return a + b  # return - zwróćenie wyniku do miejsca wywołania funkcji


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))  # 11
wyn = dodaj(8, 9)
print(wyn)
print(dodaj(4, 3) + dodaj(3, 4))

print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
print(oblicz_vat(vat=5, cena=1000))
# 1230.0
# 1070.0
# 1050.0
zm = oblicz_vat(1000)
print(zm)  # 1230.0 - float

if zm == 1230:
    print("Prawidłowo")
# Prawidłowo

zm = 1230.5
if zm == 1230:
    print("Prawidłowo")
else:
    print("Błąd")
# Błąd
