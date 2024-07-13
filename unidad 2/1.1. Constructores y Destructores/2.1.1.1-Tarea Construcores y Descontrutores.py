#Tarea Constructores y Desconstrucores

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.prestado = False
        print(f"Se ha creado un nuevo libro: '{self.titulo}' de {self.autor}, publicado en {self.año_publicacion}.")

    def __del__(self):
        print(f"Se ha eliminado el libro: '{self.titulo}' de {self.autor}.")

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya se encuentra prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no se encuentra prestado.")

    def mostrar_info(self):
        estado = "prestado" if self.prestado else "disponible"
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nAño de publicación: {self.año_publicacion}\nEstado: {estado}")

# Crear objetos Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985)
libro3 = Libro("Crónica de una muerte anunciada", "Gabriel García Márquez", 1981)

# Prestar y devolver libros
libro1.prestar()
libro2.prestar()
libro1.devolver()
libro3.prestar()

# Mostrar información de los libros
libro1.mostrar_info()
libro2.mostrar_info()
libro3.mostrar_info()

# Eliminar los libros
del libro1
del libro2
del libro3