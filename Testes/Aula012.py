#Condições aninhadas
nome: str = str(input("Digite o seu nome: "))
if nome == "Mateus":
    print("Que nome bonito !")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil !")
elif nome in "Ana Jéssica Juliana Giovana":
    print("Belo nome feminino !")
else:
    print("Seu nome é bem normal !")
print(f"Tenha um bom dia, {nome} !!")