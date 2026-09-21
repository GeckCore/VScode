# Lección 3 · Operadores

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion03-operadores/practica.ipynb)

## 🎯 Objetivos

- Dominar los operadores aritméticos, incluidos `//` y `%` que se usan muchísimo
- Comparar valores con operadores de comparación
- Combinar condiciones con `and`, `or`, `not`
- Entender la precedencia (qué se calcula primero)

---

## 1. Operadores aritméticos

| Operador | Qué hace | Ejemplo | Resultado |
|----------|----------|---------|-----------|
| `+` | Suma | `3 + 2` | `5` |
| `-` | Resta | `3 - 2` | `1` |
| `*` | Multiplicación | `3 * 2` | `6` |
| `/` | División (siempre float) | `7 / 2` | `3.5` |
| `//` | División entera (sin decimales) | `7 // 2` | `3` |
| `%` | Resto de la división | `7 % 2` | `1` |
| `**` | Potencia | `2 ** 10` | `1024` |

### La división siempre da float

```python
print(10 / 5)    # 2.0, no 2
print(10 // 5)   # 2     (división entera)
```

### `%` (módulo): el operador estrella

`a % b` es el **resto** de dividir `a` entre `b`. Sus usos clásicos:

```python
10 % 2 == 0     # True → 10 es par
7 % 2 == 1      # True → 7 es impar
minutos = 135
horas = minutos // 60      # 2
resto = minutos % 60       # 15 → 135 min = 2 h 15 min
```

Si `a % b == 0`, entonces `b` divide exactamente a `a` (¡clave para problemas de divisibilidad!).

## 2. Operadores de comparación

Devuelven un **booleano** (`True`/`False`):

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `==` | igual a | `5 == 5` → `True` |
| `!=` | distinto de | `5 != 3` → `True` |
| `>` , `<` | mayor / menor | `7 > 3` → `True` |
| `>=` , `<=` | mayor o igual / menor o igual | `18 >= 18` → `True` |

⚠️ **El error número 1 de los principiantes**: confundir `=` (asignar) con `==` (comparar).

```python
x = 5        # guarda 5 en x
x == 5       # pregunta: ¿x vale 5? → True
```

Las comparaciones también funcionan con texto (orden alfabético):

```python
"ana" < "bea"     # True (a va antes que b)
"Ana" == "ana"    # False (mayúsculas ≠ minúsculas)
```

## 3. Operadores lógicos: `and`, `or`, `not`

Sirven para combinar condiciones:

```python
edad = 20
tiene_dni = True

print(edad >= 18 and tiene_dni)   # True  (las dos deben cumplirse)
print(edad < 18 or tiene_dni)     # True  (basta con una)
print(not tiene_dni)              # False (invierte)
```

Tabla de verdad rápida:

| `a` | `b` | `a and b` | `a or b` |
|-----|-----|-----------|----------|
| True | True | True | True |
| True | False | False | True |
| False | False | False | False |

Truco mental: `and` es exigente (todo debe ser verdad), `or` es flexible (basta una cosa), `not` niega.

## 4. Precedencia: ¿qué se calcula primero?

Orden de prioridad (de mayor a menor):

1. Paréntesis `()`
2. Potencia `**`
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. Comparaciones (`==`, `<`...)
6. `not`, luego `and`, luego `or`

```python
print(2 + 3 * 4)        # 14 (primero 3*4)
print((2 + 3) * 4)      # 20 (los paréntesis mandan)
print(not True and False)  # False: primero not True → False, luego False and False
```

**Regla profesional**: cuando dudes, pon paréntesis. Código claro > código listillo.

## 5. Valores «verdaderos» y «falsos» (truthy/falsy)

En Python, casi todo se puede interpretar como verdadero o falso:

- Falsos (`falsy`): `0`, `0.0`, `""` (texto vacío), `None`, listas/diccionarios vacíos
- El resto: verdaderos (`truthy`)

```python
nombre = ""
if nombre:          # equivale a "si nombre no está vacío"
    print("Hola")
else:
    print("No escribiste nada")
```

---

## ⚠️ Errores típicos

1. Escribir `x = 5 == 5` queriendo comparar: guarda `True` en `x`.
2. Esperar que `10 / 2` dé un entero: da `5.0`.
3. Escribir condiciones como `18 <= edad < 30`... ¡es correcto en Python! (a diferencia de otros lenguajes). Aprovéchalo.
4. `if edad = 18:` → `SyntaxError`: en las condiciones va `==`.

## 📝 Resumen

- `/` divide con decimales, `//` da el cociente entero, `%` da el resto.
- Comparar (`==`, `!=`, `<`, `>`...) produce booleanos.
- `and`/`or`/`not` combinan condiciones; `and` antes que `or`.
- Usa paréntesis para que la intención sea obvia.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion03-operadores/practica.ipynb)

## ➡️ Siguiente paso

[Lección 4 · Estructuras de control](../leccion04-estructuras-control/)
