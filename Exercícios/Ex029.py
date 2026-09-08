from colorama import Fore

velocidade: float = float(input("Qual é a velocidade atual do carro? "))
limite: int = 80
if velocidade > limite:
    multa: float = 7 * (velocidade - limite)
    print(Fore.RED + "Multado! Você excedeu o limite permitido que é de 80Km/h")
    print(Fore.RED + "Você deve pagar uma multa de " + Fore.YELLOW + f"R${multa:.2f}")
print(Fore.YELLOW + "Tenha um bom dia! Dirija com segurança!")
