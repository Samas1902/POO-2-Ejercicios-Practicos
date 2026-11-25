class ControladorMedicamentos:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion = self.vista.menu_farmacia()

            if opcion == "1":
                nombre, precio, cajas = self.vista.pedir_datos_medicamento()
                self.modelo.registrar_medicamento(nombre, precio, cajas)
                self.vista.mostrar_mensaje("El medicamento ha sido registrado")

            elif opcion == "2":
                medicamentos = self.modelo.obtener_medicamentos()
                self.vista.mostrar_medicamentos(medicamentos)

            elif opcion == "3":
                codigo = self.vista.pedir_codigo_medicamento()
                cantidad = self.vista.pedir_cantidad()
                resultado = self.modelo.vender_medicamento(codigo, cantidad)
                self.vista.mostrar_mensaje(resultado)

            elif opcion == "4":
                self.vista.mostrar_mensaje("Saliendo del programa...")
                break

            else:
                self.vista.mostrar_mensaje("ERROR: Opción inválida. Por favor, seleccione una opción válida.")