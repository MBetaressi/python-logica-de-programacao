n1: float = float(input("Primeira nota: "))
n2: float = float(input("Segunda nota: "))
media: float = (n1 + n2) / 2
print(f"Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}")

if media >= 7:
    print("O aluno está APROVADO")
elif 7 > media >= 5:
    print("O aluno está em RECUPERAÇÃO")
else:
    print("O aluno está REPROVADO")