# Lección 5 · Funciones

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion05-funciones/practica.ipynb)

## 🎯 Objetivos

- Crear funciones con `def` y llamarlas
- Pasar datos con parámetros y recibir resultados con `return`
- Entender el alcance (scope) de las variables
- Usar valores por defecto y argumentos con nombre
- Escribir funciones bien documentadas

---

## 1. ¿Por qué funciones?

Una función es un **bloque de código con nombre** que puedes ejecutar cuando quieras, tantas veces como quieras. Sin funciones, los programas serían listas infinitas de instrucciones repetidas. Las funciones te dan:

- **Reutilización**: escribes la lógica una vez, la usas cien.
- **Organización**: cada función hace una cosa y la hace bien.
- **Legibilidad**: `calcular_iva(precio)` se entiende mejor que 5 líneas sueltas.

Ya has usado funciones: `print()`, `input()`, `len()`, `int()`… Ahora aprenderás a crear las tuyas.

## 2. Definir y llamar

```python
def saludar():              # def + nombre + () + :
    print("¡Hola!")         # cuerpo con sangría

saludar()                   # llamada: ejecuta el cuerpo
saludar()                   # puedes llamarla mil veces
```

⚠️ Definir una función **no la ejecuta**. Solo cuando la **llamas** (`nombre()`) corre su código.

## 3. Parámetros: datos de entrada

Los parámetros son variables que recibe la función:

```python
def saludar(nombre):            # nombre es un parámetro
    print(f"¡Hola, {nombre}!")

saludar("Ana")      # ¡Hola, Ana!
saludar("Carlos")   # ¡Hola, Carlos!
```

Puedes tener varios, separados por comas:

```python
def area_rectangulo(base, altura):
    print(base * altura)

area_rectangulo(3, 4)   # 12
```

## 4. `return`: datos de salida

Esto es lo más importante de la lección. Una función puede **devolver** un valor con `return`, y quien la llama puede guardarlo:

```python
def cuadrado(x):
    return x * x

resultado = cuadrado(5)     # guarda 25 en resultado
print(cuadrado(3) + 1)      # puedes usar el valor al momento: 10
```

**`print` vs `return` — la confusión número 1:**

- `print()` **muestra** algo en pantalla (efecto visual, no reutilizable).
- `return` **devuelve** un valor que el programa puede seguir usando.

```python
def suma_mala(a, b):
    print(a + b)        # solo lo muestra; no puedes hacer nada con él

def suma_buena(a, b):
    return a + b        # devuelve el valor

doble = suma_buena(3, 4) * 2   # 14 ✅
# doble = suma_mala(3, 4) * 2  # ❌ TypeError: suma_mala devuelve None
```

Regla profesional: las funciones **devuelven** datos; quien las usa decide si los imprime. Y ojo: una función sin `return` devuelve siempre `None`. Además, `return` termina la función al instante: lo que haya debajo no se ejecuta.

## 5. Alcance (scope): variables locales

Las variables creadas **dentro** de una función son **locales**: existen solo mientras la función corre y no se ven desde fuera.

```python
def calcular():
    resultado = 42      # local

calcular()
# print(resultado)      # ❌ NameError: no existe fuera
```

Las variables de fuera sí se pueden **leer** dentro, pero no deberías depender de eso: pasa los datos por parámetros. Es lo que hace a las funciones predecibles y fáciles de probar. La técnica de evitar `global` se considera buena práctica a nivel ingeniería.

## 6. Valores por defecto y argumentos con nombre

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}")

saludar("Ana")                    # Hola, Ana
saludar("Ana", "Buenas")          # Buenas, Ana
saludar(saludo="Ey", nombre="Ana")  # con nombre, el orden da igual
```

## 7. `*args` y `**kwargs` (nivel avanzado)

Para funciones con número variable de argumentos:

```python
def sumar_todo(*numeros):        # recoge todos los argumentos en una tupla
    total = 0
    for n in numeros:
        total += n
    return total

print(sumar_todo(1, 2, 3, 4))    # 10
```

## 8. Documentar: docstrings

La primera línea de una función puede ser un texto entre triples comillas que la documenta:

```python
def iva(precio, tasa=0.07):
    """Calcula el precio con IVA.

    precio: precio base (float)
    tasa: porcentaje de IVA (por defecto 7%, el IGIC canario)
    devuelve: precio final con IVA
    """
    return precio * (1 + tasa)
```

---

## ⚠️ Errores típicos

1. Imprimir en vez de devolver: si un ejercicio dice «devuelve», usa `return`.
2. Olvidar los paréntesis al llamar: `saludar` es la función; `saludar()` la ejecuta.
3. Usar una variable local fuera de su función.
4. Definir la función **después** de llamarla: Python lee de arriba abajo.
5. Un parámetro por defecto como lista (`def f(x=[])`) crea bugs raros; usa `None` y créala dentro (lo entenderás en la lección 6).

## 📝 Resumen

- `def nombre(parámetros):` define; `nombre(valores)` llama.
- `return` devuelve un valor y termina la función. Sin `return` → devuelve `None`.
- Las variables locales viven solo dentro de la función.
- Valores por defecto y argumentos con nombre hacen funciones flexibles.
- Documenta con docstrings.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion05-funciones/practica.ipynb)

## ➡️ Siguiente paso

[Lección 6 · Listas y tuplas](../leccion06-listas-tuplas/)
