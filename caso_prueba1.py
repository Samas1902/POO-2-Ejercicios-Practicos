class Medicamento:
    def __init__(self, codigo, nombre, precio, cajas):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cajas = cajas

    def vender(self, cantidad):
        if cantidad <= 0:
            print("ERROR: la cantidad debe ser mayor que cero.")
            return False
        if cantidad > self.cajas:
            print(f"ERROR: solo hay {self.cajas} cajas.")
            return False
        self.cajas -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8} {self.nombre:<18} ${self.precio:<9.2f} {self.cajas}"

medicamentos = [
    Medicamento(1, "Paracetamol", 2.50, 30),
    Medicamento(2, "Ibuprofeno", 3.20, 20)
]

while True:
    print("\n--- FARMACIA SAN JOSÉ ---")
    print("1. Registrar medicamento")
    print("2. Mostrar medicamentos")
    print("3. Vender medicamento")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        nombre = input("Nombre del medicamento: ")
        precio = float(input("Precio: "))
        cajas = int(input("Cajas disponibles: "))
        nuevo_codigo = len(medicamentos) + 1
        nuevo_med = Medicamento(nuevo_codigo, nombre, precio, cajas)
        medicamentos.append(nuevo_med)
        print(f"Registrado con el código {nuevo_codigo}.")

    elif opcion == "2":
        print(f"\n{'Código':<8} {'Nombre':<18} {'Precio':<10} {'Cajas'}")
        print("--------------------------------------------------------")
        for med in medicamentos:
            print(med)

    elif opcion == "3":
        codigo_buscar = int(input("Ingrese el código del medicamento: "))
        encontrado = None
        for med in medicamentos:
            if med.codigo == codigo_buscar:
                encontrado = med
                break

        if encontrado is None:
            print("ERROR: no existe ese código.")
        else:
            cantidad = int(input("Cantidad de cajas a vender: "))
            if encontrado.vender(cantidad):
                print(f"Listo. Quedan {encontrado.cajas} cajas.")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida elija entre 1 y 4")