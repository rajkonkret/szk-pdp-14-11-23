# do tej klasy w nastepnym kroku dodalismy abstrakcję
class Ptak:
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

    def wydaj_odglos(self):
        print("kiiiir ki-er")


or1 = Ptak("Orzel", 45)
or1.latam()  # Tu Orzel Lecę z szybkością 45
or1.wydaj_odglos()
print(or1.latam())  # None
kur1 = Ptak("Kura", 0)
kur1.latam()  # Tu Kura Lecę z szybkością 0
kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura, ja nie latam.
kur2.dziobanie()
or2 = Orzel("Orzel", 50)
or2.latam()  # dziedziczcy po ptaku
or2.poluj()
kur2.wydaj_odglos()
or2.wydaj_odglos()