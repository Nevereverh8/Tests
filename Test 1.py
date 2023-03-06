a = list(map(int, input().split()))
s = set(a)
b = []

for i in a:
    if i in s:
        b.append(i)
        s.remove(i)
    else:
        if i in b:
            b.remove(i)
b.sort()
for i in b:
    print(i, end=' ')
