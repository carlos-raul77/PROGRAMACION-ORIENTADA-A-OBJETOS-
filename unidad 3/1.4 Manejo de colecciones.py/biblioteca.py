# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla (inmutable)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo_autor[0]}, Autor: {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para los libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario ISBN -> Libro
        self.usuarios = {}  # Diccionario ID -> Usuario
        self.ids_usuarios = set()  # Conjunto de IDs únicos

    # Añadir libro
    def anadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")

    # Dar de baja a usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print(f"No se encontró al usuario con ID {id_usuario}.")

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")
            else:
                print(f"El usuario ya tiene prestado este libro.")
        else:
            print("Usuario o libro no encontrado.")

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.get(isbn)
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo_autor[0]}' devuelto.")
            else:
                print(f"El usuario no tiene prestado este libro.")
        else:
            print("Usuario no encontrado.")

    # Buscar libros
    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and titulo in libro.titulo_autor[0]) or \
               (autor and autor in libro.titulo_autor[1]) or \
               (categoria and categoria == libro.categoria):
                resultados.append(libro)
        return resultados

    # Listar libros prestados por un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados por {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f" - {libro.titulo_autor[0]} por {libro.titulo_autor[1]}")
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

# Prueba del sistema
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "12345")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", "67890")

usuario1 = Usuario("Juan Pérez", "U001")

biblioteca = Biblioteca()
biblioteca.anadir_libro(libro1)
biblioteca.anadir_libro(libro2)

biblioteca.registrar_usuario(usuario1)

biblioteca.prestar_libro("U001", "12345")
biblioteca.listar_libros_prestados("U001")

biblioteca.devolver_libro("U001", "12345")
biblioteca.listar_libros_prestados("U001")