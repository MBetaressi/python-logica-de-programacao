from datetime import date
ano_nascimento: int = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}")

if idade == 18:
    print("Você deve se alistar imediatamente!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento")
    ano = ano_atual + saldo
    print(f"Seu alistamento será em {ano}")
elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo} anos")
    ano = ano_atual - saldo
    print(f"Seu alistamento foi em {ano}")
