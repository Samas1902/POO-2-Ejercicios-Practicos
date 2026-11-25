frase = input("Frase: ")
# Escriba su solución aquí
palabras = frase.lower().split()
frecuencia = {}
for p in palabras:
    if p in frecuencia:
        frecuencia[p] += 1
    else:
        frecuencia[p] = 1
for palabra,valor in frecuencia.items():
    print(f"{palabra}: {valor}")


