# Ex02 - Tabuada de Um Número:
# Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

def tabuada(n: int):
    tabuadaLista = []

    print("TABUADA")
    for i in range(1, 11):
        tabuadaLista.append(f"{n} x {i} = {n * i}")
    
    return str('\n'.join(tabuadaLista))

numero = int(input("Digite o número da tabuada: "))
print(tabuada(numero))