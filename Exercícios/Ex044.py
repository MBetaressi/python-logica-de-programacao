from colorama import Fore
print("============ LOJAS BETARESSI =============")
preco: float = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO")
print("[1] à vista dinheiro/cheque")
print("[2] à vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
opcao: int = int(input("Qual é a opção: "))

if opcao == 1:
    custo: float = preco * 0.9
    print(f"Sua compra de R${preco:.2f} vai custar R${custo:.2f}")
elif opcao == 2:
    custo: float = preco * 0.8
    print(f"Sua compra de R${preco:.2f} vai custar R${custo:.2f}")
elif opcao == 3:
    valor_parcela: float = preco / 2
    print(f"Sua compra será parcelada em 2x de R${valor_parcela:.2f} SEM JUROS")
    print(f"Sua compra de R${preco:.2f} vai custar R${preco:.2f}")
elif opcao == 4:
    nparcelas: int = int(input("Quantas parcelas ? "))
    valor_parcela: float = (preco * 1.2) / nparcelas
    custo: float = valor_parcela * nparcelas
    print(f"Sua compra será parcelada em {nparcelas}x de R${valor_parcela:.2f} COM JUROS")
    print(f"Sua compra de R${preco:.2f} vai custar R${custo:.2f}")
else:
    print(Fore.LIGHTRED_EX + "Opção inválida de pagamento. Tente novamente!")

