#Declaracion de funciones
def saludar():
    print("Hola bro")

saludar()

#Funcion con parametros
def calcular_edad(anio_actual,anio_nacimiento):
    edad = anio_actual - anio_nacimiento
    print(f"Tu edad es: {edad}")

anio = int(input("Ingrese su año de nacimiento: "))
actual = int(input("Ingrese el año actual: "))
calcular_edad(actual,anio)

#funcion con retorno
def calcular_iva(precio, iva = 1.15):
    total = precio * iva
    return total

precio = float(input("Ingrese el precio del producto: "))
print(f"El precio total es: {calcular_iva(precio):.2f}")

#listas
def par_impar(num):
    if num%2==0:
        return (f"{num} es par")
    else:
        return (f"{num} es impar")

def par_impar_lista(lista):
    for num in lista:
        if num % 2 == 0:
            print(f"{num} es par")
        else:
            print(f"{num} es impar")
        

lista = [1, 5, 12, 29, 100, 1263786] 
for num in lista:
    print(par_impar(num), end=", ")

lista_num = range(0, 100, 2)
par_impar_lista(lista_num)

#diccionarios
def estudiantes(**lista_estudiantes):
    suma_edades=0 
    for nombre,edad in lista_estudiantes.items():
        print("el estudiante", nombre, "tienes",edad,"años")
        suma_edades+= edad
        print("La suma de todas las edades es:" ,suma_edades)
estudiantes(luis=15, anaya=19, miguel=20, dome=20, pepe=23, alan=18, jose=21)