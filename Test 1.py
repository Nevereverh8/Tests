a = list(map(int, input("введите элементы списка через пробел \n").split()))


def unique_val(a):
    u = []

    for i in a:
        if i in u:
            pass
        else:
            u.append(i)
    return sorted(u)


b = unique_val(a)
for i in b:
    print(i, end=' ')
