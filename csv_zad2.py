import csv

filename = "records.csv"

fields = []
rows = []

with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    print(dialect.quotechar)
    csv_f.seek(0)  # ustawienie ponownie wskażnika na elemnt 0 w pliku
    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    # next() - odczytanie z iteratora elementu i przestawienie wskaźnika na nastepny
    fields = next(csvreader)  # odczyta pierwszy wiersz i przestawi wskaźnik na następny
    for row in csvreader:  # petla wystartuje od drugiego elementu
        rows.append(row)

print(fields)
print(rows)
