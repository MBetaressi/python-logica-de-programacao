print("-=-" * 20)
print("Analisador de triângulos")
print("-=-" * 20)
seg1: float = float(input("Primeiro segmento: "))
seg2: float = float(input("Segundo segmento: "))
seg3: float = float(input("Terceiro segmento: "))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("Os segmentos acima PODEM FORMAR triângulo")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")
