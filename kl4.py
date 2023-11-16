class Dom:
    """
    klasa opisująca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        # uzupełnic konstruktor
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien
        # 14:45
        # napisac funkcje typu wypisz_...

    def wypisz_metraz(self):
        print(f"Mamy {self.__metraz} m2")

    def wypisz_kolor(self):
        print(f"Mamy {self.__kolor} kolor")

    def wypisz_okna(self):
        print(f"Mamy {self.__liczba_okien} okien/okna")

    # funkcje zmien...
    def zmien_kolor(self):
        odp = input("Podaj nowy kolor")  # str
        self.__kolor = odp
        self.wypisz_kolor()

    def zmien_metraz(self):
        odp = int(input("podaj nowy metraż"))
        self.__metraz = odp
        self.wypisz_metraz()

    def zmien_okna(self):
        odp = int(input("podaj ile okien"))
        self.__liczba_okien = odp
        self.wypisz_okna()

    # funkcja dom_info() - wypisze kolor, metraz, okna
    def dom_info(self):
        print(f"Metraż: {self.__metraz}, Kolor: {self.__kolor}, Liczba okien: {self.__liczba_okien}")

    def __repr__(self):  # metoda magiczna. Można nadpisac celem ładnego wyswietlania obiektu
        return f"Metraż: {self.__metraz}, Kolor: {self.__kolor}, Liczba okien: {self.__liczba_okien}"


dom1 = Dom(200, "biały", 10)
print(dom1)  # Metraż: 200, Kolor: biały, Liczba okien: 10 - wypisanie z funkcji __repr__
dom1.wypisz_okna()  # Mamy 10 okien/okna
dom1.zmien_kolor()
dom1.zmien_metraz()
dom1.zmien_okna()
dom1.dom_info()  # Metraż: 300, Kolor: czerwony, Liczba okien: 19
