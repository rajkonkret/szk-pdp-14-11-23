# 10:15
# funkcja kantor
# kantor() - głowna funkcja
# usd(), eur() - funkcje wewnętrzne
def kantor(waluta):
    print("Uruchomienie kantoru", waluta)

    def usd(kwota):
        print(f"Wymieniam  {kwota} usd = {kwota * 4.2}")

    def eur(kwota):
        print(f"Wymieniam  {kwota} eur = {kwota * 4.7}")

    if waluta.lower().replace(" ", "") == 'usd':
        return usd
    else:
        return eur


kantor_usd = kantor("usd")
kantor_usd(1000)  # Wymieniam  1000 usd = 4200.0

kantor_eur = kantor('eur')
kantor_eur(5000)  # Wymieniam  5000 eur = 23500.0
