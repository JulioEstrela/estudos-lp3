def calcular_volume(comprimento, altura, largura) -> float:
    return (comprimento * altura * largura) / 1000

def calcular_potencia(volume, temperatura_desejada, temperatura_ambiente) -> float:
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def calcular_litros_filtragem_por_hora(volume) -> float:
    return 2 * volume