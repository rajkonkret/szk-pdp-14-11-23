def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()  # zwracamy wynik działąnia funkcji która dekorujemy(przekzaną do nas)

    return wew  # zwracany tylko adres funkcji


@dekor
def hej():
    print('Hej')


hej()
# bez dekoratora -> Hej
# po dodaniu dekoratora @dekor wynik:
# Dekorujemy - z funkcji dekor
# Hej -  z funkcji hej
# 12:35
