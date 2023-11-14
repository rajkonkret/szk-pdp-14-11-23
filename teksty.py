# 11:00
tekst = "Witaj świecie"
print(tekst)  # Witaj świecie
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie
""" Return a copy of the string converted to uppercase. """
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie
# teksty są niemutowalne

# to samo z zamiana na małe litery (lower())
tekst_lower = tekst.lower()
print(tekst_lower)  # witaj świecie
print(tekst)

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # 1, w zakresie od indeksu zero do indeksu 4 (ale 4 ni ebierze pod uwage)
# Radek
# 01234
# 0, 4 => Rade
print(tekst.count("j", 0, 4))  # Witaj => 0 bo j na pozycji 5(indeks 4) a z prawej strony zbiór niedomknięty,
# czyli 4 nie bierzemy

imie = "Radek"
print(imie)
print("imie:", imie)
starszy = "Witaj %s!"
print(starszy % imie)  # Witaj Radek! pod %s podstawił wartośc zmiennej imie
tekst_format = f"\tMama na imię {imie}\n i lubię pythona.\b"  # f - f-string - string sformatowany
# \t tabulator
# \n nowa linia
# \b backspace
print(tekst_format)  # Mama na imię Radek i lubię pythona.
print("Witaj {}!".format(imie))  # Witaj Radek!
print("""
    Tekst
        wielolinijkowy\b
        """)
print("tekst", end="")
print("tekst2")  # teksttekst2
# end = znak konca lini, domyslnie \n
