# Lección 02: Variables y Tipos de Datos

## 📖 ¿Qué es una Variable?

Una variable es como una "caja" donde guardamos información que podemos usar después. En Python:

- No necesitas declarar el tipo explícitamente
- El nombre debe ser descriptivo
- Es sensible a mayúsculas (`nombre` ≠ `Nombre`)

## 🎯 Reglas para Nombres de Variables

✅ **Válidos:**
```python
nombre = "Juan"
edad = 25
mi_variable = "valor"
_nombre = "privado"
EDAD = 30  # Constante (por convención)
```

❌ **Inválidos:**
```python
1nombre = "Juan"      # No puede empezar con número
mi-variable = "valor" # No puede tener guiones
class = "Python"      # No puede usar palabras reservadas
```

## 📊 Tipos de Datos Principales

### 1. Números Enteros (`int`)
Números sin decimales:
```python
edad = 25
cantidad = -10
año = 2024
```

### 2. Números Decimales (`float`)
Números con punto decimal:
```python
precio = 19.99
pi = 3.1416
temperatura = -5.5
```

### 3. Cadenas de Texto (`str`)
Texto entre comillas:
```python
nombre = "María"
mensaje = 'Hola Mundo'
descripcion = """Texto 
multilinea"""
```

### 4. Booleanos (`bool`)
Valores de verdad:
```python
es_mayor = True
tiene_acceso = False
```

## 🔍 Verificar Tipos

```python
tipo = type(variable)  # Devuelve el tipo
es_instancia = isinstance(variable, int)  # Verifica si es de un tipo
```

**Ejemplo:**
```python
edad = 25
print(type(edad))  # <class 'int'>

precio = 19.99
print(type(precio))  # <class 'float'>

nombre = "Ana"
print(type(nombre))  # <class 'str'>

activo = True
print(type(activo))  # <class 'bool'>
```

## 🔄 Conversión de Tipos (Casting)

```python
# De string a número
edad_str = "25"
edad_int = int(edad_str)  # 25

precio_str = "19.99"
precio_float = float(precio_str)  # 19.99

# De número a string
cantidad = 100
cantidad_str = str(cantidad)  # "100"

# A booleano
bool_cero = bool(0)        # False
bool_numero = bool(5)      # True
bool_texto = bool("Hola")  # True
bool_vacio = bool("")      # False
```

## 📝 Operaciones con Strings

```python
nombre = "Juan"
apellido = "Pérez"

# Concatenación
nombre_completo = nombre + " " + apellido  # "Juan Pérez"

# Repetición
saludo = "Hola! " * 3  # "Hola! Hola! Hola! "

# Longitud
longitud = len(nombre)  # 4

# Mayúsculas/Minúsculas
mayus = nombre.upper()    # "JUAN"
minus = apellido.lower()  # "pérez"

# Reemplazar
texto = "Hola Mundo"
nuevo = texto.replace("Mundo", "Python")  # "Hola Python"
```

## 🎯 Ejemplos Prácticos

### Ejemplo 1: Ficha de personaje
```python
# Personaje de videojuego
nombre = "Aragorn"
clase = "Guerrero"
nivel = 45
vida = 850.5
es_heroe = True

print(f"Nombre: {nombre}")
print(f"Clase: {clase}")
print(f"Nivel: {nivel}")
print(f"Vida: {vida}")
print(f"¿Es héroe?: {es_heroe}")
```

### Ejemplo 2: Calculadora de IVA
```python
# Calculadora de IVA
precio_sin_iva = 100
iva = 0.21  # 21%

precio_con_iva = precio_sin_iva * (1 + iva)

print(f"Precio sin IVA: ${precio_sin_iva}")
print(f"IVA ({iva*100}%): ${precio_sin_iva * iva}")
print(f"Precio total: ${precio_con_iva}")
```

### Ejemplo 3: Formulario de registro
```python
# Registro de usuario
usuario = input("Nombre de usuario: ")
email = input("Email: ")
edad = int(input("Edad: "))

print("\n=== Registro Exitoso ===")
print(f"Usuario: {usuario}")
print(f"Email: {email}")
print(f"Edad: {edad}")
print(f"Próximo año tendrás: {edad + 1} años")
```

## 📚 Ejercicios

### Ejercicio 2.1: Calculadora de área
Crea un programa que calcule el área de un rectángulo:
1. Pide la base (float)
2. Pide la altura (float)
3. Calcula: área = base × altura
4. Muestra el resultado

**Archivo**: `ejercicios/ejercicio_02_01.py`

### Ejercicio 2.2: Conversor de temperaturas
Crea un programa que convierta Celsius a Fahrenheit:
- Fórmula: F = (C × 9/5) + 32

**Archivo**: `ejercicios/ejercicio_02_02.py`

### Ejercicio 2.3: Información personal
Crea variables para almacenar:
- Tu nombre completo
- Tu edad
- Tu altura en metros
- Si eres estudiante (True/False)

Muestra toda la información en un formato bonito.

**Archivo**: `ejercicios/ejercicio_02_03.py`

### Ejercicio 2.4: Operaciones con strings
Dada la cadena `"Python es increíble"`:
1. Conviértela a mayúsculas
2. Conviértela a minúsculas
3. Cuenta cuántas veces aparece la letra 'e'
4. Reemplaza "increíble" por "fantástico"

**Archivo**: `ejercicios/ejercicio_02_04.py`

## ✅ Soluciones

Las soluciones están en la carpeta `soluciones/`.

## 🔍 Test de Autoevaluación

1. ¿Qué tipo de dato es `42`?
2. ¿Qué tipo de dato es `"42"`?
3. ¿Cómo conviertes el string `"100"` a entero?
4. ¿Qué función devuelve la longitud de un string?
5. ¿Es válido `mi-variable = 5` en Python?

## ➡️ Siguiente Lección

Continúa con la [Lección 03: Operadores](../leccion03-operadores/)
