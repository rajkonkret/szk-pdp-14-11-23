# instrukcje warunkowe - instrukcje sterowania przepływem programu
# if - podstawowa instrukcja warunkowa
# # if warunek:
#     operacje gdy warunek spełniony

# wcięcia w pythonie miały  zastąpic np.: sredniki na koncu lini w innych jezykach
odp = True
odp2 = not odp  # negacja
print(odp2)

if odp:
    print("Brawo")  # wcięcie obowiązkowe (standartowo 4 spacje) - wykonuje sie gdy warunek True
else:  # w przeciwnym przypadku (działanie domyślne)
    print("Musisz się uczyc dalej")

print("Program idzie dalej")
#
# podatek = 0
# zarobki = int(input("Podaj dochód"))  # zamieniam na int()
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:  # 10000 .. 29999
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Zapłacisz {zarobki * podatek} zł")
# dodac dla przedziału 10000 - 29999 podatek 0.2

sum_zam = 50
if sum_zam > 100:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabat wynosi {rabacik}")
rabat = 25 if sum_zam > 100 else 0  # to co po lewj gdy prawda, to co po prawej gdy fałsz
# gdy warunek spełniony (True) do zmiennej rabat trafi 25,
# gdy warunek niespełniony do zmiennej rabat trafi 0
print(f"Rabat wynosi {rabat}")

# zasymulejemy system, który będzie dostawał informacje z róznych źródeł (console, email)
# w zależnosci z jakiego systemu i jaki bład przyjdzie podejmiemy rózne działanie
alert_system = 'email'
error = 'medium'

error_message = "Stało się coś strasznego"

lista_bledow = []
if alert_system == 'console':
    print(error_message)
elif alert_system == "email":
    print("Alert z sytemu email")
    if error == 'medium':
        lista_bledow.append("ostrzezenie")
    # dla błedu critical -> krytyczny, dla pozostałych -> inny
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append('inny')
else:
    print("Nie znam takiego systemu")
print(lista_bledow)
# Alert z sytemu email
# ['ostrzezenie']

# napisac test z....
# wyswietlic pytanie -> print
# pobrac odpowiedz -> input (mozna tez wyswietlic tu pytanie)
# sprawdzic odpowiedz -> if else
# wyswietlic wynik -> print

odp = input("Podaj datę Chrztu Polski")  # str
if odp == '966':
    print("Brawo")
else:
    print("Masz w książce na stronie 23")

# if elif else
