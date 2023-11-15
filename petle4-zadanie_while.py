# napisanie kalkulatora z wykorzystaniem petli while True jako gownej pętli programu,
# obsłuzenie wyjątkó za pomovą konstrukcji try - except
# menu z dostepnymi operacjami
# pobranie operacji do wykonania
# pobranie liczb
# wyswietlenie wyniku
# jaka opcja do wyjscia z programu
# obsługujemy wszelkie mozliwe błedy try - except
while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj działanie do wykonania")  # str
    if odp == '5':
        break
    try:
        a = int(input("Podaj pierwsza liczbe"))
        b = int(input("Podaj druga liczbe"))

        if odp == "1":  # Wynik dodawnia 5 + 4 = 9
            print(f"Wynik działania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik działania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik działania {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik działania {a} / {b} = {a / b}")
        else:
            print("nie nam takiego działąnia")
    except (TypeError, IndexError):
        print("Bład typu")
    # except ValueError:
    #     print("Bład wartości")
    except ZeroDivisionError:
        print("Nie dzielimy przez zero")
    except Exception as e:
        print('Błąd', e)
    else:  # wykona się tylko, gdy bład nie występuje
        print("Obliczenia wykonane poprawnie")
    finally:  # wykona sie zawsze, niezależnie czy wystąpił bład czy nie
        print("Ten fragment wykona się zawsze")
# Błąd invalid literal for int() with base 10: 'a'
# rozbudowa o pozostałe działania.
# ValueError, TypeError
# try - except - [else] - [finally]
# 13:45
# praca domowa - zmienic na match case
