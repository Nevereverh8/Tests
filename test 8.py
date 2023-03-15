from random import randint



def central_tend(a):
    #average
    average = sum(a)/len(a)
    #mode
    c = {}
    mode = []
    for i in a:
        if i in c.keys():
            c[i] += 1
        else:
            c[i] = 1
    for i in c.keys():
        if c[i] == max(c.values()):
            mode.append(i)
    ###median
    a.sort()
    if len(a) % 2 == 0:
        median = (a[len(a)//2] + a[len(a)//2+1])/2
    else:
        median = a[len(a)//2]
    return average, mode, median


m = [randint(0, 1000) for i in range(500)]
print("Среднее =", central_tend(m)[0], "\nмода -", central_tend(m)[1], "\nмедиана =", central_tend(m)[2])