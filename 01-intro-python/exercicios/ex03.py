valorDeCompra = float(input())
valorFinal = valorDeCompra

if valorDeCompra > 0 and valorDeCompra < 10:
    desconto = 0
elif valorDeCompra < 100:
    desconto = 0.05
    valorFinal -= valorDeCompra * desconto
elif valorDeCompra < 500:
    desconto = 0.1
    valorFinal -= valorDeCompra * desconto
else:
    desconto = 0.15
    valorFinal -= valorDeCompra * desconto


print(f"Valor final com desconto: {valorFinal}")

print(f"Desconto de {desconto * 100:.0f}%")