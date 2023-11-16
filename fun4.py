# funkcja zagnieżdzona
def fun1():
    print("To jest fun1")

    def fun2():
        print("to jest fun2")

    return fun2  # bez nawiasów, zwrcamy referencje(adres funkcji), nie uruchamiamy


fun1()
print(fun1())  # <function fun1.<locals>.fun2 at 0x000001B75EECCD60>
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x00000216FF3FCD60>
print(type(xFun))  # <class 'function'>
xFun()  # to jest fun2
