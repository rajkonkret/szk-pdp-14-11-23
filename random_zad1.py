import random

# random - do generowania liczb pseudolosowych

print(random.randint(1, 6))  # int 1..6 włącznie
print(random.random())  # float 0.949164200843633  0..0.999999
print(random.random() * 6)  # 1.2168446818028915 0..5.999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista_kule = list(range(1, 50))  # 1..49
print(lista_kule)

wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # powtarzajace sie liczby [5, 14, 22, 3, 14, 35]
print(random.sample(lista_kule, 6))  # [5, 23, 36, 13, 6, 42]
