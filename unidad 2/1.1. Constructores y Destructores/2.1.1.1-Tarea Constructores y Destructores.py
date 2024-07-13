#Tarea constructores y Destructores

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una nueva persona: {self.nombre}, {self.edad} años.")

    def __del__(self):
        print(f"{self.nombre} ha sido eliminado.")

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear objetos Persona
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

# Llamar al método saludar
persona1.saludar()
persona2.saludar()

# El programa finaliza, activando los destructores