# Działanie	Instrukcja SQL	HTTP	DDS
# Create	INSERT	PUT / POST	write
# Read (Retrieve)	SELECT	GET	read / take
# Update	UPDATE	POST / PUT / PATCH	write
# Delete (Destroy)	DELETE	DELETE	dispose

import requests

# pip install request
url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

response = requests.get(url)
print(response)
# <Response [200]> ok
# 3xx - błedy przekierowania
# 4xx = błedy po stronie klienta
# 5xx - błedy po stronie serwera (np. problem w bazie danych)

table = response.json()
print(table)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '223/A/NBP/2023', 'effectiveDate': '2023-11-17', 'mid': 4.0327}]}
# wypisac wszystkie klucze z tego słownika
# wypisac wartosci dla tych kluczy
# wypisac wartosc dla klucza mid
print(table.keys())  # dict_keys(['table', 'currency', 'code', 'rates'])
print(table['table'])
for k, v in table.items():
    print(k, "=>", v)
# table => A
# currency => dolar amerykański
# code => USD
# rates => [{'no': '223/A/NBP/2023', 'effectiveDate': '2023-11-17', 'mid': 4.0327}]
print(table['rates'][0]['mid'])  # 4.0327

url_gold = 'http://api.nbp.pl/api/cenyzlota'
response_gold = requests.get(url_gold)
data_gold = response_gold.json()
print(data_gold)  # [{'data': '2023-11-17', 'cena': 257.28}]
url_joke = "https://api.chucknorris.io/jokes/random"
response_joke = requests.get(url_joke)
data_joke = response_joke.json()
print(data_joke)  # [{'data': '2023-11-17', 'cena': 257.28}]
{'categories': [], 'created_at': '2020-01-05 13:42:24.40636',
 'icon_url': 'https://assets.chucknorris.host/img/avatar/chuck-norris.png', 'id': '5IduT_oHQqOshO_6rm53MQ',
 'updated_at': '2020-01-05 13:42:24.40636', 'url': 'https://api.chucknorris.io/jokes/5IduT_oHQqOshO_6rm53MQ',
 'value': "In 1983, the Department of Transportation required that Chuck Norris wear a Catalytic "
          "convertor over his ass to prevent ozone depletion. It was later determined by the Environmental Protection Agency that it wasn't enough to prevent global warming."}
