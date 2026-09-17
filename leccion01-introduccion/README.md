# 📚 Lección 01: ¿Qué es Python y cómo funciona?

## 🎯 Objetivos de esta lección

Al finalizar esta lección podrás:
- Entender qué es un lenguaje de programación
- Comprender por qué Python es especial
- Conocer la historia de Python
- Escribir y ejecutar tu primer programa
- Entender qué es una terminal/consola

---

## 1. ¿Qué es un lenguaje de programación?

### Analogía: La Cocina 👨‍🍳

Imagina que quieres preparar una torta (pastel). Necesitas:
1. **Ingredientes** → Datos en programación
2. **Receta** → Programa/Código
3. **Cocinero** → Computadora
4. **Instrucciones precisas** → Lenguaje de programación

Si le dices al cocinero: "haz una torta", no sabrá qué hacer. Necesitas instrucciones DETALLADAS:
```
1. Precalienta el horno a 180°C
2. Mezcla 2 tazas de harina con 1 taza de azúcar
3. Agrega 3 huevos uno por uno
4. Bate durante 5 minutos
5. Vierte en molde engrasado
6. Hornea por 45 minutos
```

**Un lenguaje de programación es exactamente eso**: una forma de darle instrucciones PRECISAS y DETALLADAS a la computadora.

### ¿Por qué necesitamos lenguajes de programación?

Las computadoras solo entienden **ceros y unos** (lenguaje binario/máquina). Pero escribir en ceros y unos es:
- ❌ Muy difícil para humanos
- ❌ Propenso a errores
- ❌ Lentísimo

Los lenguajes de programación son como **traductores**:
```
Tú escribes: print("Hola")
     ↓ (traducción)
Computadora entiende: 01001000 01101111 01101100 01100001
```

---

## 2. ¿Por qué Python es especial? 🐍

### Características únicas de Python:

#### ✅ Fácil de leer y escribir

**En Java:**
```java
public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
    }
}
```

**En Python:**
```python
print("Hola Mundo")
```

¡Solo UNA línea! Python está diseñado para ser legible como inglés.

#### ✅ Versátil

Python sirve para:
- 🌐 Desarrollo web (Instagram, Pinterest usan Python)
- 🤖 Inteligencia Artificial y Machine Learning
- 📊 Análisis de datos y estadísticas
- 🎮 Desarrollo de videojuegos
- 🔬 Investigación científica
- 🤖 Automatización de tareas
- 📱 Aplicaciones de escritorio

#### ✅ Gran comunidad

Millones de personas usan Python, lo que significa:
- Miles de tutoriales gratuitos
- Foros activos donde ayudarte
- Bibliotecas para casi cualquier cosa
- Actualizaciones constantes

#### ✅ Multiplataforma

Funciona en:
- Windows 💻
- Mac 🍎
- Linux 🐧
- Incluso en servidores y supercomputadoras

---

## 3. Breve Historia de Python 📜

| Año | Evento |
|-----|--------|
| 1989 | Guido van Rossum comienza a crear Python en Navidad |
| 1991 | Primera versión pública (Python 0.9.0) |
| 2000 | Python 2.0 - nuevas características |
| 2008 | Python 3.0 - versión moderna (incompatible con Python 2) |
| 2020 | Fin oficial de Python 2 |
| Hoy | Python 3.11+ - el más rápido hasta ahora |

**¿Por qué se llama Python?**
No viene de la serpiente, sino del grupo de comedia británico **"Monty Python"**. ¡Guido era fan!

---

## 4. Tu Primer Programa: "Hola Mundo" 👋

### Tradición en Programación

El primer programa que todo programador escribe es mostrar "Hola Mundo" en pantalla. Es un ritual de iniciación.

### Escribe tu primer código:

```python
print("Hola Mundo")
```

### Explicación LÍNEA POR LÍNEA:

```python
print("Hola Mundo")
│      │            │
│      │            └─ Paréntesis de cierre
│      │               (indica fin de instrucción)
│      │
│      └─ Texto entre comillas
│         (lo que queremos mostrar)
│
└─ Palabra reservada 'print'
   (instrucción para mostrar en pantalla)
```

### Desglose detallado:

#### `print` - La función impresora

- Es una **función incorporada** de Python (built-in)
- Su trabajo: mostrar información en pantalla
- Siempre lleva paréntesis: `print()`
- Puede mostrar texto, números, resultados, etc.

#### `"Hola Mundo"` - El string

- Las **comillas** indican que es texto (string)
- Puedes usar comillas simples `' '` o dobles `" "`
- Lo que está dentro se muestra TAL CUAL
- Si escribes `print(Hola Mundo)` sin comillas → ERROR

#### Los paréntesis `()`

- Indican que estás **llamando** a la función
- Dentro van los **argumentos** (lo que le das a print)
- Aunque esté vacío `print()`, necesita los paréntesis

---

## 5. ¿Cómo ejecutar tu código? 🖥️

### Opción A: Usando la terminal/consola

#### ¿Qué es la terminal?

Es una interfaz de TEXTO donde escribes comandos directamente a la computadora.

**En Windows:**
- Busca "Símbolo del sistema" o "PowerShell"
- Verás una ventana negra con texto blanco

**En Mac:**
- Busca "Terminal" en Spotlight (Cmd+Espacio)
- Verás una ventana con fondo usualmente negro

**En Linux:**
- Ctrl+Alt+T en la mayoría de distribuciones

#### Pasos para ejecutar Python:

1. Abre la terminal
2. Escribe `python` o `python3` y presiona Enter
3. Verás algo como: `>>>` (esto es el prompt interactivo)
4. Escribe: `print("Hola Mundo")`
5. Presiona Enter
6. ¡Verás: `Hola Mundo`!

```
>>> print("Hola Mundo")
Hola Mundo
>>>
```

#### Salir del modo interactivo:
- Escribe: `exit()` o presiona Ctrl+D (Mac/Linux) / Ctrl+Z (Windows)

### Opción B: Usando un archivo .py

1. Abre un editor de texto (Bloc de notas, VS Code, etc.)
2. Escribe: `print("Hola Mundo")`
3. Guarda el archivo como `hola.py`
4. En la terminal, navega a la carpeta donde guardaste el archivo
5. Escribe: `python hola.py`
6. Presiona Enter

```bash
$ python hola.py
Hola Mundo
```

---

## 6. Errores Comunes de Principiantes ⚠️

### Error 1: Olvidar las comillas

❌ **Incorrecto:**
```python
print(Hola Mundo)
```
✅ **Correcto:**
```python
print("Hola Mundo")
```

**Error que verás:** `NameError: name 'Hola' is not defined`

### Error 2: Olvidar los paréntesis

❌ **Incorrecto:**
```python
print "Hola Mundo"
```
✅ **Correcto:**
```python
print("Hola Mundo")
```

**Error que verás:** `SyntaxError: Missing parentheses in call to 'print'`

### Error 3: Comillas mezcladas

❌ **Incorrecto:**
```python
print("Hola Mundo')
```
✅ **Correcto:**
```python
print("Hola Mundo")
# o
print('Hola Mundo')
```

### Error 4: Mayúsculas incorrectas

❌ **Incorrecto:**
```python
Print("Hola Mundo")
PRINT("Hola Mundo")
```
✅ **Correcto:**
```python
print("Hola Mundo")
```

**Python distingue mayúsculas de minúsculas** (es case-sensitive)

---

## 7. Experimenta: Variaciones del Hola Mundo

Prueba estos ejemplos en tu terminal:

```python
# Texto simple
print("Hola")

# Números
print(42)

# Operaciones matemáticas
print(2 + 3)

# Múltiples valores separados por coma
print("Hola", "Mundo")

# Texto vacío
print("")

# Sin argumentos (solo salta línea)
print()
```

**Resultado esperado:**
```
Hola
42
5
Hola Mundo


```

---

## 8. ¿Qué pasa realmente cuando ejecutas código? 🤔

Cuando escribes `print("Hola Mundo")` y presionas Enter:

```
1. Tú escribes: print("Hola Mundo")
        ↓
2. Python lee tu código
        ↓
3. Python verifica sintaxis (¿está bien escrito?)
        ↓
4. Python traduce a lenguaje máquina
        ↓
5. La computadora ejecuta
        ↓
6. Resultado aparece en pantalla: Hola Mundo
```

Este proceso se llama **interpretación**. Python es un lenguaje **interpretado**, lo que significa que traduce línea por línea en tiempo real.

---

## 9. Resumen de Conceptos Clave 📝

| Término | Definición | Ejemplo |
|---------|------------|---------|
| **Lenguaje de programación** | Forma de dar instrucciones a la computadora | Python, Java, JavaScript |
| **Código** | Conjunto de instrucciones escritas | `print("Hola")` |
| **Programa** | Código que realiza una tarea | Un script .py |
| **Ejecutar** | Correr/hacer funcionar el código | `python archivo.py` |
| **Terminal/Consola** | Interfaz de texto para comandos | PowerShell, bash |
| **Función** | Bloque de código que hace algo específico | `print()` |
| **String** | Texto entre comillas | `"Hola"` |
| **Sintaxis** | Reglas de cómo escribir código correctamente | Usar paréntesis en `print()` |

---

## 10. Ejercicios Prácticos ✍️

### Ejercicio 1: Tu primera línea de código
Escribe un programa que muestre tu nombre en pantalla.

```python
# Escribe tu código aquí
```

<details>
<summary>💡 Ver solución</summary>

```python
print("Tu Nombre")
```
</details>

### Ejercicio 2: Múltiples líneas
Escribe un programa que muestre tres líneas diferentes:
- Tu nombre
- Tu ciudad
- Tu hobby favorito

```python
# Escribe tu código aquí
```

<details>
<summary>💡 Ver solución</summary>

```python
print("Ana García")
print("Madrid")
print("Leer libros")
```
</details>

### Ejercicio 3: Operaciones matemáticas
Escribe un programa que muestre el resultado de:
- Sumar 15 + 27
- Restar 100 - 45
- Multiplicar 8 × 7

```python
# Escribe tu código aquí
```

<details>
<summary>💡 Ver solución</summary>

```python
print(15 + 27)
print(100 - 45)
print(8 * 7)
```
</details>

### Ejercicio 4: Combinando texto y números
Escribe un programa que muestre:
```
Mi edad es: 25
```
Pero usando una operación: `print("Mi edad es:", 20 + 5)`

```python
# Escribe tu código aquí
```

<details>
<summary>💡 Ver solución</summary>

```python
print("Mi edad es:", 20 + 5)
```
</details>

### Ejercicio 5: Dibujo con texto
Usa prints para dibujar un triángulo:
```
*
**
***
****
```

```python
# Escribe tu código aquí
```

<details>
<summary>💡 Ver solución</summary>

```python
print("*")
print("**")
print("***")
print("****")
```
</details>

---

## 11. Desafío Final 🏆

Crea un programa que muestre exactamente esto:

```
===============================
       ¡Bienvenido a Python!
===============================
Nombre: [Tu nombre]
Ciudad: [Tu ciudad]
Edad: [Tu edad]
===============================
```

<details>
<summary>💡 Ver solución completa</summary>

```python
print("===============================")
print("       ¡Bienvenido a Python!")
print("===============================")
print("Nombre: Ana García")
print("Ciudad: Madrid")
print("Edad: 25")
print("===============================")
```
</details>

---

## 12. Autoevaluación ✅

Responde estas preguntas (sin mirar arriba):

1. ¿Qué función usamos para mostrar texto en pantalla?
2. ¿Son obligatorios los paréntesis en `print()`?
3. ¿Qué pasa si olvidas las comillas en un texto?
4. ¿Python distingue entre `Print()` y `print()`?
5. ¿Qué símbolo usamos para comentarios en Python?

<details>
<summary>📋 Ver respuestas</summary>

1. `print()`
2. Sí, siempre son obligatorios
3. Obtendrás un `NameError`
4. Sí, Python distingue mayúsculas/minúsculas
5. El numeral/hash: `#`
</details>

---

## 13. Glosario de Términos 📖

- **Argumento**: Valor que le pasas a una función
- **Built-in**: Funciones que vienen incluidas en Python
- **Case-sensitive**: Distingue entre mayúsculas y minúsculas
- **Comentario**: Texto ignorado por Python, usado para notas
- **Consola/Terminal**: Interfaz de texto para comandos
- **Ejecutar**: Correr/hacer funcionar un programa
- **Función**: Bloque de código reutilizable
- **Interpretado**: Se ejecuta línea por línea
- **Prompt**: Símbolo que indica que la terminal espera input (`>>>`)
- **Sintaxis**: Reglas gramaticales del lenguaje
- **String**: Cadena de texto entre comillas

---

## ➡️ Próxima Lección

En la **Lección 02** aprenderás sobre:
- Variables (las cajas donde guardamos información)
- Tipos de datos (str, int, float, bool)
- Cómo convertir entre tipos
- La función `type()` y `isinstance()`

¡Felicidades! Has completado tu primera lección de Python 🎉
