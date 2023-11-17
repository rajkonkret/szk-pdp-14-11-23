# typ json
# json => {"name":"Radek"}

import json

print_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
# None  - nic w innych jezykach null
print(print_dict)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(print_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(print_dict, f, indent=4, sort_keys=True)
# {"name": "Radek", "age": 40, "czy_pali": null}
# po dodaniu indent=4:
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# o dodaniu sort_keys=True
# mamy posortowane po kluczach
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data["name"])  # Radek

# zamiana słownika na json
json_text = json.dumps(data, indent=4, sort_keys=True)
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}
print(type(json_text))  # <class 'str'>

# zamiana jsona na słownik
dict_json = json.loads(json_text)
print(dict_json)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(dict_json))  # <class 'dict'>
