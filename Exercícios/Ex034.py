salario: float = float(input("Qual é o salário do funcionário? "))
if salario <= 1250:
    aumento: float = salario * 1.15
else: 
    aumento: float = salario * 1.10
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f}")