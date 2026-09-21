# Lección 6 · Listas y tuplas

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion06-listas-tuplas/practica.ipynb)

## 🎯 Objetivos

- Crear y recorrer listas
- Acceder por índice y cortar con slicing
- Usar los métodos esenciales de lista
- Saber cuándo usar tuplas en vez de listas
- Crear listas en una línea con comprensiones

---

## 1. ¿Qué es una lista?

Una lista es una **colección ordenada y modificable** de elementos, escritos entre corchetes:

```python
notas = [7, 8, 5, 9]
mezcla = ["Ana", 18, True, 3.5]    # pueden mezclar tipos (aunque mejor no abusar)
vacia = []
```

Piensa en una lista como una estantería numerada: cada elemento tiene una posición.

## 2. Índices: acceder a elementos

Las posiciones **empiezan en 0**. Los índices negativos cuentan desde el final:

```python
frutas = ["manzana", "pera", "uva", "kiwi"]

print(frutas[0])     # manzana  (el PRIMERO es el 0)
print(frutas[3])     # kiwi
print(frutas[-1])    # kiwi     (el último)
print(frutas[-2])    # uva      (el penúltimo)
print(len(frutas))   # 4        (número de elementos)
```

⚠️ `frutas[4]` daría `IndexError`: con 4 elementos los índices válidos van de 0 a 3.

## 3. Slicing: cortar trozos

`lista[inicio:fin:paso]` — el `fin` **no se incluye** (igual que `range`):

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]     # [2, 3, 4]
nums[:4]      # [0, 1, 2, 3]     (desde el principio)
nums[6:]      # [6, 7, 8, 9]     (hasta el final)
nums[::2]     # [0, 2, 4, 6, 8]  (de 2 en 2)
nums[::-1]    # [9, 8, ..., 0]   (¡la lista al revés!)
```

El slicing crea una **lista nueva**; no modifica la original.

## 4. Modificar listas: los métodos esenciales

```python
compra = ["pan", "leche"]

compra.append("huevos")       # añade al final → ["pan", "leche", "huevos"]
compra.insert(1, "fruta")     # inserta en posición 1
compra.remove("pan")          # quita la primera aparición de "pan"
ultimo = compra.pop()          # quita y DEVUELVE el último
compra.sort()                  # ordena la propia lista (modifica)
compra.reverse()               # la invierte
```

Funciones que **no modifican** la lista, devuelven algo nuevo:

```python
nums = [3, 1, 4, 1, 5]
sorted(nums)     # [1, 1, 3, 4, 5]  (nums sigue igual)
len(nums)       # 5
sum(nums)       # 14
min(nums), max(nums)   # 1, 5
nums.count(1)   # 2  (cuántas veces aparece)
1 in nums       # True (¿está el 1?)
```

⚠️ Diferencia clave: `lista.sort()` modifica y devuelve `None`; `sorted(lista)` devuelve una copia ordenada. Nunca hagas `nums = nums.sort()` (guardarías `None`).

## 5. Recorrer listas

```python
nombres = ["Ana", "Bea", "Carlos"]

# forma directa (la más usada):
for nombre in nombres:
    print(nombre)

# con índice, cuando lo necesitas:
for i in range(len(nombres)):
    print(i, nombres[i])

# la forma profesional para índice + valor a la vez:
for i, nombre in enumerate(nombres):
    print(i, nombre)
```

## 6. Tuplas: listas que no cambian

Una tupla es como una lista pero **inmutable** (no se puede modificar tras crearla). Se escribe con paréntesis:

```python
punto = (3, 5)
coordenada_x = punto[0]     # se accede igual que a listas
# punto[0] = 9              # ❌ TypeError: las tuplas no se modifican

# desempaquetado: muy útil
x, y = punto                # x=3, y=5
```

¿Cuándo tupla y cuándo lista? Tupla para datos fijos que forman una unidad (coordenadas, fechas); lista para colecciones que crecen y cambian. Además, las funciones pueden devolver varios valores empaquetándolos en tupla: `return minimo, maximo`.

## 7. Comprensiones de listas (list comprehensions)

La forma pythónica de crear listas transformando otras:

```python
cuadrados = [n ** 2 for n in range(10)]          # [0, 1, 4, 9, ..., 81]
pares = [n for n in range(20) if n % 2 == 0]     # filtrar: [0, 2, 4, ..., 18]
mayus = [nombre.upper() for nombre in nombres]   # transformar
```

Estructura: `[ expresión for elemento in iterable if condición ]`. La parte del `if` es opcional. Es exactamente un bucle for comprimido, y es el estilo que verás en código profesional.

## 8. Referencias: el concepto más importante (y traicionero)

Las variables de lista **no guardan la lista, guardan una referencia** a ella:

```python
a = [1, 2, 3]
b = a            # ¡b NO es una copia! apunta a la MISMA lista
b.append(4)
print(a)         # [1, 2, 3, 4]  ← a también cambió

c = a.copy()     # copia de verdad (también vale a[:] )
c.append(5)
print(a)         # [1, 2, 3, 4]  ← a no se entera
```

Esto explica bugs misteriosos y también por qué nunca debes poner una lista como valor por defecto en una función.

---

## ⚠️ Errores típicos

1. Pensar que el primer elemento es `[1]`: es `[0]`.
2. `mi_lista = mi_lista.sort()` guarda `None`.
3. Modificar una lista mientras la recorres con `for` (provoca elementos saltados): recorre una copia.
4. `b = a` no copia listas: usa `.copy()` o `[:]`.
5. Confundir `append` (añade un elemento) con `+` (une dos listas: `[1] + [2]` → `[1, 2]`).

## 📝 Resumen

- Lista: colección ordenada y modificable; índices desde 0, negativos desde el final.
- Slicing `[inicio:fin:paso]`, con el fin excluido.
- `append`, `remove`, `pop`, `sort` modifican; `sorted`, `len`, `sum` devuelven.
- Tupla = lista inmutable; se desempaqueta con `x, y = tupla`.
- Comprensiones: `[expr for x in iterable if cond]`.
- Asignar listas copia la referencia, no el contenido.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion06-listas-tuplas/practica.ipynb)

## ➡️ Siguiente paso

[Lección 7 · Diccionarios y conjuntos](../leccion07-diccionarios-conjuntos/)
