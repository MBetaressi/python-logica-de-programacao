from random import randint
from time import sleep
from colorama import Fore
print("SUAS OPÇÕES:")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")
opcao: int = int(input("QUAL É A SUA JOGADA ? "))

if opcao < 0 or opcao > 2:
    print(Fore.LIGHTRED_EX + "Opção inválida!")
    exit()

itens = ["Pedra", "Papel", "Tesoura"]

computador: int = randint(0, 2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("-=" * 15)
#Jogada do computador
print(f"Computador jogou {itens[computador]}")

#Jogada do jogador
print(f"Jogador jogou {itens[opcao]}")
print("-=" * 15)

#Confronto
if opcao == computador:
    print("EMPATE")
elif opcao == 0: #Jogador jogou pedra
    if computador == 1:
        print("COMPUTADOR VENCE")
    elif computador == 2:
        print("JOGADOR VENCE")
elif opcao == 1: #Jogador jogou papel
    if computador == 0:
        print("JOGADOR VENCE")
    elif computador == 2:
        print("COMPUTADOR VENCE")
elif opcao == 2: #Jogador jogou tesoura
    if computador == 0:
        print("COMPUTADOR VENCE")
    elif computador == 1:
        print("JOGADOR VENCE")

