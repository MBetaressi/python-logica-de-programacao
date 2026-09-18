peso: float = float(input("Qual é o seu peso ? (Kg) "))
altura: float = float(input("Qual é a sua altura ? (m) "))
imc: float = peso / (altura ** 2)
print(f"O IMC dessa pessoa é {imc:.1f}")

if imc <= 18.5:
    print("Você está ABAIXO DO PESO")
elif imc <= 25:
    print("Parabéns, você está no PESO IDEAL")
elif imc <= 30:
    print("Você está em SOBREPESO")
elif imc <= 35:
    print("Você está em OBESIDADE")
else:
    print("Você está em OBESIDADE MÓRBIDA")