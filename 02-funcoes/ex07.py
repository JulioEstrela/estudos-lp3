# Ex07 - Jogo da Forca:
# Implemente uma versão simples do jogo da forca.
# O programa começa com uma palavra oculta (o usuário não vê)
# e o usuário tenta adivinhar a palavra, letra por letra. 
# O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

def jogarForca(PALAVRA_OCULTA: str, NUMERO_DE_TENTATIVAS: int = 6):
    tentativasRestantes = NUMERO_DE_TENTATIVAS
    forca = ['_'] * len(PALAVRA_OCULTA)

    while True:
        print(f"\nFORCA - Tentativas restantes: {tentativasRestantes}")
        print(*forca)

        # Dá pra otimizar, 
        # invés de fazer esse loop poderia verificar se todas as letras presentes na palavra já foram inseridas.
        # Ou usar contador
        # Além disso, fazer essa verificação apenas quando o usuário digitar uma nova letra.
        if '_' not in forca: 
            print("YOU WIN - Parabéns, você acertou a palavra")
            break
        
        letra = input("Digite uma letra: ")
        if len(letra) > 1:
            continue

        
        if letra not in PALAVRA_OCULTA:
            tentativasRestantes -= 1
            if tentativasRestantes == 0:
                print("GAME OVER - Tentativas Esgotadas")
                break
            continue

        else:
            for i, c in enumerate(PALAVRA_OCULTA):
                if letra == c:
                    forca[i] = letra

jogarForca("latorre", 2)