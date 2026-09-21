# Lección 11 · Módulos y paquetes

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion11-modulos-paquetes/practica.ipynb)

## 🎯 Objetivos

- Organizar código en módulos (archivos `.py`)
- Importar de todas las formas correctas
- Entender `if __name__ == "__main__":`
- Instalar librerías con `pip`
- Estructurar un proyecto como un profesional

---

## 1. ¿Qué es un módulo?

Un módulo es simplemente **un archivo `.py`** con código reutilizable (funciones, clases, constantes). Cuando tus programas crecen, meter todo en un archivo se vuelve inmanejable: se divide en módulos por tema.

Ya has usado módulos: `math`, `random`, `csv`, `json` son módulos de la **librería estándar** (vienen con Python).

```python
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.14159...
```

## 2. Formas de importar

```python
import math                  # módulo completo: math.sqrt(2)
import math as m             # con alias: m.sqrt(2)
from math import sqrt, pi    # solo lo que necesitas: sqrt(2)
from math import *           # ⚠️ EVITAR: contamina el espacio de nombres
```

Reglas de estilo:

- Prefiere `import math` o `from math import sqrt`: siempre queda claro de dónde sale cada cosa.
- Nunca `from x import *` en código serio: no sabes qué nombres estás pisando.
- Los imports van **arriba del todo** del archivo, uno por línea.

## 3. Crear tus propios módulos

Imagina dos archivos en la misma carpeta:

```python
# archivo: geometria.py
def area_circulo(radio):
    return 3.14159265 * radio ** 2

def area_rectangulo(base, altura):
    return base * altura
```

```python
# archivo: main.py
import geometria

print(geometria.area_circulo(2))   # usando TU módulo
```

En Colab puedes crear archivos con el comando mágico `%%writefile nombre.py` en una celda, y luego importarlos (lo practicarás en el notebook).

## 4. `if __name__ == "__main__":`

Este bloque es confuso al principio pero es fundamental:

```python
# geometria.py
def area_circulo(radio):
    return 3.14159265 * radio ** 2

if __name__ == "__main__":
    # esto solo se ejecuta si corres ESTE archivo directamente,
    # no cuando otro archivo lo importa
    print("Autotest:", area_circulo(1))
```

Cuando Python ejecuta un archivo, crea la variable especial `__name__`:

- Si ejecutas el archivo directamente → `__name__` vale `"__main__"`.
- Si otro archivo lo **importa** → `__name__` vale el nombre del módulo (`"geometria"`).

Uso práctico: pones ahí tests y demos. Quien importe tu módulo no ejecutará esas pruebas. Todo script profesional termina así:

```python
def main():
    ...  # lógica del programa

if __name__ == "__main__":
    main()
```

## 5. pip: instalar librerías de terceros

La librería estándar cubre lo básico, pero el ecosistema de Python tiene +400.000 paquetes en [PyPI](https://pypi.org). Se instalan con `pip`:

```bash
pip install requests          # en una terminal normal
```

En Colab, con `!` delante:

```python
!pip install requests
import requests
```

En Colab la mayoría de librerías populares (numpy, pandas, matplotlib, requests…) ya vienen instaladas.

## 6. Paquetes: carpetas de módulos

Un **paquete** es una carpeta con módulos y un archivo `__init__.py` (puede estar vacío):

```
mi_proyecto/
├── main.py
└── utilidades/
    ├── __init__.py
    ├── matematicas.py
    └── texto.py
```

```python
from utilidades.matematicas import area_circulo
```

## 7. Estructura profesional y entornos virtuales

Un proyecto real suele tener esta pinta:

```
mi_proyecto/
├── README.md           # qué hace el proyecto y cómo usarlo
├── requirements.txt    # librerías necesarias (se genera: pip freeze > requirements.txt)
├── main.py             # punto de entrada
├── src/ o paquete/     # el código organizado en módulos
└── tests/              # pruebas automáticas
```

Y en tu ordenador se trabaja con **entornos virtuales** (`python -m venv venv`): una burbuja por proyecto con sus propias librerías y versiones, para que los proyectos no se rompan entre sí. En Colab no hace falta, pero en tu PC es la práctica estándar — lo usarás en la universidad.

---

## ⚠️ Errores típicos

1. Llamar a tu archivo como una librería (`random.py`, `math.py`): rompe los imports reales.
2. `from modulo import *`: pierdes el control de qué nombres existen.
3. Ejecutar código suelto en el módulo (fuera del `if __name__`): cualquiera que lo importe ejecutará ese código sin querer.
4. `ModuleNotFoundError`: el archivo no está en la misma carpeta o mal nombre (sensible a mayúsculas).

## 📝 Resumen

- Módulo = archivo `.py`; paquete = carpeta con `__init__.py`.
- `import modulo` / `from modulo import nombre`; nunca `import *`.
- `if __name__ == "__main__":` separa el código de «script» del código reutilizable.
- `pip install` añade paquetes de PyPI; en Colab con `!pip`.
- Proyectos serios: README, requirements.txt, código en módulos, tests.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion11-modulos-paquetes/practica.ipynb)

## ➡️ Siguiente paso

[Lección 12 · Proyectos finales](../leccion12-proyectos-finales/)
