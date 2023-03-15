import datetime


def days_distance(d1,d2):
    x = abs(datetime.date(d1[2], d1[1], d1[0])-datetime.date(d2[2], d2[1], d2[0]))
    return x.days


a = list(map(int, input("Введите первую дату через точку в формате ДД.ММ.ГГ\n").split(sep='.')))
b = list(map(int, input("Введите вторую дату через точку в формате ДД.ММ.ГГ\n").split(sep='.')))


print('Разница между двумя датами в днях =', days_distance(a, b))
