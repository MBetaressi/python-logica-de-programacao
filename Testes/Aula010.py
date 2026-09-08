#Estrutura condicional simples
nome: str = str(input("Qual é o seu nome? "))
if nome == "Mateus":
    print("Que nome lindo você tem!")
print(f"Bom dia, {nome}!")

print("--------------------------------------------------")

#Estrutura condicional composta
nome: str = str(input("Qual é o seu nome? "))
if nome == "Mateus":
    print("Que nome lindo você tem!")
else: 
    print("Seu nome é tão normal!")
print(f"Bom dia, {nome}!")

print("--------------------------------------------------")

n1: float = float(input("Digite a primeira nota: "))
n2: float = float(input("Digite a segunda nota: "))
m: float = (n1 + n2) / 2
print(f"A sua média foi {m:.1f}")
if m >= 7:
    print("Sua média foi boa! PARABÉNS!")
else:
    print("Sua média foi ruim! ESTUDE MAIS!")

    