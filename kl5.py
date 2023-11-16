# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # dziedziczenie po klasie Pojazd
    def __init__(self, kolor, marka):  # nadpisujemy konstruktor (obowiazkowo super())
        super().__init__(kolor)  # super() - element z klasy wyzszej tu: konstruktor
        self.marka = marka

    def info(self):  # nadpisujemy metode z klasy wyzszej (wykorzystanie super() opcjonalne)
        super().info()  # super() - element z klasy wyższej tu: metoda info()
        print(f"Marka: {self.marka}")


poj = Pojazd("czerwony")
poj.info()  # Kolor: czerwony
# Kolor: czerwony
car = Samochod("srebrny", "Toyota")
car.info()  # Kolor: srebrny
# Kolor: srebrny
# Marka: Toyota
