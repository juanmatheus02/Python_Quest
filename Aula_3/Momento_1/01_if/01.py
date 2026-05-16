"""Crie uma função chamada calcular_media()
que receba duas notas e retorne a média. 
SE a média for maior 70 ‘Aprovado’, SE menor que 40
‘Reprovado’, SENÃO ‘Final’"""

def calcular_media(a,b):
    total = (a+b)/2
    return total

a = float(input("Nota 1:" ))
b = float(input("Nota 2:" ))

total = calcular_media(a,b)

if (total >=7):
    print("Media: ", total, "Aprovado")
elif(total <40):
    print("Média: ", total, "Reprovado")
else:
    print("Media: ", total, "Final")
