def _calcular_imc(peso, altura) -> float:
    return peso / (altura ** 2)

def classificar_imc(peso, altura) -> str:
    imc = _calcular_imc(peso, altura)

    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    elif imc < 35:
        return "Obesidade de Classe 1"
    elif imc < 40:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def calcular_diferenca_peso(peso, altura) -> float:
    peso_normal = 24.9 * (altura ** 2)
    diferenca = peso_normal - peso
    return diferenca
