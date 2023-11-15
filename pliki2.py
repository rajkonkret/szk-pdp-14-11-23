import chardet
# pip install chardet - polecenie w terminalu

file_path = 'test.log'

with open(file_path, 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)
# gdy próbka zbyt mała
# {'encoding': 'Windows-1254', 'confidence': 0.670697820753897, 'language': 'Turkish'}
# gdy wieksza próbka
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''} - odczyt
encoding = result['encoding']
print(encoding)  # utf-8

print(raw_data.decode(encoding=encoding))
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
# utf-8
# Radek
# dodane
# dodane
# dodane
# dośdane
# dośdaćźne
