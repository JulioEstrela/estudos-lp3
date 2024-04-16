# Ex01 - Jogo de Adivinhação: 
# Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
# Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

def guessingGame():
    import random
    randomNumber = random.randint(1, 100)
    print("JOGO DE ADVINHAÇÃO\n")
    tries = 1
    while True:
        userGuess = int(input("Escolha um número de 1 a 100: "))

        if userGuess == randomNumber:
            print("\nParabéns! Você acertou o número escolhido aleatoriamente.")
            print(f"O número era: {randomNumber}")
            print(f"Número de tentativas: {tries}")
            break
        if userGuess > randomNumber:
            # Decidi usar ABAIXO e ACIMA para facilitar o entendimento.
            # Achei "O palpite está acima" e "O palpite está abaixo" confuso.
            print("O número correto está ABAIXO")
        else:
            print("O número correto está ACIMA")

        tries += 1

guessingGame()