from imc import classificar_imc, calcular_diferenca_peso

peso = float(input("Insira o peso (Kg): "))
altura = float(input("Insira a altura (m): "))

print("Classificação IMC:", classificar_imc(peso, altura))

diferenca_peso = calcular_diferenca_peso(peso, altura)
ganhar_ou_perder = "ganhar" if diferenca_peso > 0 else "perder"
print(f"O indivíduo precisa {ganhar_ou_perder} {abs(diferenca_peso) :.2f} kg para atingir IMC = 24,9")
