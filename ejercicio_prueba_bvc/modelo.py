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


class ListaMedicamentos:
    def __init__(self):
        self.listaMedicamentos = []
        self.cargar_datos()

    def cargar_datos(self):
        datos = [
            Medicamento(1, "Paracetamol", 2.50, 30),
            Medicamento(2, "Ibuprofeno", 3.20, 20)
        ]
        for m in datos:
            self.listaMedicamentos.append(m)

    def registrar_medicamento(self, nombre, precio, cajas):
        codigo = len(self.listaMedicamentos) + 1
        self.listaMedicamentos.append(Medicamento(codigo, nombre, precio, cajas))
        return codigo

    def buscar_medicamento(self, codigo):
        for med in self.listaMedicamentos:
            if med.codigo == codigo:
                return med
        return None

    def mostrar_medicamentos(self):
        return self.listaMedicamentos