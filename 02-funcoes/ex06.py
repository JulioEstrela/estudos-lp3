# Ex06 - Conversor de Notas Escolares:
# Baseado em uma pontuação fornecida pelo usuário (0 a 100),
# converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

# Para esse exercício, utilizei o seguinte padrao de conversão:
# A -> 100
# B -> [90, 99]
# C -> [70, 89]
# D -> [60, 69]
# F -> [0, 59]


def translateGrade(grade: int) -> str:
    # Decidi usar if-else invés de match-case para ser compatível com a versão 3.8 do Python (utilizada nas maratonas)
    if grade < 60:
        return 'F'
    elif grade < 70:
        return 'D'
    elif grade < 90:
        return 'C'
    elif grade < 100:
        return 'B'
    else:
        return 'A'

pontuacao = int(input("Digite a pontuação: "))
print(translateGrade(pontuacao))