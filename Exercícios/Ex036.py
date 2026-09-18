valor: float = float(input("Qual é o valor da casa: R$"))
salario: float = float(input("Qual o salário do comprador: R$"))
anos: int = int(input("Quantos anos de financiamento ? "))
prestacao: float = valor / (anos * 12)
print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos, o valor da prestação será de R${prestacao:.2f}")

minimo = prestacao * 0,3
if prestacao > minimo:
    print("Empréstimo NEGADO!")
    print("O valor da prestação excedeu 30% do salário!")
else: 
    print("O empréstimo pode ser CONCEDIDO!")