def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)  # a, b 1 2
allparams(1, 2, 3)  # c, d 3 256
allparams(1, 2, c=7)  # c, d 7 256
# / - argumenty po lewej stronie musza byc podane po pozycji
allparams(1, 2, 3, 1, 2, 3, 4, 5, 6)  # args (1, 2, 3, 4, 5, 6)
# jesli chcemy cos wpisac do args to c musimy przekazac po pozycji
allparams(1, 2, 3, 1, 2, 3, 4, 5, 6)  # args (1, 2, 3, 4, 5, 6)
allparams(1, 2, 3, 1, 2, 3, 4, 5, 6, d=100)  # c, d 3 100
allparams(1, 2, 3, 1, 2, 3, 4, 5, 6, d=100, name="Radek")  # kwargs {'name': 'Radek'}
allparams(1, 2, 3, 1, 2, 3, 4, 5, 6, d=100, name="Radek", a=9)  # kwargs {'name': 'Radek', 'a': 9}


def all_p(a, b, /, c=5, **kwargs):
    print(a, b, c, kwargs)


all_p(1, 2, 3)  # 1 2 3 {}
all_p(1, 2, a=8)  # 1 2 5 {'a': 8} z / w argumentach dodaje do słownika
# all_p(a=8, b=5)  # 8 5 5 {} bez / w argumentach podstawia pod a
