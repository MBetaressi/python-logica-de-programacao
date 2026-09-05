valor = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = valor / 4.98
euro = valor / 5.87
print(f"Com R${valor}, você pode comprar US${dolar:.2f}")
print(f"Com R${valor}, você pode comprar {euro:.2f}EURO")