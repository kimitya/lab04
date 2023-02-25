import datetime as d
a = d.datetime(2023, 2, 23, 10, 40, 40)
b = d.datetime(2022, 1, 22, 9, 30, 30)
c=(a-b).days * 24 * 3600 + (a-b).seconds
print(c)