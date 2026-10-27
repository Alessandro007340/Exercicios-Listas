print("Algoritmo para verificar e apresentar os nomes das pessoas maiores de idade")
print()
nomes = [0]*7
idades = [0]*7
maiores = []
for i in range(len(nomes)):
    nomes[i] = str(input(f"Informe o {i+1}° nome: "))
    idades[i] = int(input("Informe a idade dessa pessoa: "))
for i in range(len(idades)):
    if idades[i] >= 18:
        maiores.append(nomes[i])
print(f"Os maiores de idade são: {maiores}")