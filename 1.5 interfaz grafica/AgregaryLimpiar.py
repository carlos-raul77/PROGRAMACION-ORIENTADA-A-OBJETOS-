import tkinter as tk
from tkinter import messagebox

# Función para agregar elementos a la lista
def agregar_elemento():
    elemento = entrada_texto.get()
    if elemento:
        lista_datos.insert(tk.END, elemento)
        entrada_texto.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI con Tkinter")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=10)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=5)

# Botón para agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack(pady=5)

# Botón para limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()