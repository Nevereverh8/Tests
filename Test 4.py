def mtrx_trnsp(a):
    b = []
    for j in range(m):
        b.append([])
        for i in range(n):
            b[j].append(a[i][j])
    return b


n, m = list(map(int, input("Введите размерность матрицы через пробел ").split()))
x = []
print("Введите строки матрицы через пробел ")
for i in range(n):
    x.append(list(map(int, input().split())))


for i in mtrx_trnsp(x):
    for j in i:
        print(j, end=' ')
    print()

print('Размерность изначальной матрицы', len(x), 'x', len(x[0]))
print('Размерность конечной матрицы', len(mtrx_trnsp(x)), 'x', len(mtrx_trnsp(x)[0]))

