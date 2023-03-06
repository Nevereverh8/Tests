def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s


def combination(n, k):
    if k <= n:
        r = 1
        for i in range(k+1, n+1):
            r = r * i
        return r/fact(n-k)


def dice(n, m, s):
    p = (7-s)/6
    return combination(n, m) * (p**m) * ((1-p)**(n-m))


n, m, s = map(int, input("введите числа N, M, S через пробел\n").split())
print(f"вероятность что из {n} бросков кости {m} из них будет больше либо равно {s} =", dice(n, m, s))
