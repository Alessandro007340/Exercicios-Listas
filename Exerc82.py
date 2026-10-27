print("Algoritmo para requisitar 11 valores e apresentá-los")
print()
l = [0]*11
for i in range(len(l)):
    l[i] = float(input(f"Informe o {i+1}° número: "))
for i in range(len(l)):
    print(f"{l[i]}")
    print("---------------------")

 
