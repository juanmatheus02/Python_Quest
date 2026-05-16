"""Para as questões de 1 a 4
anteriormente realizadas, solicitar que
a pessoa usuária informe quantas vezes 
deseja realizar as operações e utilize 
o comando de repetição para realizar a
operação."""

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

vezes = int(input("Quantas vezes? "))

for i in range(vezes):
    a = float(input("Nota 1: "))
    b = float(input("Nota 2: "))
    resultado = calcular_media(a, b)
    print(f"Resultado: {resultado}")

