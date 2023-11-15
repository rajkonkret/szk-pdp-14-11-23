# pliki csv - plik w których dane są oddzielone znakiem podziału (,;tab: itd)
# Zenek, Marek, Tomek

import csv

# csv - biblioteka do pracy z plikami csv
fileds = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']

filename = 'records.csv'
dict2 = dict(zip(fileds, row))  # zip() - łączy dwie listy, dict() - tworzy z tego słownik
print(dict2)  # {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'}

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'},
    {'name': 'marek', 'branch': 'cos', 'year': '4', 'cgpa': '0.9'},
    {'name': 'tomek', 'branch': 'coz', 'year': '6', 'cgpa': '10'},
    {'name': 'zenek', 'branch': 'cop', 'year': '4', 'cgpa': '11.0'},
    {'name': 'jhon', 'branch': 'cot', 'year': None, 'cgpa': '8.90'},
]
with open(filename, 'w', newline="") as csv_f:  # newline="" eliminacja pustej lini w pliku
    # csvwriter = csv.writer(csv_f)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fileds, delimiter=";")  # delimiter - standardtowo mamy (,)
    # csvwriter.writerow(row)
    csvwriter.writeheader()
    csvwriter.writerow(dict2)
    csvwriter.writerows(dict_list)
