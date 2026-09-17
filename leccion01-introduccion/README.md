# Lección 01: Introducción a Python

## 📖 ¿Qué es Python?

Python es un lenguaje de programación interpretado, de alto nivel y de propósito general. Es conocido por:

- **Sintaxis clara y legible**: Parece pseudocódigo
- **Multiparadigma**: Soporta programación orientada a objetos, funcional y procedural
- **Gran comunidad**: Miles de librerías disponibles
- **Versatilidad**: Web, ciencia de datos, IA, automatización, etc.

## 🚀 Instalación

### Windows
1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Ejecuta el instalador
3. ✅ Marca "Add Python to PATH"
4. Haz clic en "Install Now"

### macOS
```bash
brew install python3
```

### Linux
```bash
sudo apt-get install python3 python3-pip
```

### Verificar instalación
```bash
python --version
# o
python3 --version
```

## 💻 Tu Primer Programa

Crea un archivo llamado `hola_mundo.py`:

```python
print("¡Hola, Mundo!")
```

Ejecútalo:
```bash
python hola_mundo.py
```

## 📝 Conceptos Básicos

### Comentarios
```python
# Esto es un comentario de una línea

"""
Esto es un comentario
de múltiples líneas
"""
```

### Función print()
Muestra información en pantalla:
```python
print("Hola")
print("Python", "es", "genial")  # Separa con espacios por defecto
print("Línea 1\nLínea 2")  # \n crea nueva línea
```

### Función input()
Recibe datos del usuario:
```python
nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre}!")
```

## 🎯 Ejemplos Prácticos

### Ejemplo 1: Saludo personalizado
```python
# saludo.py
nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")

print(f"Hola {nombre}, tienes {edad} años.")
print("¡Bienvenido al curso de Python!")
```

### Ejemplo 2: Calculadora simple
```python
# calculadora.py
numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
```

## 📚 Ejercicios

### Ejercicio 1.1: Presentación
Crea un programa que:
1. Pida tu nombre
2. Pida tu ciudad
3. Pida tu hobby favorito
4. Muestre: "Hola, soy [nombre], vivo en [ciudad] y me gusta [hobby]"

**Archivo**: `ejercicios/ejercicio_01_01.py`

### Ejercicio 1.2: Conversor de edad
Crea un programa que:
1. Pida tu año de nacimiento
2. Calcule tu edad aproximada
3. Muestre: "Tienes aproximadamente X años"

**Archivo**: `ejercicios/ejercicio_01_02.py`

### Ejercicio 1.3: Mensaje creativo
Crea un programa que muestre un mensaje con formato especial usando saltos de línea y tabulaciones.

**Archivo**: `ejercicios/ejercicio_01_03.py`

## ✅ Soluciones

Las soluciones están en la carpeta `soluciones/` para que verifiques tus respuestas después de intentar los ejercicios.

## 🔍 Test de Autoevaluación

Responde sin mirar el código:

1. ¿Qué función se usa para mostrar texto en pantalla?
2. ¿Qué función se usa para recibir entrada del usuario?
3. ¿Cómo se escribe un comentario de una línea en Python?
4. ¿Qué comando se usa para ejecutar un archivo Python?

## ➡️ Siguiente Lección

Continúa con la [Lección 02: Variables y Tipos de Datos](../leccion02-variables-tipos/)
