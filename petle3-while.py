# petla while
# sterowana warunkiem
# dopóki warunek jest True to petal się wykonuje

licznik = 0
while True:  # petla nieskończona
    licznik += 1
    print("Komunikat")
    if licznik > 10:
        break  # przerywa bieżącą pętle

print(licznik)  # 11
licznik = 0
while licznik < 10:
    print("Komunikat2")
    licznik += 1

# password = input("podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło. Podaj ponownie")
# print("Hasło prawidłowe")

lista = []
lista2 = []

while True:  # petla while True jako głowna pętla programu
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)  # tu doda typy jako str
    lista2.append(int(wej))  # tu zmaineiamy na int przed dodaniem do listy

print(lista)
print(lista2)
# ['4', '2', '8', '4']
# [4, 2, 8, 4]
