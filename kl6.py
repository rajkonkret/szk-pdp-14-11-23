class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", 'Kowalski', 4300)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f"""
Wynagrodzenie dla pracownika:
    {pracownik.imie} {pracownik.nazwisko}
wynosi: {wyn_prac}
""")
# Wynagrodzenie dla pracownika:
#     Jan Kowalski
# wynosi: 4300

menago = Manager("Anna", "Nowak", 10000, 5000)
menago.przedstaw_sie()
wyn_menago = menago.oblicz_pensje()
print(f"Wynagrodzenie managera {menago.imie} {menago.nazwisko}: {wyn_menago}")
# Nazywam się Anna Nowak
# Wynagrodzenie managera Anna Nowak: 15000
