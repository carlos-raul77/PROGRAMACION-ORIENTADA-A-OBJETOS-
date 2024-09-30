import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Función para añadir tarea
def añadir_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

# Función para marcar una tarea como completada
def marcar_completada():
    try:
        index = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(index)
        lista_tareas.delete(index)
        lista_tareas.insert(tk.END, f"{tarea} (Completada)")
    except:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcarla como completada.")

# Función para eliminar tarea
def eliminar_tarea():
    try:
        index = lista_tareas.curselection()[0]
        lista_tareas.delete(index)
    except:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminarla.")

# Campo de entrada para las tareas
entrada_tarea = tk.Entry(root, width=35)
entrada_tarea.pack(pady=10)

# Botón para añadir tarea
btn_añadir = tk.Button(root, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(root, width=40, height=10)
lista_tareas.pack(pady=10)

# Botones para marcar completada y eliminar tarea
btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Función para añadir tarea con la tecla "Enter"
root.bind('<Return>', lambda event: añadir_tarea())

# Ejecutar la aplicación
root.mainloop()