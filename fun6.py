# funkcja obliczająca średnia (np.: ocen)
# *oceny - dowolna ilosc argumentów pozycyjnych 1,2,3,4....
def liczby(name=None, *oceny):
    if type(name) is str:
        print(f"{name}")

    if isinstance(name, str):
        print(f"{name}")
    print(oceny)
    suma = 0
    count = len(oceny)
    try:
        for o in oceny:
            suma += o  # suma = suma + o
        print(f"{name} Średnia wynosi {suma / count}")
    except Exception as e:
        print("Bład", e)


liczby()  # ()
liczby(1, 2, 3)  # (1, 2, 3) krotka
liczby(1, 2, 3, 4, 5, 6)
liczby(1, 2, 3, 4, 5, 6, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4)
liczby("a", 2, 3)
# tak zmienic funkcje, by jako pierwszy argument było przesyłane imie
# i srednia wyswietlc wraz z podaniem imienia
liczby("Radek", 1, 2, 3, 4, 5, 6)
# Radek Średnia wynosi 3.5
# 11:15
