# Lección 14: Funciones Avanzadas

## 📖 Introducción

Esta lección explora características avanzadas de funciones en Python:

- **Funciones lambda**
- **Funciones de orden superior**
- **Decoradores**
- **Funciones map, filter, reduce**
- **Closures**
- **Recursividad avanzada**

## 🎯 Funciones Lambda

Funciones anónimas pequeñas definidas con la palabra clave `lambda`.

### Sintaxis
```python
# Función normal
def sumar(a, b):
    return a + b

# Equivalente con lambda
sumar = lambda a, b: a + b

print(sumar(5, 3))  # 8
```

### Ejemplos comunes
```python
# Cuadrado de un número
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25

# Verificar si es par
es_par = lambda x: x % 2 == 0
print(es_par(4))  # True

# Concatenar strings
unir = lambda a, b: f"{a} - {b}"
print(unir("Hola", "Mundo"))  # Hola - Mundo
```

### Uso con sorted()
```python
personas = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 35}
]

# Ordenar por edad
ordenados = sorted(personas, key=lambda p: p['edad'])
print(ordenados)

# Ordenar por nombre (inverso)
ordenados_nombre = sorted(personas, key=lambda p: p['nombre'], reverse=True)
```

## 📚 Funciones de Orden Superior

Funciones que reciben otras funciones como argumentos o retornan funciones.

### Ejemplo básico
```python
def aplicar_operacion(numeros, operacion):
    """Aplica una operación a cada número"""
    return [operacion(n) for n in numeros]

numeros = [1, 2, 3, 4, 5]

resultado_cuadrado = aplicar_operacion(numeros, lambda x: x ** 2)
print(resultado_cuadrado)  # [1, 4, 9, 16, 25]

resultado_doble = aplicar_operacion(numeros, lambda x: x * 2)
print(resultado_doble)  # [2, 4, 6, 8, 10]
```

### Función que retorna función
```python
def crear_multiplicador(factor):
    """Crea una función multiplicadora"""
    def multiplicar(numero):
        return numero * factor
    return multiplicar

doble = crear_multiplicador(2)
triple = crear_multiplicador(3)

print(doble(5))   # 10
print(triple(5))  # 15
print(doble(7))   # 14
```

## 🔄 Decoradores

Los decoradores permiten modificar el comportamiento de funciones sin cambiar su código.

### Decorador básico
```python
def mi_decorador(funcion_original):
    def wrapper():
        print("Antes de ejecutar la función")
        funcion_original()
        print("Después de ejecutar la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()
# Salida:
# Antes de ejecutar la función
# ¡Hola!
# Después de ejecutar la función
```

### Decorador con argumentos
```python
def decorador_con_args(func):
    def wrapper(*args, **kwargs):
        print(f"Argumentos: args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@decorador_con_args
def sumar(a, b):
    return a + b

sumar(5, 3)
```

### Decorador para medir tiempo
```python
import time
from functools import wraps

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def funcion_lenta():
    time.sleep(2)
    return "Completado"

funcion_lenta()
```

### Múltiples decoradores
```python
def decorador1(func):
    def wrapper(*args, **kwargs):
        print("Decorador 1 - antes")
        resultado = func(*args, **kwargs)
        print("Decorador 1 - después")
        return resultado
    return wrapper

def decorador2(func):
    def wrapper(*args, **kwargs):
        print("Decorador 2 - antes")
        resultado = func(*args, **kwargs)
        print("Decorador 2 - después")
        return resultado
    return wrapper

@decorador1
@decorador2
def mi_funcion():
    print("Ejecutando función")

mi_funcion()
# Salida:
# Decorador 1 - antes
# Decorador 2 - antes
# Ejecutando función
# Decorador 2 - después
# Decorador 1 - después
```

## ⚡ Funciones map, filter, reduce

### map() - Transformar elementos
```python
numeros = [1, 2, 3, 4, 5]

# Elevar al cuadrado
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

# Convertir a string
strings = list(map(str, numeros))
print(strings)  # ['1', '2', '3', '4', '5']

# Con múltiples iterables
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
suma = list(map(lambda x, y: x + y, lista1, lista2))
print(suma)  # [5, 7, 9]
```

### filter() - Filtrar elementos
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solo pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Solo mayores a 5
mayores = list(filter(lambda x: x > 5, numeros))
print(mayores)  # [6, 7, 8, 9, 10]

# Combinar con map
pares_al_cubo = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, numeros)))
print(pares_al_cubo)  # [8, 64, 216, 512, 1000]
```

### reduce() - Reducir a un valor
```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]

# Suma acumulada
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # 15

# Producto acumulado
producto = reduce(lambda x, y: x * y, numeros)
print(producto)  # 120

# Máximo valor
maximo = reduce(lambda x, y: x if x > y else y, numeros)
print(maximo)  # 5

# Con valor inicial
suma_con_inicial = reduce(lambda x, y: x + y, numeros, 100)
print(suma_con_inicial)  # 115
```

## 📦 Closures (Cierres Léxicos)

Una closure es una función que "recuerda" el ámbito donde fue creada.

### Ejemplo básico
```python
def crear_contador():
    cuenta = 0
    
    def contador():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    
    return contador

contador1 = crear_contador()
print(contador1())  # 1
print(contador1())  # 2
print(contador1())  # 3

contador2 = crear_contador()
print(contador2())  # 1 (independiente)
```

### Closure con configuración
```python
def crear_potencia(exponente):
    def elevar(base):
        return base ** exponente
    return elevar

cuadrado = crear_potencia(2)
cubo = crear_potencia(3)

print(cuadrado(5))  # 25
print(cubo(5))      # 125
```

## 🔄 Recursividad Avanzada

### Factorial recursivo
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Fibonacci con memoización
```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

print(fibonacci_memo(50))  # Rápido gracias a memoización
```

### Recursividad de cola (Tail Recursion)
```python
def factorial_tail(n, acumulador=1):
    if n == 0:
        return acumulador
    return factorial_tail(n - 1, n * acumulador)

print(factorial_tail(5))  # 120
```

## 🎯 Ejemplos Prácticos

### Ejemplo 1: Pipeline de procesamiento de datos
```python
from functools import reduce

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pipeline: filtrar pares -> cuadrado -> sumar
resultado = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, datos)
    )
)
print(resultado)  # 220
```

### Ejemplo 2: Sistema de autenticación con decoradores
```python
from functools import wraps

def requerir_auth(func):
    @wraps(func)
    def wrapper(usuario, *args, **kwargs):
        if not usuario.get('autenticado'):
            raise PermissionError("Usuario no autenticado")
        return func(usuario, *args, **kwargs)
    return wrapper

def requerir_admin(func):
    @wraps(func)
    def wrapper(usuario, *args, **kwargs):
        if not usuario.get('es_admin'):
            raise PermissionError("Se requieren privilegios de admin")
        return func(usuario, *args, **kwargs)
    return wrapper

@requerir_auth
@requerir_admin
def eliminar_usuario(usuario, id_usuario):
    return f"Usuario {id_usuario} eliminado"

admin = {'autenticado': True, 'es_admin': True}
print(eliminar_usuario(admin, 123))
```

### Ejemplo 3: Cache automático con decorador
```python
from functools import wraps

def cache(func):
    memoria = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in memoria:
            print(f"Cache hit para {args}")
            return memoria[args]
        
        print(f"Calculando para {args}")
        resultado = func(*args)
        memoria[args] = resultado
        return resultado
    
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Calcula
print(fibonacci(10))  # Usa cache
```

## 📝 Ejercicios

### Ejercicio 14.1: Lambda y sorting
Ordena una lista de tuplas (nombre, edad, ciudad) primero por ciudad y luego por edad usando lambda.

### Ejercicio 14.2: Decorador de reintentos
Crea un decorador `@reintentar(veces=3)` que reintente ejecutar una función si falla.

### Ejercicio 14.3: Pipeline funcional
Crea un pipeline que procese textos: convertir a minúsculas → dividir en palabras → filtrar palabras cortas (< 4 letras) → contar frecuencia.

### Ejercicio 14.4: Closure contador múltiple
Crea una función que retorne tres closures: uno que cuente incrementos, otro decrementos, y otro que retorne el total actual.

### Ejercicio 14.5: Recursividad - Torres de Hanoi
Implementa la solución recursiva para el problema de las Torres de Hanoi.

## ✅ Soluciones

Las soluciones están en la carpeta `soluciones/solucion_14_*.py`.

## 🔍 Test de Autoevaluación

1. ¿Qué es una función lambda y cuándo es útil?
2. Explica qué hace un decorador.
3. ¿Cuál es la diferencia entre map() y filter()?
4. ¿Qué es una closure y qué problema resuelve?
5. ¿Qué es la memoización y por qué es importante en recursividad?

## ➡️ Siguiente Lección

Continúa con la [Lección 15: Módulos Estándar Útiles](../leccion15-modulos-estandar/)
