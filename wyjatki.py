# wyjątki
# print(5 / 0)
#   File "C:\Users\CSComarch\PycharmProjects\szk-pdp-14-11-23\wyjatki.py", line 2, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
# try - except
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Nie dzielimy przez zero")
except Exception as e:
    print("Bład", e)

print("Program nadal działa")
# Nie dzielimy przez zero
# Program nadal działa
