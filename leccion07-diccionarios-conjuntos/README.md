# Lección 7 · Diccionarios y conjuntos

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion07-diccionarios-conjuntos/practica.ipynb)

## 🎯 Objetivos

- Crear y usar diccionarios (clave → valor)
- Recorrer diccionarios y gestionar claves ausentes
- Modelar datos reales con diccionarios anidados
- Usar conjuntos para eliminar duplicados y hacer operaciones matemáticas

---

## 1. ¿Qué es un diccionario?

Un diccionario guarda pares **clave → valor**. Como un diccionario real: buscas una palabra (clave) y obtienes su definición (valor). Se escribe con llaves `{}`:

```python
alumno = {"nombre": "Ana", "edad": 18, "carrera": "Informática"}

print(alumno["nombre"])     # Ana   (se accede por CLAVE, no por posición)
print(alumno["edad"])       # 18
```

- Las **claves** son únicas y suelen ser texto (o números).
- Los **valores** pueden ser cualquier cosa: números, texto, listas, otros diccionarios…

¿Cuándo diccionario y cuándo lista? Lista = colección de cosas del mismo tipo ordenadas por posición. Diccionario = datos con **etiquetas significativas** o búsquedas rápidas por clave.

## 2. Añadir, modificar y borrar

```python
alumno["nota"] = 8.5         # añade (o modifica si ya existe)
alumno["edad"] = 19          # modifica
del alumno["carrera"]        # borra la clave
print(len(alumno))           # 3 pares
```

⚠️ Acceder a una clave que no existe lanza `KeyError`. Dos soluciones:

```python
# opción 1: .get() devuelve un valor por defecto si no existe
print(alumno.get("telefono", "sin teléfono"))   # sin teléfono

# opción 2: comprobar antes con in
if "telefono" in alumno:
    print(alumno["telefono"])
```

## 3. Recorrer diccionarios

```python
capitales = {"España": "Madrid", "Francia": "París", "Italia": "Roma"}

for pais in capitales:                    # recorre las claves
    print(pais)

for pais, capital in capitales.items():   # clave y valor a la vez (lo más usado)
    print(f"La capital de {pais} es {capital}")

print(list(capitales.keys()))    # ['España', 'Francia', 'Italia']
print(list(capitales.values()))  # ['Madrid', 'París', 'Roma']
```

## 4. El patrón contador con diccionarios

Contar cosas es **el** uso estrella de los diccionarios:

```python
votos = ["ana", "luis", "ana", "bea", "ana", "luis"]
contador = {}
for nombre in votos:
    contador[nombre] = contador.get(nombre, 0) + 1

print(contador)   # {'ana': 3, 'luis': 2, 'bea': 1}
```

`contador.get(nombre, 0)` significa: «dame el total actual de este nombre, y si aún no existe, empieza en 0». Memoriza este patrón: aparece en exámenes, entrevistas y programas reales.

## 5. Diccionarios anidados: modelar datos reales

```python
clase = {
    "Ana": {"edad": 18, "notas": [7, 8, 9]},
    "Luis": {"edad": 19, "notas": [5, 6]}
}

print(clase["Ana"]["notas"][1])   # 8 (nota 2 de Ana)
```

Se lee por pasos: `clase["Ana"]` es el diccionario de Ana; `["notas"]` su lista de notas; `[1]` la segunda nota. Así se estructuran los datos en el mundo real (un JSON de una API tiene exactamente esta pinta — lección 9).

## 6. Conjuntos (sets)

Un `set` es una colección **sin duplicados y sin orden garantizado**:

```python
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)          # {1, 2, 3}  ← los duplicados desaparecen

lista = [1, 2, 2, 3]
unicos = list(set(lista))   # truco clásico para quitar duplicados: [1, 2, 3]
```

Operaciones de teoría de conjuntos:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b     # unión:        {1, 2, 3, 4, 5, 6}
a & b     # intersección: {3, 4}
a - b     # diferencia:   {1, 2}
3 in a    # True (búsqueda rapidísima)
```

Usa sets cuando te importe la **pertenencia** («¿está este elemento?») y la **unicidad**, no el orden.

---

## ⚠️ Errores típicos

1. `dicc["clave_inexistente"]` → `KeyError`. Usa `.get()` si no estás seguro.
2. Creer que `{1, 2, 3}` es un diccionario: con `:` es diccionario, sin `:` es set. `{}` vacío es diccionario (un set vacío se crea con `set()`).
3. Intentar usar una lista como clave: las claves deben ser inmutables (texto, números, tuplas).
4. Modificar un diccionario mientras lo recorres → errores. Recorre una copia: `for k in list(d)`.

## 📝 Resumen

- Diccionario: pares clave → valor; acceso por clave, `KeyError` si no existe, `.get(clave, defecto)` evita el error.
- Recorre con `.items()`; `.keys()` y `.values()` dan listas de claves/valores.
- Patrón contador: `d[k] = d.get(k, 0) + 1`.
- Set: sin duplicados; unión `|`, intersección `&`, diferencia `-`.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion07-diccionarios-conjuntos/practica.ipynb)

## ➡️ Siguiente paso

[Lección 8 · Programación Orientada a Objetos](../leccion08-programacion-orientada-objetos/)
