# instrukcje warunkowe - instrukcje sterowania przepływem programu
# if - podstawowa instrukcja warunkowa
# # if warunek:
#     operacje gdy warunek spełniony

# wcięcia w pythonie miały  zastąpic np.: sredniki na koncu lini w innych jezykach
odp = True
if odp:
    print("Brawo")  # wcięcie obowiązkowe (standartowo 4 spacje) - wykonuje sie gdy warunek True
else:  # w przeciwnym przypadku (działanie domyślne)
    print("Musisz się uczyc dalej")

print("Program idzie dalej")

podatek = 0
zarobki = int(input("Podaj dochód"))  # zamieniam na int()
if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30000:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.6

print(f"Zapłacisz {zarobki * podatek} zł")
# dodac dla przedziału 10000 - 29999 podatek 0.2
