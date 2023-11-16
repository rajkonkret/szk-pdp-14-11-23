# klasy - szablon wskazujacy cechy i funkcje jakie ma posiadac stworzony obiekt
# klasa ma miejsce definicji - tu sie kod nie wykonuje
# klasa uruchamie sie w momencie tworzenia obiektu
# klasa to przepis na obiekt
class Human:
    """
    Klasa Human opisujaca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    # w funkcji w klasie obowiązkowo self
    def powitanie(self):  # self - obiekt ktory wywołuje(przychodzi) do metody w klasie
        print(f'Nazywam się {self.imie}')


    def wypisz_wiek(self):
        print(f"Mój wiek {self.wiek}.")


cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000002904D800DD0>
print(Human.__doc__)  # Klasa Human opisujaca człowieka w Pythonie
print(print.__doc__)
# Prints the values to a stream, or to sys.stdout by default.
#
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
cz1.imie = "Jaś"
cz1.wiek = 10
cz1.plec = "m"
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
# m
# 10
# Jaś

cz2 = Human()
cz2.imie = "Małgosia"
cz2.wiek = 20
print(cz2.plec)
print(cz2.wiek)
print(cz2.imie)
# k
# 20
# Małgosia
# uruchomienie metody na obiekcie
cz1.powitanie()  # self -> cz1
cz2.powitanie()  # self -> cz2
# Nazywam się Jaś
# Nazywam się Małgosia
# dopisac metode wypisz_wiek() do kalsy Human
cz1.wypisz_wiek()
cz2.wypisz_wiek()
# Mój wiek 10.
# Mój wiek 20.