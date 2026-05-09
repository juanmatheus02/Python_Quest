"""4. Um sistema de logística registra quantas entregas foram feitas por viagem. 
O usuário digita o número de entregas de cada viagem. 
O sistema para quando digitar 0 (zero)e mostra o total de entregas"""

total = 0
while True:
    entregas = float(input("Digite o número de entregas: "))
    total = entregas + total
    print(total)
    if entregas == 0:
        break
print(f"Total de entregas: {total}")