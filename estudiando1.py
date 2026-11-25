from datetime import date

ARCHIVO_MOVIMIENTOS = "movimientos.txt"

class Cuenta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto_valido:
            self.saldo += monto
            registrar_movimiento("DEPOSITO", monto, self.saldo)
            return True
        else:
            return False 

    def retirar(self, monto):
        if monto_valido:
            self.saldo -= monto
            registrar_movimiento("RETIRO", monto, self.saldo)
            return True
        return False
        

def monto_valido(monto):
    return monto > 0    

def registrar_movimiento(tipo, monto, saldo_actual):
    with open(ARCHIVO_MOVIMIENTOS, "w", encoding="utf-8") as archivo:
        archivo.write(f"{date.today},{tipo},{monto:.2f},{saldo_actual:.2f}")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("ERROR, ingres un numero entero porfavor")

def leer_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("ERROR, ingrese un numero decimal porfavor")

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("ERROR, no puedes dejar vacio")
        elif "," in texto:
            print("ERROR, no se puede poner comas")
        else:
            return texto

def main():
    cuenta1 = Cuenta("Samuel", 50)

    while True:
        print("\n1. Consultar Saldo | 2. Depositar monto | 3. Retirar monto | 4. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            print(f"Titular: {cuenta1.titular} | Saldo: {cuenta1.saldo}")
        elif opcion == "2":
            monto = leer_float("Ingrese el monto a depositar: ")
            cuenta1.depositar(monto)
            if cuenta1.depositar(monto):
                print("EXITO")
            else:
                print("ERROR, el monto debe ser mayor a 0")
        elif opcion == "3":
            monto = leer_float("Ingrese el monto a depositar: ")
            cuenta1.retirar(monto)
            if cuenta1.retirar(monto):
                print("EXITO")
            else:
                print("ERROR, el monto debe ser mayor a 0")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida, elija de 1 a 4")

main()
