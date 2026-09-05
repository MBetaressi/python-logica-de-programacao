import math
num = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print(f"O ângulo de {num} tem o SENO de {seno:.2f}")
print(f"O ângulo de {num} tem o COSSENO de {cosseno:.2f}")
print(f"O ângulo de {num} tem a TANGENTE de {tangente:.2f}")
