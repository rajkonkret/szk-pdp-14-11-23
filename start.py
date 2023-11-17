import pakiet
from pakiet import fun
import pakiet.fun as pk
import main

fun.powitanie()
pk.powitanie()
# po uzupełnieniu w pliku __init__.py
# __all__ = ['powitanie']
# mozemy uzyc import pakiet
# i korzystac z funkcji w tym pakiecie
pakiet.powitanie()

# info() nie ma w  pliku __init__
# ie mozemy go uzyc po bezpośrednim imporcie
# pakiet.info() - to nie zadziała
# zadziała
fun.info()
pk.info()
main.print_hi("Text")