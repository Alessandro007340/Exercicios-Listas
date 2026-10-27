print("Algoritmo que requisita 12 números inteiros e apresenta os pares e os ímpares")
print()
l = [0]*12
pares = []
impares = []
for i in range(len(l)):
    l[i] = int(input(f"Informe o {i+1}° valor: "))
for i in range(len(l)):
    v = i % 2
    if v == 0:
        pares.append(i)
    else: 
        impares.append(i)
print(f"Os números pares inseridos foram {pares}")
print(f"Os núemros ímpares inseridos foram {impares}") 