import datetime
a = list(map(int, input().split(sep='.')))
b = list(map(int, input().split(sep='.')))
x = abs(datetime.date(a[2], a[1], a[0])-datetime.date(b[2], b[1], b[0]))
print(x.days)
