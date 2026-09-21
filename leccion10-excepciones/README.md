# Lección 10 · Excepciones

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion10-excepciones/practica.ipynb)

## 🎯 Objetivos

- Entender qué es una excepción y por qué existen
- Capturar errores con `try` / `except` / `else` / `finally`
- Lanzar tus propios errores con `raise`
- Diseñar programas robustos que no se rompen con el usuario

---

## 1. ¿Qué es una excepción?

Cuando Python no puede ejecutar algo, **lanza una excepción**: un objeto-error que, si nadie lo captura, detiene el programa mostrando un *traceback* (el texto rojo que ya conoces):

```python
int("hola")        # ValueError: texto no convertible a número
[1, 2][5]          # IndexError: índice fuera de rango
{"a": 1}["b"]      # KeyError: clave inexistente
10 / 0             # ZeroDivisionError
open("nada.txt")   # FileNotFoundError
```

Una excepción sin capturar **mata el programa entero**. Un ingeniero escribe programas que sobreviven a los errores previsibles.

## 2. `try` / `except`: capturar errores

```python
try:
    edad = int(input("Edad: "))     # código arriesgado
except ValueError:                   # si salta ValueError...
    print("Eso no era un número")    # ...se ejecuta esto y el programa SIGUE
print("El programa continúa")
```

Cómo funciona:

1. Python ejecuta el bloque `try`.
2. Si todo va bien, se salta el `except`.
3. Si salta una excepción del tipo indicado, salta directamente al `except` correspondiente.
4. Puedes capturar varios tipos distintos con varios `except`.

```python
try:
    n = int(input("Número: "))
    print(100 / n)
except ValueError:
    print("No era un número")
except ZeroDivisionError:
    print("No puedo dividir entre cero")
```

Puedes capturar el objeto-error con `as` para ver el mensaje:

```python
try:
    open("no_existe.txt")
except FileNotFoundError as e:
    print(f"Archivo no encontrado: {e}")
```

## 3. Reglas de oro de las excepciones

- **Captura lo específico, nunca todo**: un `except:` pelado (sin tipo) traga errores que no esperabas y convierte bugs en misterios. Pon siempre el tipo: `except ValueError:`.
- **`try` pequeño**: mete dentro solo la línea arriesgada. Si metes 50 líneas, no sabrás qué falló.
- **Mejor prevenir con lógica cuando se puede**: si puedes comprobar `if os.path.exists(...)`, hazlo; usa excepciones para lo realmente impredecible (input del usuario, red, archivos que otro proceso toca).

## 4. `else` y `finally`

```python
try:
    n = int(input("Número: "))
except ValueError:
    print("Error de formato")
else:
    print(f"Gracias, diste el número {n}")   # solo si NO hubo excepción
finally:
    print("Esto se ejecuta SIEMPRE")          # haya error o no
```

- `else`: código que solo corre si el `try` tuvo éxito.
- `finally`: limpieza que corre siempre (cerrar conexiones, registrar logs…). Con archivos ya lo hace `with`, pero con redes o bases de datos lo usarás.

## 5. `raise`: lanzar tus propios errores

Cuando tu función detecta un estado ilegal, puede lanzar una excepción en vez de devolver un valor trampa:

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    return a / b

try:
    dividir(10, 0)
except ValueError as e:
    print(f"Error controlado: {e}")
```

Esto separa dos responsabilidades: **quien detecta el problema lo señala** (`raise`), y **quien tiene contexto para decidir qué hacer lo captura** (`try`). Así funcionan todas las librerías serias.

## 6. Excepciones personalizadas

Para proyectos grandes puedes crear tus propios tipos heredando de `Exception`:

```python
class SaldoInsuficienteError(Exception):
    """Se lanza cuando se intenta retirar más dinero del disponible."""

class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(f"Faltan {cantidad - self.saldo} €")
        self.saldo -= cantidad
```

Ventaja: quien usa tu código puede capturar **exactamente** ese error sin confundirlo con otros.

## 7. Validación robusta de entrada: el patrón definitivo

```python
while True:
    try:
        edad = int(input("Tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera de rango")
        break                      # solo sale del bucle si todo fue válido
    except ValueError as e:
        print(f"Entrada no válida ({e}). Inténtalo de nuevo.")

print(f"Edad registrada: {edad}")
```

Este patrón (bucle + try + validación + break) es literalmente cómo se piden datos en programas profesionales.

---

## ⚠️ Errores típicos

1. `except:` sin tipo: oculta bugs. Especifica siempre.
2. Capturar la excepción y no hacer nada (`except ValueError: pass`): el error desaparece en silencio. Como mínimo, infórmalo.
3. Meter todo el programa dentro de un solo `try` gigante.
4. Usar excepciones para flujo normal del programa (son para lo **excepcional**, no para sustituir a los `if`).

## 📝 Resumen

- Las excepciones sin capturar detienen el programa; `try/except` las gestiona.
- Captura tipos específicos; `else` corre si todo fue bien; `finally` corre siempre.
- `raise` lanza errores propios; puedes crear tus propias clases de error.
- Programa robusto = valida entradas, captura lo impredecible, nunca traga errores en silencio.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion10-excepciones/practica.ipynb)

## ➡️ Siguiente paso

[Lección 11 · Módulos y paquetes](../leccion11-modulos-paquetes/)
