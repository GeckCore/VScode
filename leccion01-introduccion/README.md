# Lección 1 · Introducción a Python

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion01-introduccion/practica.ipynb)

## 🎯 Objetivos

Al terminar esta lección sabrás:

- Qué es Python y por qué se usa tanto
- Qué es un programa y cómo lo ejecuta el ordenador
- Escribir y ejecutar tus primeros programas con `print()`
- Pedir datos al usuario con `input()`
- Leer mensajes de error sin entrar en pánico

---

## 1. ¿Qué es Python?

Python es un **lenguaje de programación**: un idioma con reglas precisas que usamos para darle instrucciones al ordenador. Fue creado por Guido van Rossum en 1991 y hoy es el lenguaje más usado del mundo en inteligencia artificial, ciencia de datos, automatización, desarrollo web y educación.

¿Por qué es tan popular?

- **Se lee casi como inglés.** Comparado con C o Java, un programa en Python es corto y claro.
- **Es de propósito general.** Sirve para webs, juegos, IA, robots, análisis de datos…
- **Tiene una comunidad gigante.** Casi cualquier problema que tengas ya lo ha resuelto alguien.

Python es un lenguaje **interpretado**: un programa llamado *intérprete* lee tu código línea a línea y lo ejecuta al momento. Tú escribes texto en un archivo `.py` (o en una celda de un notebook) y el intérprete hace el resto.

## 2. Tu primer programa: `print()`

La tradición manda empezar así:

```python
print("Hola, mundo")
```

`print()` es una **función**: una orden ya construida que muestra texto en pantalla. Lo que pones entre paréntesis es lo que quieres mostrar, y el texto va entre comillas:

```python
print("Me llamo Ana")
print('También valen comillas simples')
print(2026)            # los números no necesitan comillas
print(3 + 4)           # Python calcula antes de mostrar: imprime 7
```

Puedes mostrar varias cosas separadas por comas (Python las separa con un espacio):

```python
print("El resultado de 2 + 2 es", 2 + 2)
```

Salida:

```
El resultado de 2 + 2 es 4
```

## 3. Comentarios: notas para humanos

Todo lo que va después de `#` en una línea lo ignora el intérprete. Sirve para explicar tu código:

```python
# Esto es un comentario, Python no lo ejecuta
print("Hola")  # Los comentarios también pueden ir al final de una línea
```

Comenta tu código siempre que la intención no sea obvia. Tu «yo del futuro» te lo agradecerá.

## 4. Pedir datos: `input()`

`input()` pausa el programa, muestra un mensaje y espera a que el usuario escriba algo y pulse Enter. Lo que el usuario escribe se guarda en una **variable** (una etiqueta que guarda un valor; la veremos a fondo en la lección 2):

```python
nombre = input("¿Cómo te llamas? ")
print("Encantado de conocerte,", nombre)
```

⚠️ **Importante**: `input()` **siempre devuelve texto**, aunque el usuario escriba un número:

```python
edad = input("¿Cuántos años tienes? ")   # si escribes 20, edad guarda el TEXTO "20"
```

Para convertirlo en número hay que usar `int()` o `float()` — eso lo practicarás en la lección 2, pero aquí va un adelanto:

```python
edad = int(input("¿Cuántos años tienes? "))
print("El año que viene tendrás", edad + 1)
```

## 5. Leer errores sin miedo

Vas a ver errores constantemente. **No son un fracaso: son el intérprete explicándote qué no entendió.** Un error típico:

```
NameError: name 'prin' is not defined
```

Se lee de abajo arriba: la última línea dice **qué** falló (`NameError`: usaste un nombre que no existe, aquí `prin` en vez de `print`) y las líneas de arriba dicen **dónde**. Otros frecuentes:

| Error | Significado típico |
|-------|--------------------|
| `SyntaxError` | Te faltan comillas, paréntesis o dos puntos |
| `NameError` | Escribiste mal un nombre o lo usaste antes de crearlo |
| `TypeError` | Mezclaste tipos incompatibles (texto con número) |

---

## ⚠️ Errores típicos de esta lección

1. **Olvidar las comillas**: `print(Hola)` falla porque Python cree que `Hola` es una variable. El texto literal siempre va entre comillas.
2. **Escribir `Print` con mayúscula**: Python distingue mayúsculas y minúsculas. Es `print`.
3. **Pensar que `input()` devuelve números**: devuelve texto, siempre.
4. **Asustarse ante un error**: lee la última línea del mensaje primero.

## 📝 Resumen

- Python es un lenguaje interpretado, claro y multiusos.
- `print()` muestra cosas en pantalla; `input()` pide datos al usuario (y siempre devuelve texto).
- Los comentarios empiezan con `#` y no se ejecutan.
- Los errores se leen de abajo arriba: primero el tipo, luego la línea.

## 🏋️ Práctica

Abre el notebook y haz los 10 ejercicios en orden: cada uno se autocorrige con ✅.

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion01-introduccion/practica.ipynb)

## ➡️ Siguiente paso

[Lección 2 · Variables y tipos de datos](../leccion02-variables-tipos/)
