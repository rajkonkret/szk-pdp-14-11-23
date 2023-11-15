from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-11-15
time = datetime.now()
print(time)  # 2023-11-15 14:03:00.778068

print(type(time))  # <class 'datetime.datetime'>
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2023-11-16

print(type(tomorrow))  # <class 'datetime.date'>

print(time.time())
print(today.day)
# 14:21:01.992952
# 15

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)  # 15/11/2023

formated_time = datetime.now().strftime('%H:%M')
print(formated_time)  # 14:25
print(formated_time.removeprefix("0"))  # 14:26

formated_date_12h = datetime.now().strftime("%I:%M %p")
print(formated_date_12h)

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 80.0},
    {'sku': 3, 'exp_date': today, 'price': 70.0},
]
print(products)
for p in products:
    print(p)
    print(p['exp_date'])
    #     if p['exp_date'] == today:
    #         # cena = cena * 0.8 = cena *= 0.8
    #         p['price'] *= 0.8
    #         print(f"""
    # Price for sku = {p['sku']}
    # is now {p['price']}
    # """)
    if p['exp_date'] != today:
        continue
        # konczy biezaca iteracje petli i wraca na poczatek petli(bierze kolejny elemnt)
    p['price'] *= 0.8
    print(f"""
    Price for sku = {p['sku']}
    is now {p['price']}
    """)
[{'sku': 1, 'exp_date': datetime.date(2023, 11, 15), 'price': 100.0},
 {'sku': 2, 'exp_date': datetime.date(2023, 11, 16), 'price': 80.0},
 {'sku': 3, 'exp_date': datetime.date(2023, 11, 15), 'price': 70.0}]
{'sku': 1, 'exp_date': datetime.date(2023, 11, 15), 'price': 100.0}
# 2023 - 11 - 15
#
# Price
# for sku = 1
# is now
# 80.0
#
# {'sku': 2, 'exp_date': datetime.date(2023, 11, 16), 'price': 80.0}
# 2023 - 11 - 16
# {'sku': 3, 'exp_date': datetime.date(2023, 11, 15), 'price': 70.0}
# 2023 - 11 - 15
#
# Price
# for sku = 3
# is now
# 56.0