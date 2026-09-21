# 📖 Guía rápida: Google Colab (sin instalar nada)

Google Colab es un entorno de Python que funciona **100% en el navegador**. No descargas el repo, no instalas Python, no montas servidores. Solo necesitas una cuenta de Google (gratis).

## ¿Cómo abro una práctica?

1. Entra en la carpeta de la lección en GitHub.
2. Pulsa el botón **«Abrir en Colab»** del README, o abre el archivo `practica.ipynb` y añade la URL en [colab.research.google.com](https://colab.research.google.com) → pestaña **GitHub**.
3. Se abrirá el notebook con el Python de esta lección listo para usar.

## ¿Cómo se usa un notebook?

Un notebook es una lista de **celdas**. Hay dos tipos:

- **Celdas de texto (Markdown)**: explicaciones. Solo léelas.
- **Celdas de código**: las ejecutas con **Shift + Enter** o con el botón ▶️ que aparece a la izquierda de la celda.

### Reglas de oro

1. **Ejecuta las celdas en orden, de arriba abajo.** Python recuerda lo que has ejecutado; si te saltas una celda, las siguientes pueden fallar.
2. Si algo se descontrola, usa el menú **Entorno de ejecución → Reiniciar y ejecutar todo**. Eso limpia la memoria y ejecuta todo de nuevo desde el principio.
3. Las celdas de ejercicio tienen líneas como esta:

```python
resultado = None   # ← Cambia esto por tu respuesta

assert resultado == 42   # ← Esto corrige tu ejercicio automáticamente
print("✅ ¡Correcto!")
```

- Si tu respuesta es correcta, verás el ✅.
- Si es incorrecta, verás un `AssertionError`: es la forma en que el ejercicio te dice «todavía no».

## ¿Se guarda mi progreso?

Colab guarda en tu Google Drive una copia si le das a **Archivo → Guardar una copia en Drive**. Si cierras la pestaña sin guardar, perderás tus cambios del notebook (el original en GitHub nunca se modifica).

## Atajos útiles

| Atajo | Qué hace |
|-------|----------|
| `Shift + Enter` | Ejecutar celda y bajar a la siguiente |
| `Ctrl + Enter` | Ejecutar celda sin moverse |
| `Ctrl + M, B` | Insertar celda debajo |
| `Ctrl + M, M` | Convertir celda a texto |
| `Ctrl + M, K` | Convertir celda a código |

## Alternativas (opcional)

- **vscode.dev / github.dev**: pulsa la tecla `.` en la página del repo y se abre un editor en el navegador (sirve para leer/editar archivos, no para ejecutar notebooks).
- **GitHub Codespaces**: entorno de desarrollo completo en la nube (botón verde «Code → Codespaces»). Tiene horas gratis al mes. No es necesario para este curso.
