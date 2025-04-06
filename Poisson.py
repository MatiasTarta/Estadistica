import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def poisson(media, intervalo):
    return ((math.e ** -media) * (media ** intervalo)) / math.factorial(intervalo)

print("Calculadora de Poisson")
media = float(input("Ingrese la media de Poisson: "))
intervalo = int(input("Ingrese el maximo del intervalo: "))

x = int(input("1 para mostrar valor solo, 2 para mostrar tabla: "))

if x == 1:
    print(poisson(media, intervalo))
else:
    for i in range(intervalo + 1):
        print(f"{i}: {poisson(media, i)}")
