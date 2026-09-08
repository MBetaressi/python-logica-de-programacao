dist: float = float(input("Qual é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {dist:.1f}Km")
if dist <= 200:
    preco: float = 0.50 * dist
else:
    preco: float = 0.45 * dist
print(f"O preço da sua viagem será de R${preco:.2f}") 