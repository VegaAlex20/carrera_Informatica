from sympy import symbols, integrate, Rational

x = symbols('x')

def calcular_area(A, B, C, L, R):           
    f = A*x**2 + B*x + C
    area = integrate(f, (x, L, R))
    area = Rational(str(area)).limit_denominator()
    return f'{area.numerator}/{area.denominator}'

t = int(input("Ingrese el número de casos de prueba: "))
for _ in range(t):
    A, B, C, L, R = map(int, input("Ingrese los coeficientes A, B, C y el rango L, R: ").split())
    print(calcular_area(A, B, C, L, R))
