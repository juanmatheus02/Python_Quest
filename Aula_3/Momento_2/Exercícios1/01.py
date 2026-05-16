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

media = [a,b]

for i in range (3):
    media = float(input("Digite a média: "))
    media.append(media)

print("Listando", media)