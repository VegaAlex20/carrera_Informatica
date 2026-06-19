def puede_caer_todas(n, alturas, distancias):
    for i in range(n):
        alcance = alturas[i]
        for j in range(i + 1, n):
            if alcance >= sum(distancias[i:j]):
                alcance += alturas[j]
            else:
                break
        if alcance >= sum(distancias[i:]):
            return True
    return False

def resolver_franklin(casos):
    resultados = []
    for caso in casos:
        n = caso['n']
        alturas = caso['alturas']
        distancias = caso['distancias']
        if puede_caer_todas(n, alturas, distancias):
            resultados.append("habibi")
        else:
            resultados.append("which")
    return resultados

# Leer la entrada
import sys
input = sys.stdin.read
data = input().split()

indice = 0
t = int(data[indice])
indice += 1

casos = []

for _ in range(t):
    n = int(data[indice])
    indice += 1
    alturas = list(map(int, data[indice:indice + n]))
    indice += n
    distancias = list(map(int, data[indice:indice + n - 1]))
    indice += n - 1
    casos.append({'n': n, 'alturas': alturas, 'distancias': distancias})

# Resolver los casos
resultados = resolver_franklin(casos)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
