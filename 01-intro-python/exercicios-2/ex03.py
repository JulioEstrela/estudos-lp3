# Ex03 - Contador de Vogais e Consoantes: 
# Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

def vogais(frase: str) -> int:
    # Não funciona para frases acentuadas
    vogais = ['a', 'e', 'i', 'o', 'u']
    frase = frase.lower()
    contador = 0
    for c in frase:
        if c in vogais:
            contador += 1
    return contador

def consoantes(frase: str) -> int:
    # Não funciona para frases acentuadas
    vogais = ['a', 'e', 'i', 'o', 'u']
    frase = frase.lower()
    contador = 0
    for c in frase:
        if c not in vogais:
            contador += 1
    return contador

fraseDoUsuario = input("Digite uma frase:\n")
print(f"Número de vogais: {vogais(fraseDoUsuario)}")
print(f"Número de consoantes: {consoantes(fraseDoUsuario)}")