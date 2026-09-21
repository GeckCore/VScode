# Lección 13 · Estructuras de datos y complejidad

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion13-estructuras-datos/practica.ipynb)

## 🎯 Objetivos

- Entender qué es la complejidad algorítmica (notación Big-O)
- Usar pilas y colas correctamente
- Conocer `deque`, `heapq`, `defaultdict` y `Counter`
- Elegir la estructura adecuada para cada problema

Esta es la lección más «de carrera»: estructuras de datos y algoritmos son asignatura obligatoria en todo grado de informática.

---

## 1. Big-O: ¿cuánto tarda mi programa cuando los datos crecen?

La complejidad no mide segundos, mide **cómo crece el trabajo** al crecer la entrada `n`:

| Notación | Nombre | Ejemplo en Python | Intuición |
|----------|--------|-------------------|-----------|
| O(1) | Constante | `lista[0]`, `dicc[clave]`, `x in set` | Da igual lo grande que sea |
| O(log n) | Logarítmica | búsqueda binaria en lista ordenada | Cada paso descarta la mitad |
| O(n) | Lineal | recorrer una lista, `x in lista` | Proporcional a n |
| O(n log n) | | `sorted(lista)` | Ordenaciones buenas |
| O(n²) | Cuadrática | doble bucle anidado sobre la misma lista | Con n=10⁵ ya duele |

Reglas prácticas:

- `x in lista` es O(n) (recorre todo); `x in set` / `x in diccionario` es O(1). **Si vas a hacer muchas búsquedas, usa un set.**
- `lista.insert(0, x)` y `lista.pop(0)` son O(n) (desplazan todo); `append()`/`pop()` al final son O(1).
- Dos bucles anidados sobre n elementos = O(n²). Con 10.000 elementos ya son 100 millones de operaciones.

## 2. Pila (stack): LIFO

«Último en entrar, primero en salir». Como una pila de platos. En Python: una lista con `append` y `pop`.

```python
pila = []
pila.append("a")     # apilar
pila.append("b")
pila.append("c")
print(pila.pop())    # "c"  ← sale el último que entró
```

Usos: deshacer/rehacer (Ctrl+Z), historial del navegador, analizar paréntesis balanceados, llamadas de funciones (la *call stack*).

## 3. Cola (queue): FIFO

«Primero en entrar, primero en salir». Como la cola del súper. ⚠️ No uses `lista.pop(0)` (es O(n)): usa `collections.deque`:

```python
from collections import deque

cola = deque()
cola.append("cliente1")     # llega
cola.append("cliente2")
print(cola.popleft())       # cliente1  ← sale el primero (O(1))
```

`deque` añade y quita por **ambos extremos** en O(1): `append`/`appendleft`, `pop`/`popleft`.

## 4. Montículo (heap): sacar siempre el mínimo

`heapq` mantiene una lista donde extraer el mínimo es rapidísimo (O(log n)):

```python
import heapq

tareas = []                       # guardamos tuplas (prioridad, nombre)
heapq.heappush(tareas, (3, "pasear al perro"))
heapq.heappush(tareas, (1, "estudiar"))
heapq.heappush(tareas, (2, "comer"))

print(heapq.heappop(tareas))   # (1, 'estudiar') ← sale la más prioritaria
```

También: `heapq.nlargest(3, lista)` / `nsmallest(3, lista)` para los k mayores/menores sin ordenar todo.

## 5. defaultdict y Counter

```python
from collections import defaultdict, Counter

# defaultdict: valores por defecto automáticos, sin .get()
grupos = defaultdict(list)
for nombre, equipo in [("Ana", "rojo"), ("Luis", "azul"), ("Bea", "rojo")]:
    grupos[equipo].append(nombre)
print(dict(grupos))   # {'rojo': ['Ana', 'Bea'], 'azul': ['Luis']}

# Counter: el patrón contador de la lección 7, ya hecho
votos = Counter(["ana", "luis", "ana", "bea", "ana"])
print(votos.most_common(2))   # [('ana', 3), ('luis', 1)]
```

## 6. ¿Qué estructura uso? Guía de decisión

| Necesito... | Uso... |
|-------------|--------|
| Colección ordenada que cambia | `list` |
| Datos fijos que no deben cambiar | `tuple` |
| Buscar por clave / contar | `dict` (o `Counter`) |
| Unicidad y pertenencia rápida | `set` |
| Deshacer/último en entrar | pila = `list` con append/pop |
| Cola de espera | `deque` |
| Prioridades / «el menor siempre» | `heapq` |
| Agrupar elementos | `defaultdict(list)` |

---

## ⚠️ Errores típicos

1. Usar listas como colas con `pop(0)`: lento y mala práctica.
2. Comprobar pertenencia en una lista dentro de un bucle (O(n²) disfrazado): conviértela a `set` primero.
3. Ordenar todo para sacar el máximo: `max()` es O(n), `sorted()` O(n log n).
4. Creer que `heapq` mantiene la lista ordenada: solo garantiza que el mínimo sale primero.

## 📝 Resumen

- Big-O describe el crecimiento: O(1) ≪ O(log n) ≪ O(n) ≪ O(n log n) ≪ O(n²).
- Pila LIFO con list; cola FIFO con `deque`; prioridades con `heapq`.
- `Counter` y `defaultdict` eliminan patrones repetitivos.
- La estructura correcta suele importar más que el código listo.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion13-estructuras-datos/practica.ipynb)

## ➡️ Siguiente paso

[Lección 14 · Funciones avanzadas](../leccion14-funciones-avanzadas/)
