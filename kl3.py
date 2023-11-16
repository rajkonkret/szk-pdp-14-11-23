class Car:
    """
    klasa samochod
    """

    def __init__(self, model, year, kolor):
        self.model = model
        self.year = year
        self.kolor = kolor
        self.__predkosc = 0  # __ - oznacza pole prywatne (dostępne tylko wewnątrz klasy)

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()  # uzycie metody prywatnej

    def __zmien_bieg(self):  # metoda prywatna
        print("Zmiana biegu")


car1 = Car("Mercedes", 2023, "srebrny")
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# po ustawieniu pola __predkosc na prywatne wystapi bład
# print(car1.__predkosc)  # 50 AttributeError: 'Car' object has no attribute '__predkosc'.
# Did you mean: '_Car__predkosc'?
car1.licznik()  # Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 20 km/h, Prędkość wynosi 20 km/h
car1.__predkosc = 0
# po oznaczeniu w klasie pola prywatnego Prędkość wynosi 20 km/h pomimo ustawiania w proframie pola:
# car1.__predkosc = 0
# poniewaz od teraz to są dwa rózne pola
# nadane w programie car1.__predkosc jest polem publicznym o tej nazwie
# zdefiniowane w konstruktorze self.__predkosc jest polem prywatnym
# różnią sie zasiegiem widocznosci
# publiczne widoczne dla wszystkich
# prywatne widoczne tylko w kalsie i to pole ustawia metoda gaz() lub hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h, Prędkość wynosi 20 km/h

car1.__predkosc = 100
car1.licznik()  # Prędkość wynosi 20 km/h
