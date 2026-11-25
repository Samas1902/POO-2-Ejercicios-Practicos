def saludo():
    nombre = input("Ingrese su nombre: ").strip()
    print(f"Ola {nombre}\n")

def pregunta_1():
    print("\nPregunta 1:")
    print('Código:\nciudad = "Paute y"\nprint(ciudad[-1].upper())')
    ciudad = "Paute y"
    resultado = ciudad[-1].upper()
    print(f"Salida: {resultado}\n")

def pregunta_2():
    print("\nPregunta 2:")
    print("Código:\nprint(type(10.0))")
    resultado = type(10.0)
    print(f"Salida: {resultado}\n")

def pregunta_3():
    print("\nPregunta 3:")
    print("Código:\na = {1, 2, 3, 4}\nb = {3, 4, 5}\nprint(len(a & b))")
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    resultado = len(a & b)
    print(f"Salida: {resultado}\n")

def pregunta_4():
    print("\nPregunta 4:")
    print("Código:\nprint(int(9.99))")
    resultado = int(9.99)
    print(f"Salida: {resultado}\n")

def pregunta_5():
    print("\nPregunta 5:")
    print("Código:\na = [1, 2, 3]\nb = a\nb[0] = 5\nprint(a)")
    a = [1, 2, 3]
    b = a
    b[0] = 5
    print(f"Salida: {a}\n")

def pregunta_6():
    print("\nPregunta 6:")
    print("Código:\nsaldo = 350\nif saldo >= 1000:\n    print('Oro')\nelif saldo >= 100:\n    print('Plata')\nelse:\n    print('Básica')")
    saldo = 350
    print("Salida: ", end="")
    if saldo >= 1000:
        print("Oro")
    elif saldo >= 100:
        print("Plata")
    else:
        print("Básica")
    print()

def pregunta_7():
    print("\nPregunta 7:")
    print('Código:\nfor i in range(3):\n    for j in range(2):\n        print("*", end="")')
    print("Salida: ", end="")
    for i in range(3):
        for j in range(2):
            print("*", end="")
    print("\n")

def pregunta_8():
    print("\nPregunta 8:")
    print("Código:\nfor x in [2, 4, 6]:\n    if x == 7:\n        print('Encontrado')\n        break\nelse:\n    print('No encontrado')")
    print("Salida: ", end="")
    for x in [2, 4, 6]:
        if x == 7:
            print("Encontrado")
            break
    else:
        print("No encontrado")
    print("\n")

def pregunta_9():
    print("\nPregunta 9:")
    print('Código:\nnotas = {"Ana": 10, "Luis": 8}\nfor nombre, nota in notas.items():\n    print(f"{nombre}:{nota}", end=" ")')
    notas = {"Ana": 10, "Luis": 8}
    print("Salida: ", end="")
    for nombre, nota in notas.items():
        print(f"{nombre}:{nota}", end=" ")
    print("\n")

def pregunta_10():
    print("\nPregunta 10:")
    print("Código:\nfor n in [1, 2, 3, 4]:\n    if n == 3:\n        break\n    print(n, end=' ')")
    print("Salida: ", end="")
    for n in [1, 2, 3, 4]:
        if n == 3:
            break
        print(n, end=" ")
    print("\n")

def pregunta_11():
    print("\nPregunta 11:")
    print('Código:\nfrase = "El sol y el mar"\npalabras = frase.lower().split()\nfrecuencia = {}\nfor p in palabras:\n    if p in frecuencia:\n        frecuencia[p] += 1\n    else:\n        frecuencia[p] = 1\nfor palabra, valor in frecuencia.items():\n    print(f"{palabra}: {valor}")')
    frase = "El sol y el mar"
    palabras = frase.lower().split()
    frecuencia = {}
    for p in palabras:
        if p in frecuencia:
            frecuencia[p] += 1
        else:
            frecuencia[p] = 1
    print("Salida:")
    for palabra, valor in frecuencia.items():
        print(f"{palabra}: {valor}")
    print()

def ejecutar_todas():
    pregunta_1()
    pregunta_2()
    pregunta_3()
    pregunta_4()
    pregunta_5()
    pregunta_6()
    pregunta_7()
    pregunta_8()
    pregunta_9()
    pregunta_10()
    pregunta_11()

def menu_preguntas():
    while True:
        print("================================")
        print("            PREGUNTAS           ")
        print("================================")
        print("1. Pregunta 1 (ciudad[-1].upper())")
        print("2. Pregunta 2 (type(10.0))")
        print("3. Pregunta 3 (len(a & b))")
        print("4. Pregunta 4 (int(9.99))")
        print("5. Pregunta 5 (Asignación listas)")
        print("6. Pregunta 6 (Condicional saldo)")
        print("7. Pregunta 7 (Bucles anidados)")
        print("8. Pregunta 8 (For con else)")
        print("9. Pregunta 9 (Diccionario items)")
        print("10. Pregunta 10 (For con break)")
        print("11. Pregunta 11 (Frecuencia de palabras)")
        print("12. Ejecutar TODAS las preguntas")
        print("13. Volver")
        
        opc = input("Seleccione una opción (1-13): ").strip()
        
        if opc == "1":
            pregunta_1()
        elif opc == "2":
            pregunta_2()
        elif opc == "3":
            pregunta_3()
        elif opc == "4":
            pregunta_4()
        elif opc == "5":
            pregunta_5()
        elif opc == "6":
            pregunta_6()
        elif opc == "7":
            pregunta_7()
        elif opc == "8":
            pregunta_8()
        elif opc == "9":
            pregunta_9()
        elif opc == "10":
            pregunta_10()
        elif opc == "11":
            pregunta_11()
        elif opc == "12":
            ejecutar_todas()
        elif opc == "13":
            print("Volviendo al menú principal\n")
            break
        else:
            print("ERROR elige entre 1 y 13\n")

def main():
    while True:
        print("              MENÚ              ")
        print("--------------------------------")
        print("1. Saludo")
        print("2. Menu de preguntas")
        print("3. Salir")
        
        opcion = input("Elija una opción (1-3): ").strip()
        
        if opcion == "1":
            saludo()
        elif opcion == "2":
            menu_preguntas()
        elif opcion == "3":
            print(f"Saliendo...")
            break
        else:
            print("ERROR. Ingrese 1, 2 o 3\n")
main()