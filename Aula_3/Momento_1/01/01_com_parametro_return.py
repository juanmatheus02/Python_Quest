'''1. Crie uma função chamada calcular_media() que receba duas notas e
retorne a média. Depois, mostre o resultado final.'''

def calcular_media(a,b):
    total = (a+b)/2
    return total

a = float(input("Valor 1: "))
b = float(input("Valor 2: "))

print(calcular_media(a,b))