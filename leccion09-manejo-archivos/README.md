# Lección 9 · Manejo de archivos

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion09-manejo-archivos/practica.ipynb)

## 🎯 Objetivos

- Leer y escribir archivos de texto de forma segura
- Entender por qué `with` es obligatorio en la práctica profesional
- Trabajar con CSV y JSON
- Manejar rutas con `pathlib`
- Persistir datos entre ejecuciones de tus programas

---

## 1. ¿Por qué guardar en archivos?

Todo lo que hace tu programa vive en la memoria RAM: cuando termina, desaparece. Los **archivos** son la forma de que los datos sobrevivan: agendas, partidas guardadas, registros, configuraciones… Esto se llama **persistencia**.

En Colab los archivos se guardan en una máquina temporal de Google, perfecta para practicar (se borra al cerrar, pero para aprender no importa).

## 2. Escribir y leer texto: la forma correcta (`with`)

```python
# ESCRIBIR (o sobrescribir si existe)
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")

# LEER todo el contenido
with open("notas.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
print(contenido)
```

Piezas importantes:

- **`with ... as f:`** abre el archivo y lo **cierra automáticamente** al salir del bloque, incluso si hay un error. Olvidar cerrar archivos corrompe datos y fuga recursos: usa siempre `with`.
- **Modos**: `"r"` leer (error si no existe), `"w"` escribir (⚠️ borra lo anterior), `"a"` añadir al final.
- **`encoding="utf-8"`**: hazlo siempre. Sin esto, las tildes y eñes pueden romperse al mover archivos entre sistemas.

Leer línea a línea (para archivos grandes):

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())   # strip() quita el \n del final
```

O cargar todas las líneas en una lista: `lineas = f.readlines()`.

## 3. CSV: datos en tabla

CSV (comma-separated values) es el formato universal de las hojas de cálculo. El módulo `csv` te lo da hecho:

```python
import csv

with open("notas.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["alumno", "nota"])    # cabecera
    escritor.writerow(["Ana", 8.5])
    escritor.writerow(["Luis", 6.0])

with open("notas.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)              # cada fila como diccionario
    for fila in lector:
        print(fila["alumno"], "->", fila["nota"])
```

⚠️ Todo lo que lees de un CSV llega como **texto**: convierte con `float()`/`int()` si vas a calcular.

## 4. JSON: el formato de Internet

JSON (JavaScript Object Notation) es cómo se intercambian datos las apps y las APIs. Es casi idéntico a los diccionarios de Python:

```python
import json

datos = {"jugador": "Ana", "nivel": 5, "inventario": ["espada", "escudo"]}

# guardar
with open("partida.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

# cargar
with open("partida.json", "r", encoding="utf-8") as f:
    cargado = json.load(f)
print(cargado["inventario"])   # ['espada', 'escudo']
```

- `indent=2` deja el archivo legible para humanos.
- `ensure_ascii=False` mantiene las tildes y eñes tal cual.
- También existen `json.dumps()` / `json.loads()` para convertir a/desde texto (sin archivo).

## 5. Rutas con `pathlib`

El módulo moderno para manejar rutas de archivos (mejor que concatenar strings):

```python
from pathlib import Path

carpeta = Path("datos")
carpeta.mkdir(exist_ok=True)      # crea la carpeta si no existe
archivo = carpeta / "registro.txt"  # el operador / une rutas

archivo.write_text("Hola", encoding="utf-8")    # escribe directo
print(archivo.read_text(encoding="utf-8"))       # lee directo
print(archivo.exists())                          # True
```

`Path` funciona igual en Windows, Linux y macOS. Es la forma recomendada hoy día.

---

## ⚠️ Errores típicos

1. Abrir con `open()` sin `with` y olvidar el `close()`.
2. Abrir en modo `"w"` un archivo con datos que querías conservar (se borra todo, usa `"a"` para añadir).
3. Olvidar `encoding="utf-8"` y ver caracteres raros.
4. Calcular con datos de CSV sin convertirlos de texto a número.
5. `FileNotFoundError` por rutas mal escritas: comprueba con `Path(...).exists()`.

## 📝 Resumen

- `with open(...) as f:` abre y cierra seguro; modos `"r"`, `"w"`, `"a"`; siempre `encoding="utf-8"`.
- `csv.DictReader/DictWriter` para tablas; `json.dump/load` para datos estructurados.
- `pathlib.Path` para rutas modernas y multiplataforma.
- Los archivos son persistencia: los datos sobreviven al programa.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion09-manejo-archivos/practica.ipynb)

## ➡️ Siguiente paso

[Lección 10 · Excepciones](../leccion10-excepciones/)
