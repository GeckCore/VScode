# Lección 4 · Estructuras de control

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion04-estructuras-control/practica.ipynb)

## 🎯 Objetivos

- Tomar decisiones con `if`, `elif`, `else`
- Repetir código con `while` y `for`
- Usar `range()` para contar
- Controlar bucles con `break` y `continue`
- Evitar bucles infinitos

---

## 1. La indentación: la regla sagrada de Python

En Python, el código que pertenece a un bloque se marca **con sangría** (4 espacios o un tabulador). No hay llaves `{}` como en otros lenguajes:

```python
if edad >= 18:
    print("Eres mayor de edad")   # estas líneas con sangría
    print("Puedes votar")          # pertenecen al if
print("Fin")                        # esta ya no
```

Un error de sangría (`IndentationError`) es de los más comunes al empezar. Colab y los editores te ayudan, pero entiende la regla: **misma sangría = mismo bloque**.

## 2. Decisiones: `if`, `elif`, `else`

```python
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

Reglas:

- Python evalúa las condiciones **de arriba abajo** y ejecuta solo el primer bloque que sea `True`. El resto se salta.
- `elif` (else + if) puede repetirse las veces que quieras; `else` es opcional y va siempre al final.
- Cada condición termina en `:`.

⚠️ El orden importa. Si pones `nota >= 5` primero, un 9 entraría ahí y nunca llegaría a «Sobresaliente». Ordena de más exigente a menos.

## 3. Bucle `while`: repetir mientras se cumpla una condición

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1      # ¡sin esto el bucle es INFINITO!
```

El patrón `while` tiene 3 piezas: **inicializar** la variable de control, **condición**, y **actualizar** la variable dentro. Olvidar la tercera pieza = bucle infinito (el programa nunca termina).

Úsalo cuando **no sabes cuántas repeticiones harán falta**: pedir una contraseña hasta que sea correcta, jugar hasta que el jugador pierda…

## 4. Bucle `for`: repetir un número conocido de veces

`for` recorre los elementos de una secuencia. Con `range()` generas números:

```python
for i in range(5):        # 0, 1, 2, 3, 4 (¡empieza en 0 y NO incluye el 5!)
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 11, 2): # 0, 2, 4, 6, 8, 10 (de 2 en 2)
    print(i)
```

También recorre texto letra a letra (y en la lección 6, listas):

```python
for letra in "Python":
    print(letra)
```

**¿Cuál usar?** Si sabes cuántas veces → `for`. Si depende de una condición → `while`.

## 5. `break` y `continue`

- `break`: sale del bucle inmediatamente.
- `continue`: salta a la siguiente vuelta, ignorando lo que quede del bloque.

```python
for n in range(1, 11):
    if n == 4:
        continue   # se salta el 4
    if n == 8:
        break      # para en el 8
    print(n)       # imprime 1 2 3 5 6 7
```

## 6. Patrones clásicos con bucles

Estos tres patrones resuelven el 80% de los ejercicios de programación básica:

```python
# PATRÓN ACUMULADOR: sumar cosas
total = 0
for i in range(1, 101):
    total += i          # suma 1+2+...+100
print(total)            # 5050

# PATRÓN CONTADOR: contar cosas que cumplen algo
multiplos = 0
for i in range(1, 51):
    if i % 3 == 0:
        multiplos += 1
print(multiplos)        # 16

# PATRÓN BUSCADOR: encontrar algo y parar
secreto = 7
intento = 0
while intento != secreto:
    intento = int(input("Adivina el número: "))
print("¡Acertaste!")
```

## 7. Bucles anidados

Un bucle dentro de otro. El interior se completa entero por cada vuelta del exterior:

```python
for fila in range(3):
    for col in range(4):
        print("*", end=" ")   # end=" " evita el salto de línea
    print()                    # salto de línea al terminar la fila
```

Salida:

```
* * * *
* * * *
* * * *
```

---

## ⚠️ Errores típicos

1. `range(5)` llega hasta 4, no hasta 5. El límite superior nunca se incluye.
2. Bucles infinitos por olvidar actualizar la variable del `while`.
3. `if x = 5:` → debe ser `==`.
4. Mezclar tabuladores y espacios en la sangría (usa siempre 4 espacios; Colab lo hace solo).
5. Poner el `else` al nivel equivocado: la sangría define a qué `if` pertenece.

## 📝 Resumen

- `if/elif/else` ejecutan bloques según condiciones, en orden.
- `while` repite mientras la condición sea verdadera; `for` recorre secuencias y rangos.
- `break` sale del bucle; `continue` salta a la siguiente vuelta.
- Domina los patrones acumulador, contador y buscador.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion04-estructuras-control/practica.ipynb)

## ➡️ Siguiente paso

[Lección 5 · Funciones](../leccion05-funciones/)
