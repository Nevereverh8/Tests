def cos_sim(a, b):
    if len(a) == len(b):
        dot = sum(a[i]*b[i] for i in range(len(a)))
        sq_modulus_a = (sum(i**2 for i in a))
        sq_modulus_b = (sum(i**2 for i in b))
        return dot / (sq_modulus_a * sq_modulus_b)**0.5
    else:
        return 'Cannot define cosinus simularity: vectors have diffirent dimensions'


v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))

print(cos_sim(v1, v2))
