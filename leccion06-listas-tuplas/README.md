# Lección 06: Listas y Tuplas

## 📖 ¿Qué son las Listas?

Una lista es una colección ordenada y modificable de elementos.

```python
# Crear listas
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", 3.14, True]
vacia = []
```

## 🎯 Operaciones con Listas

### Acceder a elementos
```python
frutas = ["manzana", "banana", "naranja"]

print(frutas[0])     # "manzana" (primer elemento)
print(frutas[-1])    # "naranja" (último elemento)
print(frutas[1:3])   # ["banana", "naranja"] (slicing)
```

### Modificar listas
```python
frutas = ["manzana", "banana", "naranja"]

frutas[0] = "pera"           # Modificar elemento
frutas.append("uva")         # Agregar al final
frutas.insert(1, "kiwi")     # Insertar en posición
frutas.remove("banana")      # Eliminar por valor
ultimo = frutas.pop()        # Eliminar último
del frutas[0]                # Eliminar por índice
```

### Métodos útiles
```python
lista = [3, 1, 4, 1, 5]

lista.count(1)      # 2 (veces que aparece)
lista.index(4)      # 2 (posición)
lista.sort()        # Ordena: [1, 1, 3, 4, 5]
lista.reverse()     # Invierte el orden
len(lista)          # 5 (longitud)
```

## 📚 Tuplas

Las tuplas son como listas pero **inmutables** (no se pueden modificar).

```python
# Crear tuplas
coordenadas = (10, 20)
colores = ("rojo", "verde", "azul")
una_sola = (5,)  # La coma es necesaria
```

## 📝 Ejercicios

1. Crea una lista de 5 números y calcula su suma
2. Invierte una lista sin usar reverse()
3. Filtra solo los números pares de una lista

**Archivos**: `ejercicios/ejercicio_06_*.py`

## ➡️ Siguiente Lección

[Lección 07: Diccionarios y Conjuntos](../leccion07-diccionarios-conjuntos/)
