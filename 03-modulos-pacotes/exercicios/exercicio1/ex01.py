from aquario import *

comprimento = float(input("Insira o comprimento: "))
altura = float(input("Insira a altura: "))
largura = float(input("Insira a largura: "))
temperatura_desejada = float(input("Insira a temperatura desejada: "))
temperatura_ambiente = float(input("Insira a temperatura ambiente: "))

volume = calcular_volume(comprimento, altura, largura)
potencia = calcular_potencia(volume, temperatura_desejada, temperatura_ambiente)
litros_filtragem_por_hora = calcular_litros_filtragem_por_hora(volume)

print()
print("Dados do aquário".center(50, "-"))
print("Volume em litos:", volume)
print("Potencia necessária:", potencia)
print("Quantidade de litros/hora necessária:", litros_filtragem_por_hora)