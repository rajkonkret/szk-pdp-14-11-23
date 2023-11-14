user = "Tomek"  # str
wiek = 30  # int
wersja = 3.900001  # float - zmiennoprzecinkowe
liczba = 134567890123  # int

print("Witaj %s masz teraz %d lat" % (user, wiek))  # Wiatj Tomek masz teraz 30 lat
# w przypadku korzystanie z formatowania z %, python sprawdza typ
# print("Witaj %s masz teraz %d lat" % (wiek, user))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit - liczba
print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, 'wiek': wiek})
print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, 'age': wiek})

print("Witaj {} masz teraz {} lat".format(user, wiek))
print("Witaj {} masz teraz {} lat".format(wiek, user))  # Witaj 30 masz teraz Tomek lat

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 30 lat.

print("uzywamy wersji Python %i" % 3)  # %i - integer
print("uzywamy wersji Python %f" % 3.9)  # %f - float uzywamy wersji Python 3.900000
print("uzywamy wersji Python %.1f" % 3.9)  # uzywamy wersji Python 3.9  #.1f - jedna liczba po przecinku
print("uzywamy wersji Python %.2f" % 3.9)  # uzywamy wersji Python 3.90
print("uzywamy wersji Python %.f" % 3.9)  # uzywamy wersji Python 4
print("uzywamy wersji Python %.0f" % 3.9)  # uzywamy wersji Python 4
# o0 miejsc po przecinku, zaokrągla, %.Xf - zaokrągla i wyswietla w X miejsc po przecinku

print(f"Uzywamy wersji Pythona {wersja}")
print(f"Uzywamy wersji Pythona {wersja:.1f}")
print(f"Uzywamy wersji Pythona {wersja:.2f}")
print(f"Uzywamy wersji Pythona {wersja:.0f}")
# Uzywamy wersji Pythona 3.900001
# Uzywamy wersji Pythona 3.9
# Uzywamy wersji Pythona 3.90
# Uzywamy wersji Pythona 4  - również zaokrąglone wyświetlanie

print(f"{user:>10}")  # "     Tomek"  - uzupełnił spacjami do długosci 10, wyrównał do prawej
print(f"{user:<20}")  # "Tomek               "  wyrównaj do lewej
print(f"{user:^20}")  # "       Tomek        "  wyśrodkuj
# 12:45
