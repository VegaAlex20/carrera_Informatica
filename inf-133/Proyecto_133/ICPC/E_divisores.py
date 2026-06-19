def factores_primos(n):
    while(n<2 or n>10**5):
        n = int(input())
    i = 2
    factores = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factores.append(i)
    if n > 1:
        factores.append(n)
    return 'x'.join(map(str, factores))

n = int(input())
print(factores_primos(n))





