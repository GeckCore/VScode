# Lección 12 · Proyectos finales (nivel básico-intermedio)

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion12-proyectos-finales/practica.ipynb)

## 🎯 Objetivos

Esta lección no tiene teoría nueva: aquí **integras todo lo aprendido** (lecciones 1-11) en proyectos completos. Es donde de verdad se aprende a programar.

---

## Cómo enfrentarte a un proyecto

Antes de picar código, sigue este método (el mismo que usarás en la universidad y en el trabajo):

1. **Entiende el problema.** Escríbelo con tus palabras. ¿Qué entra? ¿Qué sale?
2. **Descompón.** Divide el proyecto en funciones pequeñas, cada una con una responsabilidad. Empieza por la más fácil.
3. **Hazlo funcionar feo.** Una versión sencilla que funcione vale más que una elegante a medias.
4. **Prueba a romperlo.** Introduce datos raros: textos donde van números, listas vacías, ceros…
5. **Refactoriza.** Cuando funcione, limpia: buenos nombres, funciones cortas, sin código repetido, docstrings.

## Estructura recomendada para cada proyecto

```python
# 1. DATOS / CONSTANTES
ARCHIVO = "datos.json"

# 2. FUNCIONES DE LÓGICA (sin input/print: devuelven valores)
def cargar_datos(): ...
def guardar_datos(datos): ...
def operacion_principal(...): ...

# 3. INTERFAZ DE USUARIO (aquí sí input/print)
def menu(): ...

# 4. PUNTO DE ENTRADA
if __name__ == "__main__":
    menu()
```

## Los proyectos

En el notebook tienes **3 proyectos guiados** (esqueleto con las funciones a completar) y **1 proyecto libre**. Hazlos en este orden:

### 🥉 Proyecto A — Gestor de tareas (To-Do)
- Añadir, listar, completar y borrar tareas
- Persistencia en JSON (lección 9)
- Funciones + diccionarios/listas + excepciones

### 🥈 Proyecto B — Quiz de preguntas
- Preguntas con opciones almacenadas en una lista de diccionarios
- Puntuación y porcentaje de aciertos
- Validación de entradas robusta (lección 10)

### 🥇 Proyecto C — Simulador de inventario de videojuego (POO)
- Clases `Objeto`, `Inventario` y `Jugador`
- Añadir/usar objetos, límite de peso, guardado en JSON
- Demuestra dominio de la lección 8

### 🏆 Proyecto D — Libre
Elige uno: un juego del ahorcado, un conversor de divisas, un generador de contraseñas seguras, o un gestor de gastos. Aplícale el método de los 5 pasos.

## Criterios de «proyecto bien hecho»

| Criterio | Mínimo exigible |
|----------|-----------------|
| Funciona | No se rompe con entradas incorrectas |
| Modular | Funciones cortas con una responsabilidad cada una |
| Persistente | Guarda datos en archivo (JSON) |
| Legible | snake_case, docstrings, código sin repetir |
| Demo | Al ejecutarlo, se entiende qué hace sin leer el código |

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion12-proyectos-finales/practica.ipynb)

## ➡️ Siguiente paso

[Lección 13 · Estructuras de datos](../leccion13-estructuras-datos/)
