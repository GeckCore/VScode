# Lección 14 · Funciones avanzadas

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion14-funciones-avanzadas/practica.ipynb)

## 🎯 Objetivos

- Usar funciones como datos: lambdas, `map`, `filter`
- Entender iteradores y crear generadores con `yield`
- Escribir decoradores
- Comprender closures

Estos conceptos separan a quien «escribe Python» de quien **piensa en Python**. Son material de 2º de carrera y de entrevistas técnicas.

---

## 1. Las funciones son objetos

En Python, una función es un valor como cualquier otro: se puede guardar en variables, pasar como argumento y devolver de otra función.

```python
def saludar(nombre):
    return f"Hola {nombre}"

f = saludar          # guardar la función (sin paréntesis: no la ejecuta)
print(f("Ana"))      # Hola Ana

def aplicar(funcion, valor):   # pasar función como argumento
    return funcion(valor)

print(aplicar(len, "Python"))   # 6
```

Ya lo usaste: `sorted(lista, key=lambda x: x[1])` pasa una función a otra.

## 2. Lambdas: funciones anónimas de una línea

```python
doble = lambda x: x * 2
cuadrado = lambda x: x ** 2

print(doble(5))        # 10
```

Sintaxis: `lambda parámetros: expresión`. Sin nombre, sin `return` (devuelve la expresión). Regla de estilo: úsalas solo para cosas cortas y de usar y tirar (típicamente como `key=`); si tiene lógica, escribe un `def` con nombre.

## 3. `map` y `filter`

```python
nums = [1, 2, 3, 4, 5]

list(map(lambda x: x * 2, nums))        # [2, 4, 6, 8, 10]  (transforma)
list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]            (filtra)
```

Devuelven **iteradores** (por eso el `list(...)`). En la práctica moderna las comprensiones suelen ser más legibles (`[x*2 for x in nums]`), pero `map`/`filter` aparecen mucho en código real y en exámenes.

## 4. Iteradores y generadores

Un **iterador** es un objeto que produce elementos **uno a uno, bajo demanda**, sin tenerlos todos en memoria. `range(1_000_000_000)` no guarda mil millones de números: los genera al vuelo.

Un **generador** es la forma fácil de crear iteradores: una función con `yield` en vez de `return`:

```python
def cuenta_atras(n):
    while n > 0:
        yield n        # «entrega» n y se PAUSA aquí, recordando su estado
        n -= 1

for numero in cuenta_atras(3):
    print(numero)      # 3, 2, 1
```

Diferencia clave: `return` termina la función y olvida todo; `yield` entrega un valor, **congela** la función y la reanuda en la siguiente petición. Esto permite procesar datos infinitos o gigantescos sin llenar la RAM:

```python
def fibonacci():
    a, b = 0, 1
    while True:              # ¡secuencia infinita sin memoria infinita!
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

También existen **expresiones generadoras**: `(x**2 for x in range(1000))` — como una comprensión de lista pero perezosa.

## 5. Closures: funciones que recuerdan

Una función interna puede **recordar** las variables de la función externa que la creó:

```python
def crear_multiplicador(factor):
    def multiplicar(x):          # recuerda 'factor' aunque la externa ya terminó
        return x * factor
    return multiplicar

triple = crear_multiplicador(3)
print(triple(10))     # 30
```

Es una fábrica de funciones personalizadas. Y es la base de los decoradores.

## 6. Decoradores

Un **decorador** es una función que envuelve otra función para añadirle comportamiento sin tocar su código:

```python
import time

def cronometro(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        print(f"{funcion.__name__} tardó {time.time() - inicio:.4f}s")
        return resultado
    return envoltura

@cronometro            # equivale a: tarea_pesada = cronometro(tarea_pesada)
def tarea_pesada():
    return sum(range(10_000_000))

tarea_pesada()   # ejecuta la función Y además imprime su tiempo
```

El `@algo` sobre un `def` es azúcar sintáctico: envuelve la función. Usos reales: medir tiempos, registrar llamadas (logging), comprobar permisos, caché (`@functools.lru_cache`), rutas web en Flask/FastAPI (`@app.get("/")`). Los decoradores están en todas partes en el Python profesional.

Bonus: `@functools.lru_cache` es un decorador de la librería estándar que memoriza resultados — convierte funciones recursivas lentas en instantáneas:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))   # instantáneo; sin caché tardaría una eternidad
```

---

## ⚠️ Errores típicos

1. Llamar en vez de pasar: `map(doble(), nums)` ejecuta la función; es `map(doble, nums)`.
2. Consumir un generador dos veces: una vez recorrido, se agota (`next()` lanza `StopIteration`).
3. Lambdas con lógica compleja: si necesitas más de una expresión, usa `def`.
4. Olvidar que un decorador debe **devolver** la envoltura y que la envoltura debe devolver el resultado de la función original.

## 📝 Resumen

- Las funciones son valores: se guardan, se pasan, se devuelven.
- `lambda` para funciones cortas anónimas; `map`/`filter` transforman y filtran.
- Los generadores (`yield`) producen datos bajo demanda sin llenar memoria.
- Closures = funciones que recuerdan su contexto; decoradores = funciones que envuelven funciones (`@`).

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion14-funciones-avanzadas/practica.ipynb)

## ➡️ Siguiente paso

[Lección 15 · Librería estándar](../leccion15-modulos-estandar/)
