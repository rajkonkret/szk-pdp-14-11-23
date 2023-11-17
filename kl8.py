# wielodziedziczenie
class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(A, B):  # wielodziedziczenie
    """
   Klasa C,  dzieziczy po klasie A
   """

    def method(self):
        print("Metoda z klasy C")
        super().method()
        B.method(self)


class D(B, A):
    def method(self):
        super().method()


a = A()
a.method()  # Metoda z klasy A
b = B()
b.method()  # Metoda z klasy B
c = C()
c.method()
# dla C(A, B) -> Metoda z klasy A
# gdy nadpisze metode w klasie C - > Metoda z klasy C
#         super().method() -> Metoda z klasy A
#         B.method(self) -> Metoda z klasy B
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
d = D()
d.method()  # Metoda z klasy B
print(D.__mro__)  # class D(B, A):
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(type(D.__mro__))  # <class 'tuple'>
for i in D.__mro__:
    print(type(i))
