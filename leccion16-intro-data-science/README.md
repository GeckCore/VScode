# Lección 16 · Introducción a Data Science

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion16-intro-data-science/practica.ipynb)

## 🎯 Objetivos

- Entender qué hacen NumPy, pandas y matplotlib y cuándo usar cada uno
- Operar con arrays y tablas de datos reales
- Crear tus primeras gráficas
- Hacer un mini-análisis de datos de principio a fin

Esta lección es tu puerta de entrada al mundo de los datos (y a la IA): todo lo que hace un modelo de machine learning empieza por datos manipulados con estas tres librerías. En Colab ya vienen instaladas.

---

## 1. NumPy: matemáticas a velocidad de vértigo

`numpy` trabaja con **arrays**: parecen listas, pero las operaciones se aplican a todos los elementos a la vez (vectorización) y van decenas de veces más rápido que los bucles de Python:

```python
import numpy as np

notas = np.array([5.0, 7.5, 8.0, 4.5])
print(notas + 1)              # [6.  8.5 9.  5.5] — suma a TODOS (¡con listas esto no funciona!)
print(notas.mean())           # 6.25
print(notas.max(), notas.std())
print(notas[notas >= 5])      # filtrado elegante: [5.  7.5 8. ]

np.arange(0, 10, 2)           # array([0, 2, 4, 6, 8]) — como range pero array
np.linspace(0, 1, 5)          # array([0, 0.25, 0.5, 0.75, 1]) — 5 puntos equiespaciados
```

La diferencia clave con una lista: `lista * 2` duplica la lista (`[1,2,1,2]`); `array * 2` multiplica cada número (`[2,4]`). NumPy piensa en matemáticas.

## 2. pandas: Excel con superpoderes

`pandas` trabaja con **DataFrames**: tablas con filas y columnas etiquetadas. Es la herramienta estándar mundial para análisis de datos.

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Bea"],
    "nota": [8.5, 6.0, 9.0],
    "aprobado": [True, True, True]
})

df                        # la tabla completa
df["nota"]                # una columna (una Serie)
df["nota"].mean()         # 7.83...
df[df["nota"] >= 7]       # filtrar filas: Ana y Bea
df["nota_con_bonus"] = df["nota"] + 0.5   # nueva columna calculada
df.sort_values("nota", ascending=False)   # ordenar
df.describe()             # resumen estadístico automático
```

Y leer archivos reales es una línea:

```python
df = pd.read_csv("datos.csv")          # archivos locales
df = pd.read_csv("https://url/archivo.csv")  # ¡incluso desde Internet directamente!
df.head()              # primeras 5 filas
df.groupby("ciudad")["ventas"].sum()   # agregaciones por grupo
```

## 3. matplotlib: ver los datos

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])   # línea
plt.title("Cuadrados")
plt.xlabel("x"); plt.ylabel("x²")
plt.show()
```

Tipos básicos: `plt.plot` (líneas), `plt.bar` (barras), `plt.scatter` (dispersión, relación entre variables), `plt.hist` (histograma, distribución). En pandas puedes graficar directo: `df["nota"].hist()`.

## 4. El flujo completo de un análisis

Todo análisis de datos (y toda práctica de universidad de esta materia) sigue este circuito:

1. **Cargar**: `pd.read_csv(...)`
2. **Explorar**: `head()`, `describe()`, `info()` — mira los datos antes de tocarlos
3. **Limpiar**: nulos (`dropna`, `fillna`), tipos, duplicados
4. **Analizar**: filtros, `groupby`, columnas calculadas
5. **Visualizar**: una gráfica vale más que 1000 números
6. **Concluir**: escribe qué has descubierto (¡una conclusión sin datos no vale nada!)

## 5. ¿Y después de esto?

Este curso te deja en el punto de partida de:

- **Asignaturas de programación** de cualquier grado de ingeniería: vas cubierto sobrao con las lecciones 1-11.
- **Algoritmia y estructuras de datos**: lecciones 13-14.
- **Data Science / IA**: esta lección es el prólogo; continúa con pandas a fondo y luego scikit-learn.

---

## ⚠️ Errores típicos

1. Tratar un array de NumPy como lista: `array * 2` multiplica, no duplica.
2. Comparaciones lógicas en pandas: se usa `&` y `|` (con paréntesis), no `and`/`or`: `df[(df.a > 1) & (df.b < 3)]`.
3. Modificar una vista: usa `df.copy()` si vas a tocar una tabla filtrada (el famoso `SettingWithCopyWarning`).
4. Olvidar `plt.show()` o mezclar varias gráficas sin limpiar con `plt.figure()`.

## 📝 Resumen

- NumPy = arrays vectorizados rápidos; pandas = tablas etiquetadas; matplotlib = gráficas.
- Filtra con corchetes booleanos, agrega con `groupby`, explora con `describe()`.
- Flujo: cargar → explorar → limpiar → analizar → visualizar → concluir.

## 🏋️ Práctica

El notebook contiene un mini-proyecto completo de análisis con datos reales.

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion16-intro-data-science/practica.ipynb)

## 🎓 ¡Fin del curso!

Has llegado al final. Repasa los proyectos de la lección 12 con lo que sabes ahora: notarás lo mucho que has crecido como programador.
