def cos_sim(a, b):
    if len(a) == len(b):
        dot = sum(a[i]*b[i] for i in range(len(a)))
        sq_modulus_a = (sum(i**2 for i in a))
        sq_modulus_b = (sum(i**2 for i in b))
        return dot / (sq_modulus_a * sq_modulus_b)**0.5
    else:
        return 'Невозможно определить косинусное расстояние так как вектора имеют разную размерность'


v1 = list(map(int, input('Введите координаты 1-ого вектора через пробел\n').split()))
v2 = list(map(int, input('Введите координаты 2-ого вектора через пробел\n').split()))

print('Косинусное расстояние между векторами = ', cos_sim(v1, v2))
