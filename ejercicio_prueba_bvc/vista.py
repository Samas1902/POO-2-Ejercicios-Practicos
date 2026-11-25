class VistaFarmacia:
    def menu_farmacia(self):
        print("\n--- FARMACIA SAN JOSÉ ---")
        print("1. Registrar medicamento")
        print("2. Mostrar medicamentos")
        print("3. Vender medicamento")
        print("4. Salir")

        opc = input("Seleccione una opción (1-4): ")
        return opc

    def pedir_datos_medicamento(self):
        nombre = input("Ingrese el nombre del medicamento: ")
        precio = float(input("Ingrese el precio del medicamento: "))
        cajas = int(input("Ingrese el numero de cajas disponibles: "))
        return nombre, precio, cajas

    def mostrar_medicamentos(self, medicamentos):
        print(f"\n{'Código':<8} {'Nombre':<18} {'Precio':<10} {'Cajas'}")
        print("--------------------------------------------------------")
        for med in medicamentos:
            print(med)

    def pedir_codigo_medicamento(self):
        return int(input("Ingrese el código del medicamento: "))

    def pedir_cantidad(self):
        return int(input("Cantidad de cajas a vender: "))

    def mostrar_mensaje(self, mensaje):
        print(mensaje)