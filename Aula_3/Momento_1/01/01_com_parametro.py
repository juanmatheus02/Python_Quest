'''1. Crie uma função chamada calcular_media() que receba duas notas e
retorne a média. Depois, mostre o resultado final.'''

def calcular_media (a,b):
    total = (a+b)/2
    print(total)

a = float(input("Número 1: "))
b = float(input("Número 2: "))
calcular_media(a,b)