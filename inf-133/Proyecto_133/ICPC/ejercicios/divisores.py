def suma_divisores_propios(n):
    suma = 1  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            suma += i
            if i != n // i:  
                suma += n // i
    return suma

def clasificar_numero(n):
    suma_divisores = suma_divisores_propios(n)
    if suma_divisores == n:
        return 'perfecto'
    elif suma_divisores > n:
        return 'abundante'
    else:
        suma_divisores_del_suma = suma_divisores_propios(suma_divisores)
        if suma_divisores_del_suma == n:
            return 'romántico'
        else:
            return 'complicado'
        
def obtener_entrada_valida(min_val, max_val):
    while True:
        try:
            valor = int(input())
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"Por favor, ingrese un número entre {min_val} y {max_val}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

n = obtener_entrada_valida( 1, 10**5)

for _ in range(n):
    a = obtener_entrada_valida(1, 10**5)
    clasificacion = clasificar_numero(a)
    print(f'{a} {clasificacion}')






def suma_divisores_propios(n):
    if n == 1:
        return 0
    suma = 1  # 1 siempre es divisor propio de cualquier n > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            suma += i
            if i != n // i:
                suma += n // i
    return suma

def clasificar_numero(n):
    suma1 = suma_divisores_propios(n)
    if suma1 == n:
        return f"{n} perfecto"
    
    suma2 = suma_divisores_propios(suma1)
    if suma2 == n:
        resultado = f"{n} romantico"
        if suma1 > n:
            resultado += " abundante"
        return resultado
    
    if suma1 > n:
        return f"{n} abundante"
    
    return f"{n} complicado"

# Leer la entrada
n = int(input())
numeros = [int(input()) for _ in range(n)]

# Procesar cada número y obtener su clasificación
for numero in numeros:
    print(clasificar_numero(numero))

