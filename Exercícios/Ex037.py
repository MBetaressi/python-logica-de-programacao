num: int = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:")
print("[1] Coverter para BINÁRIO")
print("[2] Converter para OCTAL")
print("[3] Converter para HEXADECIMAL")
opcao: int = int(input("Sua opção: "))

if opcao == 1:
    print(f"{num} em BINÁRIO é {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} em OCTAL é {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} em HEXADECIMAL é {hex(num)[2:].upper()}")
else:
    print("Opção inválida! Tente novamente")


