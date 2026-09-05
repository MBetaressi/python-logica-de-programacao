from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(co, ca)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")

print('\n')

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
print(f"A hipotenusa  vai medir {hipotenusa:.2f}")
