# match case - od python 3.10
lista = []

lang = input("Podaj znany Ci język programowania")  # zwraca str

match lang:
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case '1' | '2' | '3':
        print("Co innego")
    case _:  # wartośc domyślna (taki else)
        print("Nie znam takiego języka")

print(lista)
# ['java']
