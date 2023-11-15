dictionary = {'imie': 'Radek', 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# zwraca klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# zwraca wartości
for v in dictionary.values():
    print(v)

for i in dictionary.items():
    print(i)  # ('nazwisko', 'Kowalski')
# petla z rozpakowaniem krotki
for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => Kowalski

print("dana1", "dana2", sep=";", end="")  # dana1;dana2
"""
   Prints the values to a stream, or to sys.stdout by default.

     sep
       string inserted between values, default a space.
     end
       string appended after the last value, default a newline.
     file
       a file-like object (stream); defaults to the current sys.stdout.
     flush
       whether to forcibly flush the stream.
   """
print()
dictionary2 = {'name': 'imie', "company": "Orange"}
print(dictionary2)  # {'name': 'imie', 'company': 'Orange'}
# zamiana kluczy z wartosciami
print({value: key for key, value in dictionary2.items()})  # {'imie': 'name', 'Orange': 'company'}

d2 = {}
for k, v in dictionary2.items():
    d2[v] = k  # dodajemy do słownika klucz v o wartosci k

print(d2)  # {'imie': 'name', 'Orange': 'company'}
