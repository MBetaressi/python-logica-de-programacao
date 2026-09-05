frase = "   Curso em vídeo Python   "
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print("""Welcome! Are you completely new to prgramming?
If so, you might want to start with the Python track,
which will teach you the fundamentals of programming in Python.
If you already know how to program, you might want to check out our other tracks,
which will teach you how to use Python for data science, web development, and more.""")

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Java'))
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('curso'))
print(frase.split())

