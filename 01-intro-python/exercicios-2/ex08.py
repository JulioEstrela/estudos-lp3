# Ex08 - Função de Contagem de Palavras:
# Escreva uma função que receba uma string (frase) como argumento e 
# retorne um dicionário onde as chaves são as palavras únicas no texto e
# os valores são o número de vezes que cada palavra aparece no texto.
# Depois, teste a função com diferentes textos fornecidos pelo usuário.


def retornarDicionario(frase: str) -> dict:
    import string
    frase = frase.strip()

    for c in frase:
        if c not in string.ascii_letters + ' ':
            frase = frase.replace(c, '')
    
    palavras = frase.split()
    dicionario = dict.fromkeys(palavras)

    for palavra in palavras:
        dicionario[palavra] = frase.count(palavra)

    return dicionario


# TESTES
import string

# Should return {}, because punctuation should be ignored
print(retornarDicionario(string.punctuation))

# Should return {}, because whitespace should be ignored 
print(retornarDicionario(string.whitespace))

# Should return {'palavra': 4}
print(retornarDicionario("palavra1, palavra1, palavra2, palavra3"))

# Should return {'palavraUm': 1, 'palavraDois': 1}, because words are split by one, and only one, whitespace
print(retornarDicionario("palavraUm        palavraDois"))

# Should return {'palavraUm': 2, 'palavraDois': 3, 'palavraTres': 1}, as expected
print(retornarDicionario("palavraUm palavraDois palavraUm palavraDois palavraDois palavraTres"))

