edades = [18, 22, 25, 30, 35, 40, 45, 50, 55, 60]
edades.append(65)  # agregar un elemento al final de la lista
edades.insert(1, 15)  # insertar un elemento en la posición 1
print(edades)  # imprimir la lista completa
print(len(edades))  # imprimir la cantidad de elementos en la lista
print(edades[4])  # imprimir el elemento en la posición 4
print(sum(edades))  # imprimir la suma de todos los elementos de la lista
print(max(edades))  # imprimir el valor máximo de la lista
print(min(edades))  # imprimir el valor mínimo de la lista
print(sorted(edades))  # imprimir la lista ordenada de menor a mayor
ordenado = sorted(edades)  # ordenar la lista
print(ordenado[4])  # imprimir la lista ordenada de mayor a menor

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print(meses)  # imprimir la tupla completa

estudiante = {
    "correo": "juan.perez@example.com",
    "nombre": "Juan Pérez",
    "cedula": "1234567890",
    "celular": "0987654321",
    "notas" : [8.5, 8, 9, 10]
}
print(estudiante.get("nombre"))  # imprimir el valor asociado a la clave "nombre"
print(estudiante.keys())  # imprimir todas las claves del diccionario

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}
print(conjunto_a.union(conjunto_b))  # imprimir la unión de los conjuntos
print(conjunto_a.intersection(conjunto_b))  # imprimir la intersección de los conjuntos

socio = {
    "cedula": "0102030405",                 # str: puede empezar con 0
    "nombre": "  ana lucía pérez ",          # str con espacios y minúsculas
    "edad": 34,                              # int
    "activo": True,                          # bool
    "garante": None,                         # None: todavía no tiene
    "cuentas": [                             # list de dict
        {"numero": "AH-001", "tipo": "ahorros", "saldo": 1520.75},
        {"numero": "PF-010", "tipo": "plazo fijo", "saldo": 5000.0},
        {"numero": "AH-002", "tipo": "ahorros", "saldo": 80.5},
    ],
}

print(socio["nombre"].strip())  # imprimir el nombre con espacios eliminados