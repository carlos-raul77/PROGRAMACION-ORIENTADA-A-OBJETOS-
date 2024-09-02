import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El ID ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, archivo):
        try:
            with open(archivo, 'w') as file:
                productos_serializados = {id_producto: vars(producto) for id_producto, producto in self.productos.items()}
                json.dump(productos_serializados, file)
            print("Inventario guardado exitosamente en el archivo.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as file:
                productos_serializados = json.load(file)
                self.productos = {id_producto: Producto(**datos) for id_producto, datos in productos_serializados.items()}
            print("Inventario cargado exitosamente desde el archivo.")
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")