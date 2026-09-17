# Lección 03: Operadores

## 📖 ¿Qué son los Operadores?

Los operadores son símbolos que realizan operaciones sobre variables y valores. Python tiene varios tipos de operadores.

## 🎯 Tipos de Operadores

### 1. Operadores Aritméticos

Realizan operaciones matemáticas básicas:

| Operador | Descripción | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `+` | Suma | `5 + 3` | `8` |
| `-` | Resta | `5 - 3` | `2` |
| `*` | Multiplicación | `5 * 3` | `15` |
| `/` | División (float) | `5 / 2` | `2.5` |
| `//` | División entera | `5 // 2` | `2` |
| `%` | Módulo (resto) | `5 % 2` | `1` |
| `**` | Potencia | `5 ** 2` | `25` |

**Ejemplos:**
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 (solo parte entera)
print(a % b)   # 1 (resto de la división)
print(a ** b)  # 1000 (10 al cubo)
```

### 2. Operadores de Comparación

Comparan valores y devuelven un booleano (`True` o `False`):

| Operador | Descripción | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `>=` | Mayor o igual | `5 >= 5` | `True` |
| `<=` | Menor o igual | `5 <= 3` | `False` |

**Ejemplos:**
```python
edad = 18
tiene_permiso = edad >= 18  # True

precio = 100
es_gratis = precio == 0     # False

nombre = "Ana"
es_ana = nombre == "Ana"    # True
```

### 3. Operadores Lógicos

Combinan expresiones booleanas:

| Operador | Descripción | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `and` | Y lógico | `True and False` | `False` |
| `or` | O lógico | `True or False` | `True` |
| `not` | Negación | `not True` | `False` |

**Tablas de verdad:**

**AND:**
- `True and True` → `True`
- `True and False` → `False`
- `False and True` → `False`
- `False and False` → `False`

**OR:**
- `True or True` → `True`
- `True or False` → `True`
- `False or True` → `True`
- `False or False` → `False`

**Ejemplos:**
```python
edad = 25
tiene_dinero = True

puede_comprar = edad >= 18 and tiene_dinero  # True

dia = "sábado"
es_finde = dia == "sábado" or dia == "domingo"  # True

llueve = False
no_llueve = not llueve  # True
```

### 4. Operadores de Asignación

Asignan valores a variables:

| Operador | Ejemplo | Equivalente a |
|----------|---------|---------------|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

**Ejemplos:**
```python
contador = 0
contador += 1  # contador = 1
contador += 1  # contador = 2

precio = 100
precio *= 1.21  # precio = 121.0 (con IVA)

numero = 10
numero %= 3     # numero = 1 (resto de 10/3)
```

### 5. Operadores de Identidad

Comprueban si dos variables apuntan al mismo objeto:

| Operador | Descripción |
|----------|-------------|
| `is` | Es el mismo objeto |
| `is not` | No es el mismo objeto |

**Ejemplo:**
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)      # True (mismo valor)
print(a is b)      # False (objetos diferentes)
print(a is c)      # True (misma referencia)
print(a is not b)  # True
```

### 6. Operadores de Pertenencia

Comprueban si un valor está en una secuencia:

| Operador | Descripción |
|----------|-------------|
| `in` | Está contenido |
| `not in` | No está contenido |

**Ejemplos:**
```python
frutas = ["manzana", "banana", "naranja"]

print("banana" in frutas)      # True
print("uva" in frutas)         # False
print("uva" not in frutas)     # True

texto = "Hola Mundo"
print("H" in texto)            # True
print("z" not in texto)        # True
```

## 🎯 Ejemplos Prácticos

### Ejemplo 1: Calculadora completa
```python
# Calculadora con todos los operadores
a = 10
b = 3

print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")
```

### Ejemplo 2: Verificador de acceso
```python
# Sistema de acceso
usuario_correcto = "admin"
password_correcto = "1234"

usuario = input("Usuario: ")
password = input("Password: ")

acceso_concedido = usuario == usuario_correcto and password == password_correcto

print(f"Acceso concedido: {acceso_concedido}")
```

### Ejemplo 3: Descuento por edad y membresía
```python
# Cálculo de descuento
edad = 70
es_miembro = True
precio_base = 100

# Descuento por edad (mayores de 65)
descuento_edad = edad >= 65

# Descuento por membresía
descuento_membresia = es_miembro

# Aplicar descuentos
if descuento_edad:
    precio_base *= 0.9  # 10% descuento

if descuento_membresia:
    precio_base *= 0.95  # 5% descuento adicional

print(f"Precio final: ${precio_base:.2f}")
```

## 📚 Ejercicios

### Ejercicio 3.1: Calculadora de IMC
Crea un programa que calcule el Índice de Masa Corporal:
- Fórmula: IMC = peso / (altura ** 2)
- Pide peso en kg y altura en metros
- Muestra el resultado con 2 decimales

**Archivo**: `ejercicios/ejercicio_03_01.py`

### Ejercicio 3.2: Verificador de año bisiesto
Un año es bisiesto si:
- Es divisible por 4 Y no por 100, O
- Es divisible por 400

Crea un programa que pida un año y diga si es bisiesto.

**Archivo**: `ejercicios/ejercicio_03_02.py`

### Ejercicio 3.3: Operaciones combinadas
Dados dos números ingresados por el usuario, muestra:
- Suma, resta, multiplicación, división
- División entera y módulo
- Potencia del primero elevado al segundo

**Archivo**: `ejercicios/ejercicio_03_03.py`

### Ejercicio 3.4: Validador de rango
Pide un número y verifica si está entre 1 y 100 (inclusive).
Muestra `True` si está en el rango, `False` si no.

**Archivo**: `ejercicios/ejercicio_03_04.py`

### Ejercicio 3.5: Buscador de caracteres
Pide una frase y una letra.
Verifica si la letra está en la frase (usa `in`).

**Archivo**: `ejercicios/ejercicio_03_05.py`

## ✅ Soluciones

Las soluciones están en la carpeta `soluciones/`.

## 🔍 Test de Autoevaluación

1. ¿Qué operador se usa para división entera?
2. ¿Qué devuelve `5 % 2`?
3. ¿Cuál es la diferencia entre `=` y `==`?
4. ¿Qué devuelve `True and False`?
5. ¿Qué operador verifica si un elemento está en una lista?
6. ¿Qué hace `x += 5`?

## ➡️ Siguiente Lección

Continúa con la [Lección 04: Estructuras de Control](../leccion04-estructuras-control/)
