registros = ["  DEP;150.50 ", "RET;40.00", " DEP;300.00", "RET;120.25  "]
depositos = [float(r.strip().split(";")[1]) for r in registros if r.strip().startswith("DEP")]
print(f"Total depositado: ${sum(depositos):,.2f}")
print(f"Depósito más alto: ${max(depositos):,.2f}")

def validar_nota(nota):
    if not isinstance(nota, (int, float)) or isinstance(nota, bool):
        raise TypeError("La nota debe ser un número (int o float).")
    if nota < 0 or nota > 10:
        raise ValueError("La nota debe estar entre 0 y 10.")
    return True


def pedir_nota():
    while True:
        try:
            nota = float(input("Ingrese la nota (0 a 10): "))
            validar_nota(nota)
            return nota
        except ValueError as e:
            print(f"Error: {e}")

socios = [
    {"cedula": "0102030405", "nombre": "Ana", "saldo": 500.0},
    {"cedula": "0912345678", "nombre": "Luis", "saldo": 120.5},
]

def guardar(socios):
    with open("socios.txt", "w", encoding="utf-8") as archivo:
        for s in socios:
            archivo.write(f"{s['cedula']};{s['nombre']};{s['saldo']}\n")


def cargar():
    socios = []
    try:
        with open("socios.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip():
                    cedula, nombre, saldo = linea.strip().split(";")
                    socios.append({
                        "cedula": cedula,
                        "nombre": nombre,
                        "saldo": float(saldo)
                    })
    except FileNotFoundError:
        return []
    return socios

class Credito:
    def __init__(self, socio, monto):
        self.socio = socio
        self.monto = monto
        self.pagado = 0.0

    def abonar(self, valor):
        if valor > 0 and self.pagado + valor <= self.monto:
            self.pagado += valor
        else:
            print("Abono inválido")

    def saldo_pendiente(self):
        return self.monto - self.pagado

    def __str__(self):
        return f"Socio: {self.socio} | Pendiente: ${self.saldo_pendiente():,.2f}"


# Prueba
credito = Credito("Ana", 500.0)
credito.abonar(150.0)
credito.abonar(400.0)  # Imprime "Abono inválido" porque 150 + 400 > 500
print(credito)         # Imprime: Socio: Ana | Pendiente: $350.00

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 7


estudiantes = [
    Estudiante("Ana", 9.5),
    Estudiante("Luis", 6.0),
    Estudiante("Sofía", 7.0),
    Estudiante("Carlos", 4.5),
]

for e in estudiantes:
    if e.aprobo():
        print(f"{e.nombre} aprobó con {e.nota}")

# En una sola línea:
aprobados = sum(1 for e in estudiantes if e.aprobo())
promedio = sum(e.nota for e in estudiantes) / len(estudiantes)

print(f"Total aprobados: {aprobados} | Promedio del curso: {promedio:.2f}")