import pickle

lista = [1, 2, 3, 4, 5]

with open('test_lista.txt', 'w') as f:
    f.write(str(lista))

with open('test_lista.txt', 'r') as f:
    dane = f.read()

print(dane)  # [1, 2, 3, 4, 5]
print(type(dane))  # <class 'str'>
print(dane[0])  # [
lista2 = list(dane)
print(lista2)

with open('test_pickle.log', 'wb') as f:  # wb - zapis bajtowy, wymagania pickle
    pickle.dump(lista, f)

with open('test_pickle.log', 'rb') as file:
    loaded_list = pickle.load(file)

print(loaded_list)
print(type(loaded_list))  # <class 'list'>
print(loaded_list[0])  # 1
