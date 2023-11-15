import csv

with open('dane.csv', 'r') as file:
    reader = csv.reader(file)
    lista = list(reader)

print(lista)  # [['SN', ' Name', ' City'], ['1', ' Michael', ' New Jersey'], ['2', ' Jack', ' California']]
# zamienc w tej liscie Michel na wasze imie

print(lista[1])  # ['1', ' Michael', ' New Jersey']
print(lista[1][1])  # Michael indeks 1 , 1

# zmiana danych
lista[1][1] = "Radek"

with open('dane_2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lista)  # zapis listy
