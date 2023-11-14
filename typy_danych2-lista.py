# lista - kolekcja do przechowywania danych
# lista moze przechowywać różnego typu  elementy
# lista zapamietuje kolejnosc dodawania
lista = []  # dekalrujemy (tworzymy) pustą liste
print(type(lista))  # <class 'list'>

lista.append("Radek")  # append() - dodawanie elemntów do listy
lista.append("Maciek")
lista.append("Dominik")
lista.append("Sławek")
lista.append("Konrad")
lista.append("Aleksandra")
lista.append("Magdalena")
print(lista)  # ['Radek', 'Maciek', 'Dominik', 'Sławek', 'Konrad', 'Aleksandra', 'Magdalena']
print(lista[0])  # index 0 oznacza pierwszy element listy
print(lista[1])
print(len(lista))  # 7 elementów, ostatni indeks 6, len() - pobieranie długości kolekcji
# print(lista[10])  # IndexError: list index out of range
print(lista[-1])  # Magdalena indeks -1 oznacza osytani element czyli indeks 6

# ['Radek', 'Maciek', 'Dominik', 'Sławek', 'Konrad', 'Aleksandra', 'Magdalena']
#   0(-7)     1(-6)     2(-5)      3(-4)     4(-3)        5(-2)        6(-1)
print(lista[0:3])  # ['Radek', 'Maciek', 'Dominik'] z prawej zbior nirdomknięty
print(lista[-2:0])  # [] idzie tylko w prawo, nie znajdzie zera po prawej stronie idac od -2
# nazwa listy, nawias kwadratowy [], i w nawiasie numer indeksu

# nadpisanie elementu w liscie na danym indeksie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Sławek', 'Konrad', 'Aleksandra', 'Magdalena']

# wstawic element pomiedzy dwa inne
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Sławek', 'Konrad', 'Aleksandra', 'Magdalena']

# usuniecie elementu z listy (pierwszego napotkanego)
lista.remove("Maciek")
print(lista)

# sprawdzenie indeksu dla danego elementu
indeks = lista.index("Aleksandra")
print(indeks)  # 5

# usunięcie elemntu po indeksie
print(lista.pop(indeks))  # Aleksandra
print(lista)  # ['Radek', 'Marcin', 'Mikołaj', 'Sławek', 'Konrad', 'Magdalena']

a = 6
b = 7
a = b
print(a)
b = 8
print(a)

lista1 = lista  # kopia referencji (adresu pamięci)
lista_copy = lista.copy()  # kopiwanie elemntów listy do drugiej
print(lista)
print(lista1)
lista1.clear()  # usunięcie wszystkich elementów z listy
print(lista)  # []
print(id(lista))  # 2484832391168
print(id(lista1))  # 2484832391168
print(lista_copy)
print(id(lista_copy))  # 2484833908416

print("Radek" in lista_copy)  # True - oznacza, "Radek" znajduje sie w liscie lista_copy

liczby = [54, 999, 34, 22.14, 687]
# liczby = [54, 999, 34, 22.14, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
print(type(liczby))  # <class 'list'>
print(liczby)  # [54, 999, 34, 22.14, 687]
liczby.sort()
print(liczby)  # [22.14, 34, 54, 687, 999]

liczby.reverse()
print(liczby)  # [999, 687, 54, 34, 22.14]
liczby.sort(reverse=True)
print(liczby)  # [999, 687, 54, 34, 22.14]

lista_osob = ['radek', 'ola']
lista_osob.sort()
print(lista_osob)  # ['ola', 'radek']

liczby[3] = 666
print(liczby)  # [999, 687, 54, 666, 22.14]
print(liczby[-2])
print(liczby[0:3])
print(liczby[0:-2])  # [999, 687, 54]

indeks_li = liczby.index(666)
print(liczby.pop(indeks_li))  # 666

liczby.remove(54)
print(liczby)  # [999, 687, 22.14]
print(len(liczby))  # długosc kolekcji wynosi 3

krotka = tuple(liczby)  # zamiana listy na tuple(krotkę)
print(krotka)
print(type(krotka))  # <class 'tuple'>
