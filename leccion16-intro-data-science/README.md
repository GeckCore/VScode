# Lección 16: Introducción a Data Science con Python

## 📖 Introducción

Data Science (Ciencia de Datos) es un campo interdisciplinario que usa métodos científicos para extraer conocimiento de datos. Esta lección introduce las librerías fundamentales:

- **NumPy** - Computación numérica eficiente
- **pandas** - Manipulación y análisis de datos
- **matplotlib** - Visualización de datos

> **Nota**: Estas librerías requieren instalación: `pip install numpy pandas matplotlib`

## 🎯 NumPy - Numerical Python

NumPy proporciona arrays multidimensionales y funciones matemáticas avanzadas.

### Instalación e importación
```bash
pip install numpy
```

```python
import numpy as np
```

### Arrays de NumPy
```python
# Crear arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]

# Array bidimensional (matriz)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz.shape)  # (2, 3) - 2 filas, 3 columnas

# Arrays especiales
ceros = np.zeros((3, 3))        # Matriz 3x3 de ceros
unos = np.ones((2, 4))          # Matriz 2x4 de unos
rango = np.arange(0, 10, 2)     # [0 2 4 6 8]
aleatorio = np.random.rand(3, 3) # Matriz 3x3 aleatoria

# Array de identidad
identidad = np.eye(3)
```

### Operaciones con arrays
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Operaciones elemento a elemento
print(arr1 + arr2)  # [5 7 9]
print(arr1 * arr2)  # [4 10 18]
print(arr1 ** 2)    # [1 4 9]

# Funciones estadísticas
datos = np.array([10, 20, 30, 40, 50])
print(f"Media: {np.mean(datos)}")      # 30.0
print(f"Mediana: {np.median(datos)}")  # 30.0
print(f"Desviación: {np.std(datos)}")  # 14.14...
print(f"Máximo: {np.max(datos)}")      # 50
print(f"Mínimo: {np.min(datos)}")      # 10

# Indexación avanzada
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz[0, 1])     # 2 (fila 0, columna 1)
print(matriz[:, 1])     # [2 5 8] (toda la columna 1)
print(matriz[matriz > 5])  # [6 7 8 9] (filtrado)
```

### Álgebra lineal
```python
# Producto matricial
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
producto = np.dot(A, B)
print(producto)

# Transpuesta
print(A.T)

# Determinante
det = np.linalg.det(A)
print(f"Determinante: {det}")

# Inversa
inversa = np.linalg.inv(A)
print(inversa)
```

## 📚 pandas - Análisis de Datos

pandas proporciona estructuras de datos flexibles para trabajar con datos tabulares.

### Instalación e importación
```bash
pip install pandas
```

```python
import pandas as pd
```

### Series y DataFrames
```python
# Serie (columna unidimensional)
serie = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(serie['b'])  # 2

# DataFrame (tabla bidimensional)
df = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Carlos', 'Ana'],
    'Edad': [25, 30, 35, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'Salario': [30000, 35000, 40000, 32000]
})
print(df)
```

### Lectura de datos
```python
# Desde CSV
df = pd.read_csv('archivo.csv')

# Desde Excel
df = pd.read_excel('archivo.xlsx')

# Desde JSON
df = pd.read_json('archivo.json')

# Desde diccionario
datos = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(datos)
```

### Exploración de datos
```python
# Primeras filas
print(df.head())      # Primeras 5 filas
print(df.head(10))    # Primeras 10 filas

# Últimas filas
print(df.tail())

# Información general
print(df.info())      # Tipos y valores nulos
print(df.describe())  # Estadísticas descriptivas

# Dimensiones
print(df.shape)       # (filas, columnas)
print(df.columns)     # Nombres de columnas
```

### Selección y filtrado
```python
# Seleccionar columnas
print(df['Nombre'])           # Una columna
print(df[['Nombre', 'Edad']]) # Múltiples columnas

# Filtrar filas
mayores_30 = df[df['Edad'] > 30]
madrid = df[df['Ciudad'] == 'Madrid']

# Múltiples condiciones
filtro = df[(df['Edad'] > 25) & (df['Salario'] > 33000)]

# Usando loc y iloc
print(df.loc[0])         # Por etiqueta
print(df.iloc[0])        # Por posición
print(df.loc[0:2, 'Nombre':'Edad'])  # Rango
```

### Operaciones con DataFrames
```python
# Agregar columna
df['Bonus'] = df['Salario'] * 0.1

# Eliminar columna
df_sin_bonus = df.drop('Bonus', axis=1)

# Ordenar
df_ordenado = df.sort_values('Salario', ascending=False)

# Agrupar y agregar
por_ciudad = df.groupby('Ciudad')['Salario'].mean()
print(por_ciudad)

# Múltiples agregaciones
resumen = df.groupby('Ciudad').agg({
    'Salario': ['mean', 'sum', 'count'],
    'Edad': 'mean'
})
```

### Limpieza de datos
```python
# Detectar nulos
print(df.isnull().sum())  # Nulos por columna

# Eliminar nulos
df_limpio = df.dropna()

# Rellenar nulos
df_relleno = df.fillna(0)  # Con cero
df_relleno = df.fillna(df.mean())  # Con media

# Eliminar duplicados
df_sin_duplicados = df.drop_duplicates()

# Renombrar columnas
df_renombrado = df.rename(columns={'Nombre': 'nombre_completo'})
```

## 📊 matplotlib - Visualización

matplotlib es la librería estándar para crear gráficos en Python.

### Instalación e importación
```bash
pip install matplotlib
```

```python
import matplotlib.pyplot as plt
```

### Gráfico de líneas
```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linewidth=2, color='blue')
plt.title('Crecimiento de Ventas')
plt.xlabel('Mes')
plt.ylabel('Ventas (miles €)')
plt.grid(True)
plt.show()
```

### Gráfico de barras
```python
categorias = ['A', 'B', 'C', 'D']
valores = [23, 45, 56, 78]

plt.figure(figsize=(8, 6))
plt.bar(categorias, valores, color=['red', 'green', 'blue', 'orange'])
plt.title('Comparación de Categorías')
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.show()
```

### Histograma
```python
datos = np.random.randn(1000)  # 1000 números aleatorios

plt.figure(figsize=(8, 6))
plt.hist(datos, bins=30, edgecolor='black', alpha=0.7)
plt.title('Distribución de Datos')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()
```

### Gráfico de dispersión (scatter)
```python
x = np.random.rand(50)
y = np.random.rand(50)
colores = np.random.rand(50)
tamanos = 100 * np.random.rand(50)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colores, s=tamanos, alpha=0.6, cmap='viridis')
plt.colorbar(label='Intensidad')
plt.title('Diagrama de Dispersión')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.show()
```

### Múltiples gráficos (subplots)
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico 1
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 0].set_title('Líneas')

# Gráfico 2
axes[0, 1].bar(['A', 'B'], [5, 7])
axes[0, 1].set_title('Barras')

# Gráfico 3
axes[1, 0].hist(np.random.randn(100), bins=20)
axes[1, 0].set_title('Histograma')

# Gráfico 4
axes[1, 1].scatter(range(10), range(10))
axes[1, 1].set_title('Dispersión')

plt.tight_layout()
plt.show()
```

### Guardar gráficos
```python
plt.figure(figsize=(8, 6))
plt.plot([1, 2, 3], [1, 4, 9])
plt.savefig('mi_grafico.png', dpi=300, bbox_inches='tight')
plt.close()
```

## 🎯 Ejemplo Práctico Completo: Análisis de Ventas

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo
np.random.seed(42)
n_registros = 100

df_ventas = pd.DataFrame({
    'fecha': pd.date_range('2024-01-01', periods=n_registros),
    'producto': np.random.choice(['A', 'B', 'C', 'D'], n_registros),
    'categoria': np.random.choice(['Electrónica', 'Ropa', 'Hogar'], n_registros),
    'cantidad': np.random.randint(1, 20, n_registros),
    'precio_unitario': np.random.uniform(10, 500, n_registros).round(2)
})

# Calcular venta total
df_ventas['venta_total'] = df_ventas['cantidad'] * df_ventas['precio_unitario']

# Exploración
print("=== PRIMERAS FILAS ===")
print(df_ventas.head())

print("\n=== ESTADÍSTICAS ===")
print(df_ventas.describe())

# Análisis por producto
ventas_por_producto = df_ventas.groupby('producto')['venta_total'].sum()
print("\n=== VENTAS POR PRODUCTO ===")
print(ventas_por_producto)

# Visualización
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Ventas por producto
axes[0, 0].bar(ventas_por_producto.index, ventas_por_producto.values)
axes[0, 0].set_title('Ventas Totales por Producto')
axes[0, 0].set_xlabel('Producto')
axes[0, 0].set_ylabel('Venta Total (€)')

# 2. Distribución de precios
axes[0, 1].hist(df_ventas['precio_unitario'], bins=20, edgecolor='black')
axes[0, 1].set_title('Distribución de Precios')
axes[0, 1].set_xlabel('Precio (€)')
axes[0, 1].set_ylabel('Frecuencia')

# 3. Ventas por categoría
ventas_por_cat = df_ventas.groupby('categoria')['venta_total'].sum()
axes[1, 0].pie(ventas_por_cat.values, labels=ventas_por_cat.index, autopct='%1.1f%%')
axes[1, 0].set_title('Distribución por Categoría')

# 4. Evolución temporal
ventas_diarias = df_ventas.groupby('fecha')['venta_total'].sum()
axes[1, 1].plot(ventas_diarias.index, ventas_diarias.values, linewidth=2)
axes[1, 1].set_title('Evolución de Ventas Diarias')
axes[1, 1].set_xlabel('Fecha')
axes[1, 1].set_ylabel('Venta Total (€)')
plt.setp(axes[1, 1].xaxis.get_majorticklabels(), rotation=45)

plt.tight_layout()
plt.savefig('analisis_ventas.png', dpi=300)
plt.show()

print("\n=== GRÁFICOS GUARDADOS EN 'analisis_ventas.png' ===")
```

## 📝 Ejercicios

### Ejercicio 16.1: Análisis de temperaturas
Crea un array NumPy con 365 temperaturas aleatorias (media 20°C, desviación 5°C). Calcula:
- Temperatura media anual
- Día más caluroso y más frío
- Número de días above 25°C

### Ejercicio 16.2: Gestor de inventario con pandas
Crea un DataFrame con productos (nombre, categoría, precio, stock). Implementa:
- Filtrar productos con stock < 10
- Calcular valor total del inventario por categoría
- Encontrar el producto más caro y más barato

### Ejercicio 16.3: Dashboard de ventas
Usando matplotlib, crea un dashboard con 4 gráficos mostrando:
- Ventas mensuales (línea)
- Productos más vendidos (barras)
- Distribución de categorías (pie)
- Correlación precio-ventas (scatter)

### Ejercicio 16.4: Limpieza de dataset
Crea un DataFrame con datos "sucios" (nulos, duplicados, tipos incorrectos) y límpialos completamente.

## ✅ Soluciones

Las soluciones están en la carpeta `soluciones/solucion_16_*.py`.

## 🔍 Test de Autoevaluación

1. ¿Qué ventaja tiene un array de NumPy sobre una lista de Python?
2. ¿Cómo seleccionas todas las filas donde una columna es mayor a un valor en pandas?
3. ¿Qué función usas para guardar un gráfico en matplotlib?
4. ¿Cómo calculas la media de una columna en un DataFrame?
5. ¿Qué tipo de gráfico usarías para mostrar la distribución de una variable continua?

## 📚 Recursos Adicionales

- **Documentación oficial NumPy**: https://numpy.org/doc/
- **Documentación pandas**: https://pandas.pydata.org/docs/
- **Documentación matplotlib**: https://matplotlib.org/stable/contents.html
- **Kaggle**: Dataset gratuitos para practicar
- **Coursera/edX**: Cursos especializados en Data Science

## ➡️ ¡Fin del Curso!

Has completado las 16 lecciones del curso. Ahora tienes:

✅ Fundamentos sólidos de Python
✅ Conocimientos de programación avanzada
✅ Introducción a Data Science

**Próximos pasos recomendados:**
1. Practica con proyectos personales
2. Explora librerías especializadas (scikit-learn, seaborn, plotly)
3. Participa en competencias de Kaggle
4. Contribuye a proyectos open source

¡El aprendizaje nunca termina! 🚀
