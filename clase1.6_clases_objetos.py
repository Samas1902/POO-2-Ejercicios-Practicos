#Creación de clases y objetos
class Libro:
    pass

libro1 = Libro()
print(type(libro1)) # <class '__main__.Libro'>

class Libro:
    def __init__(self, nombre, autor, estado, lista_libros): #constructor
        self.nombre = nombre
        self.autor = autor
        self.estado = estado
        self.lista_libros = lista_libros

    def mostrar(self): #mostrar
        print(f'Nombre: {self.nombre}, Estado: {self.estado}') 

    def cambiar_estado(self, nuevo_estado): #cambiar estado
        self.estado = nuevo_estado 

    def mostrar_lista_libros(self): #mostrar lista de libros
        for libro in self.lista_libros:
            print(libro)

    def __str__(self): #toString
        return f'Nombre: {self.nombre}, Autor: {self.autor}, Estado: {self.estado}, Lista de libros: {self.lista_libros}'
    
libro2 = Libro("El Quijote", "Miguel de Cervantes", "Disponible", ["El Quijote", "Cien años de soledad", "La casa de los espíritus"])
libro2.mostrar()
libro2.cambiar_estado("Prestado")
libro2.mostrar_lista_libros()
print(libro2.__str__) #muestra la referencia de memoria del tostring
print(libro2) #muestra el tostring del libro
libro2.estado = "Roto" #cambiar el estado directamente
print(libro2) #muestra el tostring del libro
