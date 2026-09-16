# Lección 05: Funciones

## 📖 ¿Qué es una Función?

Una función es un bloque de código reutilizable que realiza una tarea específica. Las funciones permiten:
- **Organizar** el código en partes lógicas
- **Reutilizar** código sin duplicarlo
- **Mantener** el código más fácilmente

## 🎯 Definición de Funciones

### Sintaxis básica
```python
def nombre_funcion():
    """Docstring - descripción de la función"""
    # Código de la función
    return resultado
```

### Ejemplo simple
```python
def saludar():
    """Imprime un saludo"""
    print("¡Hola! Bienvenido a Python")

# Llamar a la función
saludar()  # ¡Hola! Bienvenido a Python
```

## 📝 Parámetros y Argumentos

### Parámetros posicionales
```python
def saludar_persona(nombre):
    """Saluda a una persona por su nombre"""
    print(f"¡Hola {nombre}!")

saludar_persona("María")  # ¡Hola María!
saludar_persona("Juan")   # ¡Hola Juan!
```

### Múltiples parámetros
```python
def sumar(a, b):
    """Suma dos números"""
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

sumar(5, 3)  # 5 + 3 = 8
```

### Valor por defecto
```python
def saludar(nombre="Invitado"):
    """Saluda con nombre opcional"""
    print(f"¡Hola {nombre}!")

saludar()              # ¡Hola Invitado!
saludar("Ana")         # ¡Hola Ana!
```

### Parámetros nombrados (keyword arguments)
```python
def describir_mascota(nombre, especie="perro"):
    """Describe una mascota"""
    print(f"{nombre} es un {especie}")

describir_mascota("Firulais")                    # Firulais es un perro
describir_mascota(especie="gato", nombre="Michi")  # Michi es un gato
```

## 🔄 Retorno de Valores

### Return simple
```python
def cuadrado(numero):
    """Devuelve el cuadrado de un número"""
    return numero ** 2

resultado = cuadrado(5)
print(resultado)  # 25
```

### Múltiples retornos
```python
def operaciones(num1, num2):
    """Devuelve suma y resta"""
    suma = num1 + num2
    resta = num1 - num2
    return suma, resta

s, r = operaciones(10, 4)
print(f"Suma: {s}, Resta: {r}")  # Suma: 16, Resta: 6

# También se puede recibir como tupla
resultado = operaciones(10, 4)
print(resultado)  # (16, 6)
```

## 📚 Tipos de Funciones

### Funciones sin parámetros ni retorno
```python
def mostrar_menu():
    print("=== MENÚ ===")
    print("1. Opción 1")
    print("2. Opción 2")
```

### Funciones con parámetros pero sin retorno
```python
def imprimir_tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
```

### Funciones con parámetros y retorno
```python
def calcular_area(base, altura):
    return base * altura
```

### Funciones con parámetros variables (*args)
```python
def sumar_todos(*numeros):
    """Suma cualquier cantidad de números"""
    return sum(numeros)

print(sumar_todos(1, 2, 3))        # 6
print(sumar_todos(1, 2, 3, 4, 5))  # 15
```

### Funciones con parámetros nombrados variables (**kwargs)
```python
def mostrar_info(**datos):
    """Muestra información con nombres variables"""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")
```

## 🎯 Ámbito de Variables (Scope)

### Variable local
```python
def mi_funcion():
    variable_local = "Soy local"
    print(variable_local)

mi_funcion()
# print(variable_local)  # Error: no existe fuera de la función
```

### Variable global
```python
variable_global = "Soy global"

def mi_funcion():
    print(variable_global)  # Se puede acceder

mi_funcion()
print(variable_global)  # También fuera
```

### Modificar variable global
```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1
```

## 📝 Funciones Lambda

Funciones anónimas de una sola línea:

```python
# Forma tradicional
def cuadrado(x):
    return x ** 2

# Forma lambda
cuadrado = lambda x: x ** 2

print(cuadrado(5))  # 25
```

**Ejemplos:**
```python
suma = lambda a, b: a + b
mayor = lambda a, b: a if a > b else b

print(suma(3, 5))    # 8
print(mayor(3, 5))   # 5
```

## 🎯 Ejemplos Prácticos

### Ejemplo 1: Calculadora modular
```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    return None

# Uso
print(sumar(5, 3))      # 8
print(dividir(10, 2))   # 5.0
```

### Ejemplo 2: Validador de email
```python
def validar_email(email):
    """Verifica si un email tiene formato válido"""
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if len(email) < 5:
        return False
    return True

# Tests
print(validar_email("juan@email.com"))  # True
print(validar_email("invalido"))        # False
```

### Ejemplo 3: Formateador de texto
```python
def formatear_nombre(nombre, apellido, mayusculas=False):
    """Formatea nombre completo"""
    completo = f"{nombre} {apellido}"
    
    if mayusculas:
        return completo.upper()
    
    return completo.title()

print(formatear_nombre("juan", "pérez"))           # Juan Pérez
print(formatear_nombre("juan", "pérez", True))     # JUAN PÉREZ
```

## 📚 Ejercicios

### Ejercicio 5.1: Saludo personalizado
Crea una función `saludar(nombre)` que reciba un nombre e imprima "¡Hola [nombre]!".

**Archivo**: `ejercicios/ejercicio_05_01.py`

### Ejercicio 5.2: Máximo de tres números
Crea una función `maximo_tres(a, b, c)` que devuelva el mayor de tres números.

**Archivo**: `ejercicios/ejercicio_05_02.py`

### Ejercicio 5.3: Contar letras
Crea una función `contar_letras(palabra)` que devuelva la longitud de una palabra.

**Archivo**: `ejercicios/ejercicio_05_03.py`

### Ejercicio 5.4: Es palíndromo
Crea una función `es_palindromo(texto)` que verifique si un texto se lee igual al revés.

**Archivo**: `ejercicios/ejercicio_05_04.py`

### Ejercicio 5.5: Generador de contraseña
Crea una función `generar_password(longitud)` que genere una contraseña aleatoria.

**Archivo**: `ejercicios/ejercicio_05_05.py`

## ✅ Soluciones

Las soluciones están en la carpeta `soluciones/`.

## 🔍 Test de Autoevaluación

1. ¿Qué palabra clave se usa para definir una función?
2. ¿Qué hace `return` en una función?
3. ¿Cómo se define un parámetro con valor por defecto?
4. ¿Qué es `*args`?
5. ¿Qué es una función lambda?
6. ¿Qué diferencia hay entre variable local y global?

## ➡️ Siguiente Lección

Continúa con la [Lección 06: Listas y Tuplas](../leccion06-listas-tuplas/)
