# Lección 04: Estructuras de Control

## 📖 ¿Qué son las Estructuras de Control?

Las estructuras de control permiten alterar el flujo de ejecución de un programa. Con ellas podemos:
- **Tomar decisiones** (condicionales)
- **Repetir acciones** (bucles/ciclos)

## 🎯 Condicionales (if, elif, else)

### if (si)
Ejecuta código solo si una condición es verdadera:

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar")
```

⚠️ **Importante:** La indentación (sangría) es obligatoria en Python.

### else (si no)
Se ejecuta cuando la condición del `if` es falsa:

```python
edad = 16

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### elif (si no, si)
Permite verificar múltiples condiciones:

```python
nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
elif nota >= 60:
    print("Regular")
else:
    print("Reprobado")
```

### Condicionales anidados
```python
edad = 25
tiene_licencia = True

if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("Necesitas obtener licencia")
else:
    print("No tienes edad para conducir")
```

### Operador ternario
Forma compacta de escribir un if-else:

```python
# Forma tradicional
edad = 20
if edad >= 18:
    estado = "mayor"
else:
    estado = "menor"

# Forma ternaria
estado = "mayor" if edad >= 18 else "menor"
```

## 🔄 Bucles (Ciclos)

### while (mientras)
Repite código mientras una condición sea verdadera:

```python
contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # Importante: actualizar la condición

print("Fin del bucle")
```

**While con break:**
```python
numero = 0

while True:  # Bucle infinito
    print(numero)
    if numero >= 10:
        break  # Sale del bucle
    numero += 1
```

**While con continue:**
```python
# Imprimir solo números impares
numero = 0

while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue  # Salta a la siguiente iteración
    print(numero)  # Solo imprime impares
```

### for (para)
Itera sobre una secuencia (lista, string, rango, etc.):

```python
# Iterar sobre una lista
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
```

```python
# Iterar sobre un string
palabra = "Python"

for letra in palabra:
    print(letra)
```

### Función range()
Genera una secuencia de números:

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 7)     # 2, 3, 4, 5, 6
range(0, 10, 2) # 0, 2, 4, 6, 8 (inicio, fin, paso)
```

**Ejemplos con range:**
```python
# Contar de 0 a 4
for i in range(5):
    print(i)

# Contar de 1 a 5
for i in range(1, 6):
    print(i)

# Contar de 2 en 2
for i in range(0, 10, 2):
    print(i)

# Contar hacia atrás
for i in range(5, 0, -1):
    print(i)
```

### for con else
El `else` se ejecuta cuando el bucle termina normalmente (sin break):

```python
for numero in range(5):
    print(numero)
else:
    print("Bucle completado")
```

## 🎯 Ejemplos Prácticos

### Ejemplo 1: Menú interactivo
```python
# Menú de opciones
opcion = 0

while opcion != 4:
    print("\n=== MENÚ ===")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Mostrar número")
    print("4. Salir")
    
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        print("¡Hola!")
    elif opcion == 2:
        print("¡Adiós!")
    elif opcion == 3:
        for i in range(1, 4):
            print(i)
    elif opcion == 4:
        print("Saliendo...")
    else:
        print("Opción inválida")
```

### Ejemplo 2: Adivina el número
```python
import random

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("¡Adivina el número entre 1 y 100!")

while not adivinado:
    intento = int(input("Tu intento: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos")
        adivinado = True
    elif intento < numero_secreto:
        print("Más alto...")
    else:
        print("Más bajo...")
```

### Ejemplo 3: Tabla de multiplicar
```python
# Tabla de multiplicar del 1 al 10
numero = int(input("Número para la tabla: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

### Ejemplo 4: Suma acumulativa
```python
# Sumar números hasta que el usuario ingrese 0
total = 0
contador = 0

while True:
    numero = float(input("Ingresa un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    total += numero
    contador += 1

if contador > 0:
    promedio = total / contador
    print(f"Suma total: {total}")
    print(f"Cantidad de números: {contador}")
    print(f"Promedio: {promedio}")
else:
    print("No ingresaste ningún número")
```

## 📚 Ejercicios

### Ejercicio 4.1: Número positivo o negativo
Crea un programa que pida un número y diga si es positivo, negativo o cero.

**Archivo**: `ejercicios/ejercicio_04_01.py`

### Ejercicio 4.2: Contador de vocales
Pide una frase y cuenta cuántas vocales tiene usando un bucle `for`.

**Archivo**: `ejercicios/ejercicio_04_02.py`

### Ejercicio 4.3: Números pares del 1 al 50
Imprime todos los números pares del 1 al 50 usando `range()`.

**Archivo**: `ejercicios/ejercicio_04_03.py`

### Ejercicio 4.4: Factorial de un número
Calcula el factorial de un número ingresado por el usuario.
- Factorial de 5 = 5 × 4 × 3 × 2 × 1 = 120

**Archivo**: `ejercicios/ejercicio_04_04.py`

### Ejercicio 4.5: Patrón de estrellas
Crea un patrón de estrellas:
```
*
**
***
****
*****
```

**Archivo**: `ejercicios/ejercicio_04_05.py`

### Ejercicio 4.6: Validador de contraseña
Pide una contraseña y valida que:
- Tenga al menos 8 caracteres
- Tenga al menos una mayúscula
- Tenga al menos un número

Si no cumple, pide la contraseña nuevamente.

**Archivo**: `ejercicios/ejercicio_04_06.py`

## ✅ Soluciones

Las soluciones están en la carpeta `soluciones/`.

## 🔍 Test de Autoevaluación

1. ¿Qué palabra clave se usa para una condicional?
2. ¿Cómo se escribe "si no" en Python?
3. ¿Qué bucle se usa cuando sabes cuántas veces repetir?
4. ¿Qué hace `break` en un bucle?
5. ¿Qué hace `continue` en un bucle?
6. ¿Qué genera `range(3)`?
7. ¿Cuándo se ejecuta el `else` en un bucle `for`?

## ➡️ Siguiente Lección

Continúa con la [Lección 05: Funciones](../leccion05-funciones/)
