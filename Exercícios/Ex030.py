from colorama import Fore

num: int = int(input(Fore.LIGHTMAGENTA_EX + "Me diga um número qualquer: "))
if num % 2 == 0:
    print(Fore.BLUE + f"O número {num} é par")
else:
    print(Fore.BLUE + f"O número {num} é impar")