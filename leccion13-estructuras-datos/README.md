# Lección 13: Estructuras de Datos Avanzadas

## 📖 Introducción

Python ofrece estructuras de datos poderosas más allá de listas y diccionarios básicos. Esta lección cubre:

- **Listas por comprensión** (list comprehensions)
- **Diccionarios por comprensión**
- **Generadores**
- **Iteradores**
- **Módulo collections**

## 🎯 Listas por Comprensión

Una forma concisa de crear listas transformando iterables.

### Sintaxis básica
```python
# Forma tradicional
cuadrados = []
for i in range(10):
    cuadrados.append(i ** 2)

# Con list comprehension
cuadrados = [i ** 2 for i in range(10)]
```

### Con condición
```python
# Números pares del 1 al 20
pares = [x for x in range(1, 21) if x % 2 == 0]
# Resultado: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Filtrar palabras con más de 5 letras
palabras = ["casa", "elefante", "sol", "computadora"]
largas = [p for p in palabras if len(p) > 5]
# Resultado: ['elefante', 'computadora']
```

### Anidadas
```python
# Tabla de multiplicar
tabla = [[i * j for j in range(1, 11)] for i in range(1, 11)]

# Aplanar una matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [num for fila in matriz for num in fila]
# Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 📚 Diccionarios por Comprensión

```python
# Crear diccionario de cuadrados
cuadrados = {x: x**2 for x in range(5)}
# Resultado: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtrar diccionario
precios = {"manzana": 1.5, "banana": 0.8, "uva": 2.5}
caros = {k: v for k, v in precios.items() if v > 1}
# Resultado: {"manzana": 1.5, "uva": 2.5}

# Intercambiar claves y valores
inverso = {v: k for k, v in precios.items()}
```

## ⚡ Generadores

Los generadores son funciones que retornan un iterable perezoso (lazy evaluation).

### Funciones generadoras
```python
def numeros_naturales():
    """Genera números naturales infinitos"""
    n = 0
    while True:
        yield n
        n += 1

# Uso
gen = numeros_naturales()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

# Iterar sobre el generador
for i in numeros_naturales():
    if i > 10:
        break
    print(i, end=" ")
```

### Expresiones generadoras
Similar a list comprehension pero con paréntesis:

```python
# List comprehension (crea toda la lista en memoria)
lista_cuadrados = [x**2 for x in range(1000000)]

# Generator expression (calcula bajo demanda)
gen_cuadrados = (x**2 for x in range(1000000))

# Más eficiente para grandes volúmenes de datos
suma_cuadrados = sum(x**2 for x in range(1000000))
```

### Ejemplo práctico: Lectura eficiente de archivos
```python
def leer_archivo_lineas(ruta):
    """Generador que lee archivo línea por línea"""
    with open(ruta, 'r') as f:
        for linea in f:
            yield linea.strip()

# Uso eficiente de memoria
for linea in leer_archivo_lineas("archivo_grande.txt"):
    procesar(linea)
```

## 🔄 Iteradores Personalizados

```python
class ContadorInfinito:
    """Iterador personalizado"""
    
    def __init__(self, inicio=0, paso=1):
        self.actual = inicio
        self.paso = paso
    
    def __iter__(self):
        return self
    
    def __next__(self):
        valor = self.actual
        self.actual += self.paso
        return valor

# Uso
contador = ContadorInfinito(inicio=10, paso=5)
print(next(contador))  # 10
print(next(contador))  # 15
print(next(contador))  # 20
```

## 📦 Módulo collections

### Counter - Contador especializado
```python
from collections import Counter

texto = "hola mundo hola python hola"
palabras = texto.split()

contador = Counter(palabras)
print(contador)  # Counter({'hola': 3, 'mundo': 1, 'python': 1})

# Los 2 más comunes
print(contador.most_common(2))  # [('hola', 3), ('mundo', 1)]
```

### defaultdict - Diccionario con valor por defecto
```python
from collections import defaultdict

# Sin defaultdict
dicc = {}
for clave in ['a', 'b', 'a', 'c']:
    if clave not in dicc:
        dicc[clave] = []
    dicc[clave].append(1)

# Con defaultdict
dicc_defecto = defaultdict(list)
for clave in ['a', 'b', 'a', 'c']:
    dicc_defecto[clave].append(1)
# Resultado: {'a': [1, 1], 'b': [1], 'c': [1]}
```

### deque - Cola de dos extremos
```python
from collections import deque

cola = deque([1, 2, 3])
cola.append(4)        # Agrega al final
cola.appendleft(0)    # Agrega al inicio
cola.pop()            # Elimina del final
cola.popleft()        # Elimina del inicio

# Ideal para colas FIFO y pilas LIFO
```

### namedtuple - Tuplas con nombres
```python
from collections import namedtuple

# Definir tipo
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])

# Crear instancia
juan = Persona(nombre="Juan", edad=30, ciudad="Madrid")

# Acceso por nombre (más legible)
print(juan.nombre)  # Juan
print(juan.edad)    # 30

# Desempaquetado
nombre, edad, ciudad = juan
```

## 🎯 Ejemplos Prácticos

### Ejemplo 1: Procesamiento de datos con generadores
```python
def filtrar_pares(numeros):
    """Generador que filtra solo pares"""
    for n in numeros:
        if n % 2 == 0:
            yield n

def cuadrado(numeros):
    """Generador que calcula cuadrados"""
    for n in numeros:
        yield n ** 2

# Pipeline de procesamiento
datos = range(100)
resultado = list(cuadrado(filtrar_pares(datos)))
print(sum(resultado))  # Suma de cuadrados de pares
```

### Ejemplo 2: Análisis de texto avanzado
```python
from collections import Counter, defaultdict

def analizar_texto(texto):
    """Analiza frecuencia de palabras y letras"""
    palabras = texto.lower().split()
    
    # Frecuencia de palabras
    freq_palabras = Counter(palabras)
    
    # Frecuencia de letras
    letras = [l for palabra in palabras for l in palabra if l.isalpha()]
    freq_letras = Counter(letras)
    
    # Palabras por longitud
    por_longitud = defaultdict(list)
    for palabra in set(palabras):
        por_longitud[len(palabra)].append(palabra)
    
    return {
        'palabras_comunes': freq_palabras.most_common(5),
        'letras_comunes': freq_letras.most_common(5),
        'por_longitud': dict(por_longitud)
    }

texto = "Python es increíble Python es poderoso Python es genial"
analisis = analizar_texto(texto)
print(analisis['palabras_comunes'])
```

### Ejemplo 3: Sistema de caché con OrderedDict
```python
from collections import OrderedDict

class CacheLRU:
    """Caché con política Least Recently Used"""
    
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cache = OrderedDict()
    
    def get(self, clave):
        if clave in self.cache:
            # Mover al final (más reciente)
            self.cache.move_to_end(clave)
            return self.cache[clave]
        return None
    
    def put(self, clave, valor):
        if clave in self.cache:
            self.cache.move_to_end(clave)
        self.cache[clave] = valor
        
        if len(self.cache) > self.capacidad:
            # Eliminar el menos reciente (primero)
            self.cache.popitem(last=False)

# Uso
cache = CacheLRU(2)
cache.put('a', 1)
cache.put('b', 2)
cache.put('c', 3)  # Elimina 'a'
print(cache.get('b'))  # 2
print(cache.get('a'))  # None (fue eliminado)
```

## 📝 Ejercicios

### Ejercicio 13.1: List comprehension avanzado
Crea una lista con todos los números del 1 al 100 que sean divisibles por 3 y 5 simultáneamente.

### Ejercicio 13.2: Generador de Fibonacci
Crea un generador que produzca la secuencia de Fibonacci infinita.

### Ejercicio 13.3: Analizador de logs
Usa `Counter` y `defaultdict` para analizar un archivo de logs y encontrar:
- Las 5 IPs más frecuentes
- Errores por tipo
- Requests por hora

### Ejercicio 13.4: Iterador de rango personalizado
Crea un iterador que genere números primos infinitos.

## ✅ Soluciones

Las soluciones están en la carpeta `soluciones/solucion_13_*.py`.

## 🔍 Test de Autoevaluación

1. ¿Cuál es la diferencia entre list comprehension y generator expression?
2. ¿Qué hace la palabra clave `yield`?
3. ¿Cuándo usarías `defaultdict` en lugar de `dict` normal?
4. ¿Qué ventaja tiene `deque` sobre una lista para colas?
5. ¿Cómo funciona `namedtuple` y cuándo es útil?

## ➡️ Siguiente Lección

Continúa con la [Lección 14: Funciones Avanzadas](../leccion14-funciones-avanzadas/)
