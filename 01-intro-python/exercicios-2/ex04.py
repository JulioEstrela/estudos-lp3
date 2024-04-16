# Ex04 - Simulador de Eleições:
# Crie um programa que simule uma votação com três candidatos. 
# O programa deve pedir ao usuário para votar várias vezes e,
# no final, mostrar o número de votos de cada candidato e quem foi o vencedor.


def votar(quantidadeDeVotos = 5):
    votosCandidato1 = 0
    votosCandidato2 = 0
    votosCandidato3 = 0

    print("Candidatos")
    print("Candidato 1 (opção 1)")
    print("Candidato 2 (opção 2)")
    print("Candidato 3 (opção 3)")

    for _ in range(quantidadeDeVotos):

        while True:
            votoDoUsuario = int(input('Vote na opção do seu candidato: '))
            if votoDoUsuario <= 3 and votoDoUsuario >= 1:
                break
            print("INVÁLIDO! Vote entre 1 e 3")

        # Decidi usar if-else invés de match-case para ser compatível com a versão 3.8 do Python (utilizada nas maratonas)
        if votoDoUsuario == 1:
            votosCandidato1 += 1
        elif votoDoUsuario == 2:
            votosCandidato2 += 1
        elif votoDoUsuario == 3:
            votosCandidato3 += 1

    print("Votação encerrada")
    print(f"Candidato 1: {votosCandidato1} votos")
    print(f"Candidato 2: {votosCandidato2} votos")
    print(f"Candidato 3: {votosCandidato3} votos")

votar(quantidadeDeVotos=5)