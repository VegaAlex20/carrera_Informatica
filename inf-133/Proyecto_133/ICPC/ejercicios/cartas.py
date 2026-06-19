def obtener_numeros_de_tarjeta(tarjeta):
    numeros = []
    paso = 2 ** (tarjeta - 1)
    for i in range(1, 61):
        if (i - 1) % (2 * paso) < paso:
            numeros.append(i)
    return set(numeros)

# Preprocesar todas las tarjetas
tarjetas = {}
for i in range(1, 61):
    tarjetas[i] = obtener_numeros_de_tarjeta(i)

def adivinar_numero_secreto(tarjetas_dadas):
    # Iniciar el conjunto de números posibles con todos los números del 1 al 60
    numeros_posibles = set(range(1, 61))
    # Intersectar con los números en cada tarjeta dada
    for tarjeta in tarjetas_dadas:
        numeros_posibles &= tarjetas[tarjeta]
    # Filtrar números fuera del rango [1, 10]
    numeros_posibles = {num for num in numeros_posibles if 1 <= num <= 10}
    # Debe quedar un único número posible
    return numeros_posibles.pop()

# Leer la entrada
q = int(input())
for _ in range(q):
    datos = list(map(int, input().split()))
    k = datos[0]
    tarjetas_dadas = datos[1:]
    print(adivinar_numero_secreto(tarjetas_dadas))
