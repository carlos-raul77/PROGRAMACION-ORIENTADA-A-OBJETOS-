def ejecutar_sistema():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad: "))
            precio = float(input("Introduce el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            if inventario.añadir_producto(producto):
                print("Producto añadido con éxito.")
            else:
                print("No se pudo añadir el producto.")

        elif opcion == "2":
            id_producto = input("Introduce el ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_producto):
                print("Producto eliminado con éxito.")
            else:
                print("No se pudo eliminar el producto.")

        elif opcion == "3":
            id_producto = input("Introduce el ID del producto a actualizar: ")
            cantidad = input("Introduce la nueva cantidad (deja en blanco si no quieres cambiarla): ")
            precio = input("Introduce el nuevo precio (deja en blanco si no quieres cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            if inventario.actualizar_producto(id_producto, cantidad, precio):
                print("Producto actualizado con éxito.")
            else:
                print("No se pudo actualizar el producto.")

        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                print("Productos encontrados:")
                for prod in resultados:
                    print(prod)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_sistema()