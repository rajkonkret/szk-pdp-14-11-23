# klasa wykorzystujaca inicjalizator (konsktruktor)

class Human:
    """
    klasa opsujaca człowiek a w pythonie
    """

    def __init__(self, imie, wiek, plec='k'):  # inicjalizator, konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):  # self - obiekt ktory wywołuje(przychodzi) do metody w klasie
        print(f'Nazywam się {self.imie}')

    def wypisz_wiek(self):
        print(f"Mój wiek {self.wiek}.")

    # wypisz_plec
    def wypisz_plec(self):
        print(f"Płeć {self.plec}.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Ania", 34)
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
# k
# 34
# Ania
cz1.powitanie()  # Nazywam się Ania
cz1.wypisz_plec()
cz1.ruszaj()  # Ruszyłam w drogę

cz2 = Human("Radek", 78, "m")
cz2.ruszaj()  # Ruszyłem w drogę
