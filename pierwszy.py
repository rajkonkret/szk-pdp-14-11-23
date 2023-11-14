print()  # wypisz/ wydrukuj
print("nazywam się Radek")  # nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
# ctrl - d - duplikuje linijki
print(type("Radek"))  # <class 'str'> - teksty
print(type('Radek'))  # <class 'str'>

print(39)
print(type(39))  # <class 'int'> liczba całkowita
# int ma pojemnosc 4300 znakow - uzależnioy od architektury

print("39" + "14")  # 3914 - konkatenacja tekstów - łaczenie tekstów
print(39 + 14)  # 53 - int
# ctrl alt l - formatowanie kodu (probuje dostosowac kod do PEP8)
print(5 * "4")  # 44444
print(int("39") + int("14"))  # 53 - int() - rzutowanie na liczbę cąlkowita (zamiana)

# zmienna  - pudełko na dane
imie = "Raddek"
print(type(imie))  # <class 'str'>
# type() - sprawdenie typu danych

wiek = 48
print(type(wiek))  # <class 'int'>
print(wiek)  # 48

wiek = "Raddek"
print(type(wiek))  # <class 'str'>
# print(wiek + 1)  # TypeError: can only concatenate str (not "int") to str
# ctrl / - zakomentowanie lini
print(wiek + str(1))  # Raddek1
