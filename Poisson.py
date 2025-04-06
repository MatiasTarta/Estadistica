import math
print("Calculadora de Poisson")
media=float(input("Ingrese la media de Poisson"))
intervalo=int(input("Ingrese el maximo del intervalo"))



def poisson(media, intervalo):
    return ((math.e ** -media) * (media ** intervalo)) / math.factorial(intervalo)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
