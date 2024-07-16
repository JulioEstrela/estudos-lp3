# Ex05 - Verificador de Palíndromos:
# Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo
# (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

def is_palindromo(frase: str, considerarEspacos: bool) -> bool:
    if considerarEspacos == False:
        frase = frase.replace(' ', '')
    if frase == frase[::-1]:
        return True
    else:
        return False

fraseDoUsuario = input("Insira uma frase:\n")

print("\nConsiderando espaços:")
if is_palindromo(fraseDoUsuario, considerarEspacos=True):
    print("É palíndromo")
else:
    print("Não é palíndromo")

print("\nDesconsiderando os espaços:")
if is_palindromo(fraseDoUsuario, considerarEspacos=False):
    print("É palíndromo")
else:
    print("Não é palíndromo")