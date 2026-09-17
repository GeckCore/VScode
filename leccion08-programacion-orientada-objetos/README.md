# Lección 08: Programación Orientada a Objetos (POO)

## 📖 Clases y Objetos

La POO organiza el código en objetos que combinan datos y comportamiento.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"

# Crear objeto
juan = Persona("Juan", 30)
print(juan.saludar())  # "Hola, soy Juan"
```

## 🎯 Conceptos Clave

- **Clase**: Molde para crear objetos
- **Objeto**: Instancia de una clase
- **Atributos**: Datos del objeto
- **Métodos**: Funciones del objeto
- **Herencia**: Reutilizar código de clases padre

## ➡️ Siguiente Lección

[Lección 09: Manejo de Archivos](../leccion09-manejo-archivos/)
