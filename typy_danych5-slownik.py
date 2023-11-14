# słownik, typ danych para klucz, wartosc
# json - {"name":"Radek"}
# słownik = {'name' : 'Radek'} -> {"klucz" : 'wartosc'}
# klucze nie mogą sie powtarzać

dictionary = {}  # pusty słownik
print(type(dictionary))
print(dictionary)  # {} - pusty słownik

# dodawanie elemntu, jesli klucz nie istniej zostanie dodany do słownika
dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}
dictionary['imie'] = "Tomek"  # gdy klucz istnieje, nadpiszemy wartość dla tego klucza
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39}

# jakie są elemnty w słowniku?
# klucze, wartości, pary
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Tomek', 39])
# dict_items([('imie', 'Tomek'), ('wiek', 39)])

dictionary.update({'date': '12-12-2023'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39, 'date': '12-12-2023'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ("z", 3)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 3}

# aplikacja słownik
# stworzyc słownik z nazwami polskimi i angielkimi tłumaczeniami
# pokazac znane nam słówka (np.: wyswietlic klucze)
# pobrac słowko od usera input() - pobieranie danych (np.:  z kalwaitury)
# wyswietlić tłumaczenie

dict_pol_eng = {'imie': 'name', 'kot': 'cat', 'drzewo': 'tree'}
print(f"Mamy w słowniku: {dict_pol_eng.keys()}")
odp = input("Podaj słowo do przetłumaczenia")  # odpowiedz od użytkownika wrzucamy do zmiennej odp (str)
print(dict_pol_eng[odp.replace(" ", "").lower()])

a = input("Podaj pierwszą liczbę")
b = int(input("Podaj drugą liczbę"))
print(float(a) + b)  # 11.0
