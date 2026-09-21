# Lección 15 · La librería estándar

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion15-modulos-estandar/practica.ipynb)

## 🎯 Objetivos

- Conocer los módulos estándar que más se usan en la vida real
- Trabajar con fechas y horas (`datetime`)
- Buscar patrones en texto con expresiones regulares (`re`)
- Generar aleatoriedad reproducible (`random`)
- Usar herramientas de iteración profesionales (`itertools`, `functools`)

Python presume de «baterías incluidas»: casi todo lo común ya está hecho y probado. Un buen programador no reinventa la rueda — conoce su librería estándar.

---

## 1. `math` y `random`

```python
import math, random

math.sqrt(2), math.pi, math.ceil(4.2), math.floor(4.8), math.gcd(12, 18)  # 1.414..., 3.1415..., 5, 4, 6

random.randint(1, 6)          # entero aleatorio en [1, 6]
random.choice(["a", "b"])     # elemento aleatorio
random.shuffle(lista)         # baraja la lista (la modifica)
random.sample(range(50), 6)   # 6 números distintos (tipo lotería)
random.seed(42)               # fija la semilla: misma secuencia siempre (¡clave para testear!)
```

⚠️ `random` no sirve para seguridad (contraseñas, tokens). Para eso existe el módulo `secrets`.

## 2. `datetime`: fechas y horas

```python
from datetime import date, datetime, timedelta

hoy = date.today()
fin_curso = date(2027, 6, 20)
print((fin_curso - hoy).days, "días hasta fin de curso")

ahora = datetime.now()
print(ahora.strftime("%d/%m/%Y %H:%M"))     # formatear: 21/09/2026 18:30

fecha = datetime.strptime("15/08/2026", "%d/%m/%m")  # texto → fecha
```

Códigos de formato útiles: `%d` día, `%m` mes, `%Y` año, `%H` hora, `%M` minuto. Y `timedelta(days=7)` suma/resta tiempo sin errores de calendario.

## 3. `re`: expresiones regulares

Las regex definen **patrones de texto**. Imprescindibles para validar y extraer datos:

```python
import re

re.fullmatch(r"\d{8}[A-Z]", "12345678A")     # valida formato DNI: 8 dígitos + letra
re.findall(r"\d+", "tengo 3 gatos y 12 peces")  # ['3', '12']
re.sub(r"\s+", " ", "demasiados    espacios")    # 'demasiados espacios'
```

Mini-guía de símbolos:

| Símbolo | Significa |
|---------|-----------|
| `\d` | un dígito (0-9) |
| `\w` | letra, dígito o `_` |
| `\s` | espacio en blanco |
| `.` | cualquier carácter |
| `+` , `*` | 1 o más / 0 o más |
| `{n}` , `{n,m}` | exactamente n / entre n y m |
| `[abc]` , `[^abc]` | uno de / ninguno de |
| `^` , `$` | principio / fin del texto |

La `r"..."` (raw string) evita problemas con las barras: úsala siempre en regex.

## 4. `collections` e `itertools`: iteración profesional

Ya viste `Counter`, `defaultdict` y `deque` (lección 13). `itertools` es la navaja suiza de los bucles:

```python
from itertools import combinations, permutations, cycle, islice

list(combinations("ABC", 2))    # [('A','B'), ('A','C'), ('B','C')]  — sin orden ni repetición
list(permutations("AB"))        # [('A','B'), ('B','A')]             — el orden importa

# islice corta iteradores infinitos:
naturales = cycle([1, 2, 3])
list(islice(naturales, 7))       # [1, 2, 3, 1, 2, 3, 1]
```

Y `functools.reduce` acumula (aunque normalmente un bucle es más legible):

```python
from functools import reduce
reduce(lambda a, b: a * b, [1, 2, 3, 4])   # 24 (factorial de 4)
```

## 5. Otros que debes conocer de nombre

| Módulo | Para qué |
|--------|----------|
| `os` / `sys` | Sistema operativo, argumentos de línea de comandos |
| `string` | Constantes útiles: `string.ascii_lowercase`, `string.digits`… |
| `statistics` | `mean`, `median`, `stdev` |
| `time` | Medir tiempos, pausas (`time.sleep`) |
| `textwrap` / `pprint` | Formatear texto y estructuras de datos bonitas |

## 6. Cómo descubrir lo que necesitas

Cuando pienses «seguro que Python ya hace esto», es verdad el 90% de las veces. Consulta la [documentación oficial](https://docs.python.org/es/3/library/) o inspecciona en vivo:

```python
import string
dir(string)          # lista todo lo que tiene el módulo
help(string.ascii_lowercase)
```

---

## ⚠️ Errores típicos

1. Poner la clase en vez de la instancia: `date.today()` ✅ vs `datetime.today()` ❌ (es `datetime.now()`).
2. Olvidar que `strftime` formatea y `strptime` parsea (la «p» es de *parse*).
3. Usar `random` para contraseñas reales: usa `secrets`.
4. Regex sin la `r` de raw string: los `\` se interpretan dos veces.

## 📝 Resumen

- `math` y `random` para números y azar (con `seed` reproducible).
- `datetime` para fechas: `strftime` (a texto), `strptime` (desde texto), `timedelta` (aritmética).
- `re` para patrones de texto: `fullmatch`, `findall`, `sub`.
- `itertools` y `functools` llevan los bucles al nivel profesional.
- La documentación oficial + `dir()`/`help()` son tus mejores aliados.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion15-modulos-estandar/practica.ipynb)

## ➡️ Siguiente paso

[Lección 16 · Intro a Data Science](../leccion16-intro-data-science/)
