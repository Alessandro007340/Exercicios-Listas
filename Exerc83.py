print("Algoritmo para requisitar 18 números inteiros e apresentá-los em ordem inversa à ordem de entrada.")
print()
l = [0]*18
for i in range(len(l)):
    l[i] = int(input(f"Informe o {i+1}° valor: "))
l.reverse()
print(l)