from modelo import *
from vista import *
from controlador import *

modelo = ListaMedicamentos()
vista = VistaFarmacia()
controlador = ControladorMedicamentos(modelo, vista)
controlador.ejecutar()