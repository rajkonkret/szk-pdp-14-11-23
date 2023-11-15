import pandas

# pip install pandas
# pandas - biblioek do przetwarzania danych

data = pandas.read_csv('records.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  radek    coe   3.0   0.0
# 1  radek    coe   3.0   0.0
# 2  marek    cos   4.0   0.9
# 3  tomek    coz   6.0  10.0
# 4  zenek    cop   4.0  11.0
# 5   jhon    cot   NaN   8.9

print(data.values)
print(data.columns)
# [['radek' 'coe' 3.0 0.0]
#  ['radek' 'coe' 3.0 0.0]
#  ['marek' 'cos' 4.0 0.9]
#  ['tomek' 'coz' 6.0 10.0]
#  ['zenek' 'cop' 4.0 11.0]
#  ['jhon' 'cot' nan 8.9]]
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(type(data))  # <class 'pandas.core.frame.DataFrame'>
print(type(data.values))  # <class 'numpy.ndarray'>
print(data.values[0])  # ['radek' 'coe' 3.0 0.0]
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  radek    coe   3.0   0.0
# 1  radek    coe   3.0   0.0
# 2  marek    cos   4.0   0.9
# 3  tomek    coz   6.0  10.0
# 4  zenek    cop   4.0  11.0
# 5   jhon    cot   NaN   8.9>
