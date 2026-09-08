from random import randint
from time import sleep
from colorama import Fore

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
print("-=-" * 20)
computador: int = randint(0, 5) #Faz o computador "PENSAR"
sleep(1)
jogador: int = int(input("Em que número eu pensei? ")) #Escolha do jogador
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print(Fore.GREEN + "PARABÉNS! Você conseguiu me vencer!")
else:
    print(Fore.RED + f"GANHEI! Eu pensei no número {computador} e não no {jogador}")
