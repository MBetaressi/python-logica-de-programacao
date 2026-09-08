#Geração de diferentes cores, por meio do ANSI escape sequence 
print("Olá, mundo!")

#Texto em vermelho
print("\033[31mOlá, mundo!\033[m")

#Texto em vermelho com fundo amarelo
print("\033[31;43mOlá, mundo!\033[m")

#Em negrito, texto vermelho e fundo amarelo
print("\033[1;31;43mOlá, mundo!\033[m")

#Sublinhado, texto branco e fundo magenta
print("\033[4;30;45mOlá, mundo!\033[m")

#Texto branco e fundo preto
print("\033[30mOlá, mundo!\033[m")

#Fundo branco e texto preto
print("\033[7;30mOlá, mundo!\033[m")

#Texto amarelo e fundo azul
print("\033[0;33;44mOlá, mundo!\033[m")

#Texto azul e fundo amarelo
print("\033[7;33;44mOlá, mundo!\033[m")

#Valores verde e vermelhos
a = 3
b = 5
print(f"Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m")