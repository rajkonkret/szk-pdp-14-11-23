from abc import ABC, abstractmethod


class Ptak(ABC):  # Dziedziczymy po ABC aby uzyskać własciwosci klasy abstrakcyjnej
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        """
        Metoda latam
        Wypisuje lot ptaka
        :return: None
        """
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # dekorator, metoda abstrakcyjna
    def wydaj_odglos(self):
        pass  # nic nie rob


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print(f"Tu {self.gatunek}, ja nie latam.")

    def dziobanie(self):
        print(f"Tu {self.gatunek}, idę sobie podziobać")

    def wydaj_odglos(self):
        print("Ko kko ko ko ")


class Orzel(Ptak):
    def poluj(self):
        print("Tu", self.gatunek, 'Rozpoczynam polowanie')

    # musimy obowiązkowo w klasach dziedziczących nadpisa tą metode
    # jeśli nie nadpiszemy dostajemy bład:
    # TypeError: Can't instantiate abstract class Orzel with abstract method wydaj_odglos
    def wydaj_odglos(self):
        print("kiiiir ki-er")


# po oznaczeniu klasy jako abstrakcyjna, nie mozna utworzyc z niej obiektów
# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos
# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością 45
# or1.wydaj_odglos()
# print(or1.latam())  # None
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura, ja nie latam.
kur2.dziobanie()
or2 = Orzel("Orzel", 50)
or2.latam()  # dziedziczcy po ptaku
or2.poluj()
kur2.wydaj_odglos()
or2.wydaj_odglos()
