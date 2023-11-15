# pliki
# open()
# context manager -> with
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
with open('test.log', 'w', encoding='utf-8') as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# w - nadpisanie pliku
with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Radek\n")

# a - dopisanie danych do pliku
with open('test.log', 'a', encoding='utf-8') as f:
    f.write('dodane\n')
    f.write('dodane\n')
    f.write('dodane\n')
    f.write('dośdane\n')

with open('test.log', 'r', encoding='utf-8') as file:
    lines = file.read()

print(lines)

# Gdy chcemy uzyc "x" ale plik istnieje dostaniemy:
# FileExistsError: [Errno 17] File exists: 'test.log'
with open('test.log', 'x') as f:
    f.write("X")
