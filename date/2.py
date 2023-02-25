import datetime as d

a = d.datetime.today()
yesterday = a - d.timedelta(1)
today = d.datetime.today()
tomorrow = a + d.timedelta(1)

print(yesterday)
print(today)
print(tomorrow)
