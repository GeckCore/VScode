# Lección 2 · Variables y tipos de datos

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion02-variables-tipos/practica.ipynb)

## 🎯 Objetivos

Al terminar esta lección sabrás:

- Qué es una variable y cómo se crea
- Los 4 tipos básicos: `int`, `float`, `str`, `bool`
- Convertir entre tipos (`int()`, `str()`, `float()`)
- Construir textos dinámicos con f-strings
- Elegir buenos nombres de variable

---

## 1. ¿Qué es una variable?

Una variable es una **etiqueta que apunta a un valor** guardado en la memoria del ordenador. Se crea asignando con `=`:

```python
edad = 18
nombre = "Ana"
```

Se lee: «la variable `edad` guarda el valor 18». No es una ecuación matemática: `=` significa **guardar**, no «es igual a». Por eso esto tiene sentido:

```python
puntos = 10
puntos = puntos + 5   # coge el valor actual (10), súmale 5 y guárdalo de nuevo → 15
print(puntos)         # 15
```

## 2. Los 4 tipos básicos

Cada valor en Python tiene un **tipo**. Los fundamentales:

| Tipo | Qué es | Ejemplos |
|------|--------|----------|
| `int` | Números enteros | `5`, `-3`, `1000000` |
| `float` | Números con decimales | `3.14`, `-0.5`, `2.0` |
| `str` | Texto (cadena de caracteres) | `"hola"`, `'Python'` |
| `bool` | Verdadero o falso | `True`, `False` |

Puedes preguntar el tipo de cualquier cosa con `type()`:

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hola"))    # <class 'str'>
print(type(True))      # <class 'bool'>
```

**Detalles que importan:**

- Los decimales en Python usan **punto**, no coma: `precio = 9.99` ✅, `precio = 9,99` ❌.
- `"42"` (con comillas) es texto, no un número. `type("42")` es `str`.
- `True` y `False` van con mayúscula inicial. Son el resultado de las comparaciones: `5 > 3` vale `True`.

## 3. Operaciones con texto

Los `str` se pueden unir (**concatenar**) con `+` y repetir con `*`:

```python
saludo = "Hola" + " " + "mundo"
print(saludo)        # Hola mundo
print("ja" * 3)      # jajaja
```

Y medir su longitud con `len()`:

```python
print(len("Python"))   # 6
```

⚠️ No puedes mezclar texto y número con `+`:

```python
edad = 18
# print("Tengo " + edad)   # ❌ TypeError
print("Tengo " + str(edad))  # ✅ convierte antes
```

## 4. Conversión de tipos (casting)

```python
int("25")      # 25      (texto → entero)
float("3.5")   # 3.5     (texto → decimal)
str(100)       # "100"   (número → texto)
int(3.99)      # 3       (⚠️ trunca, no redondea)
bool(0)        # False   (0, 0.0 y "" son «falsos»; el resto «verdaderos»)
```

Esto es esencial con `input()`, que siempre devuelve `str`:

```python
precio = float(input("Precio: "))
print("Con IVA:", precio * 1.07)
```

## 5. f-strings: la forma moderna de mezclar texto y valores

Un **f-string** es un texto precedido de `f` que permite incrustar valores entre llaves `{}`. Es la forma recomendada:

```python
nombre = "Ana"
edad = 18
print(f"Me llamo {nombre} y tengo {edad} años")
print(f"El año que viene tendré {edad + 1}")   # dentro de {} puede haber operaciones
precio = 9.5
print(f"Precio: {precio:.2f} €")               # :.2f → 2 decimales → "Precio: 9.50 €"
```

## 6. Nombres de variable

Reglas obligatorias (si no, `SyntaxError`):

- Solo letras, números y guion bajo `_`. Sin espacios ni tildes (aunque Python las tolera, no se usan por convención).
- No puede empezar por número: `2edad` ❌, `edad2` ✅.
- No puedes usar palabras reservadas (`if`, `for`, `while`, `print`…).

Convenciones (cómo lo escriben los profesionales):

- **snake_case**: minúsculas con guiones bajos: `nota_media`, `velocidad_maxima`.
- Nombres **descriptivos**: `precio_total` mejor que `x` o `pt`.
- Las constantes (valores que no cambian) en MAYÚSCULAS: `IVA = 0.07`.

## 7. Asignación abreviada

Muy usada en bucles y contadores:

```python
puntos = 100
puntos += 20    # equivale a puntos = puntos + 20  → 120
puntos -= 10    # → 110
puntos *= 2     # → 220
puntos /= 4     # → 55.0  (¡la división siempre da float!)
```

---

## ⚠️ Errores típicos

1. `int("3.5")` falla: para texto con decimales usa `float()`.
2. Creer que `int(3.99)` da 4: trunca, da 3. Para redondear usa `round(3.99)`.
3. Usar `=` para comparar: `=` guarda, `==` compara (lo verás en la lección 3).
4. Comas decimales: en Python es `9.99`, nunca `9,99`.
5. Nombres como `precio-total` (con guion): Python lo lee como una resta. Usa `_`.

## 📝 Resumen

- Una variable guarda un valor; `=` asigna y se puede reasignar.
- Tipos básicos: `int`, `float`, `str`, `bool`. `type()` te dice el tipo.
- Convierte con `int()`, `float()`, `str()`. `input()` siempre da `str`.
- Los f-strings (`f"Hola {nombre}"`) son la forma moderna de construir texto.
- Nombres en snake_case y descriptivos.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion02-variables-tipos/practica.ipynb)

## ➡️ Siguiente paso

[Lección 3 · Operadores](../leccion03-operadores/)
