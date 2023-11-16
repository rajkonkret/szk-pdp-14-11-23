# argumnty słownikowe (przekazane po nazwie)
def connect(**opcje):
    print(opcje)
    connect_param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    connect_param['pwd'] = opcje
    print(connect_param)  # {'host': '127.0.0.1', 'port': '8080', 'pwd': {'a': 7}}
    print(connect_param['pwd'])


def funk(*args, **kwargs):  # funkcja moze przyjac argumnty pozycyjne i nazwane
    print(args)
    print(kwargs)


connect()  # {} - słownik klucz=wartosc - argument nazwany
connect(a=7)  # {'a': 7}

funk()
funk(1, 2, 3, 4, 5, 6)
funk(1, 2, 3, 4, 5, 6, a=7, b=6, name="Radek")
# (1, 2, 3, 4, 5, 6)  - krotka => *args
# {'a': 7, 'b': 6, 'name': 'Radek'} słownik => *kwargs
dictionary = {'host': '127.0.0.1', 'port': '8080', 'pwd': {'a': 7}}
print(dictionary['pwd']['a'])  # 7
