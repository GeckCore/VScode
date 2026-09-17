# 🎓 Curso Completo de Python - Desde Cero hasta Experto

## 📖 Descripción del Curso

Este es un **curso universitario completo de Python** diseñado especialmente para personas que **nunca han programado**. Cada concepto se explica de forma extremadamente detallada, con ejemplos prácticos, analogías cotidianas y ejercicios progresivos.

### 🎯 ¿Para quién es este curso?

- ✅ Personas que **nunca han programado** en su vida
- ✅ Estudiantes universitarios que necesitan una base sólida
- ✅ Profesionales que quieren cambiar de carrera
- ✅ Cualquier persona curiosa que quiera aprender Python

### 🌟 Características Únicas

1. **Explicaciones ultra-detalladas**: Cada función, cada parámetro, cada concepto se explica como si fueras un niño de 5 años
2. **Ejemplos cotidianos**: Analogías con situaciones de la vida real para entender conceptos abstractos
3. **Ejercicios autocorregibles**: Obtén retroalimentación inmediata sobre tu código
4. **Aplicación de escritorio**: Todo en un programa .exe, sin necesidad de configurar nada
5. **Terminal interactiva**: Practica directamente en la aplicación
6. **Progreso guardado**: Tu avance se guarda automáticamente

---

## 📚 Temario Completo del Curso

### **MÓDULO 1: FUNDAMENTOS ABSOLUTOS** (Para quienes nunca han programado)

#### Lección 1: ¿Qué es Python y cómo funciona?
- ¿Qué es un lenguaje de programación? (explicado con analogías de cocina)
- ¿Por qué Python es especial?
- Historia breve de Python
- Instalación paso a paso (con capturas de pantalla)
- Tu primer programa: "Hola Mundo" explicado línea por línea
- ¿Qué es una terminal/consola?
- Errores comunes de principiantes y cómo solucionarlos

#### Lección 2: Variables - Las Cajas donde Guardamos Información
- ¿Qué es una variable? (analogía: cajas etiquetadas)
- Reglas para nombrar variables (nombres válidos e inválidos)
- Tipos de datos básicos explicados uno por uno:
  - `str` (texto): comillas simples, dobles y triples
  - `int` (enteros): números sin decimales
  - `float` (decimales): punto vs coma decimal
  - `bool` (booleanos): True y False (verdadero/falso)
- La función `type()`: cómo saber qué tipo de dato tienes
- Conversión entre tipos (casting): `int()`, `float()`, `str()`, `bool()`
- Ejemplos prácticos de conversión con casos reales
- Ejercicio: Calculadora de edad
- **NUEVO**: Función `isinstance()` - Cómo verificar el tipo de una variable

#### Lección 3: Operadores - Las Herramientas Matemáticas y Lógicas
- **Operadores aritméticos** (cada uno con múltiples ejemplos):
  - `+` (suma): números y concatenación de texto
  - `-` (resta): solo números
  - `*` (multiplicación): números y repetición de texto
  - `/` (división): siempre devuelve float
  - `//` (división entera): qué es y cuándo usarla
  - `%` (módulo/residuo): explicado con ejemplos de relojes y pares/impares
  - `**` (potencia): elevando números
  - Jerarquía de operaciones (PEMDAS explicado)
  
- **Operadores de comparación** (devuelven True o False):
  - `==` (igual que): ¡ojo! no confundir con `=`
  - `!=` (diferente de)
  - `>` (mayor que), `<` (menor que)
  - `>=` (mayor o igual), `<=` (menor o igual)
  - Comparación de strings (orden alfabético)
  
- **Operadores lógicos** (combinando condiciones):
  - `and` (y): ambas condiciones deben ser verdaderas (tabla de verdad)
  - `or` (o): al menos una condición debe ser verdadera (tabla de verdad)
  - `not` (no): invierte el valor (True→False, False→True)
  - Combinaciones complejas con paréntesis
  - Tablas de verdad explicadas con ejemplos cotidianos
  
- **Operadores de asignación**:
  - `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
  - Cuándo usar cada uno

#### Lección 4: Entrada y Salida - Interactuando con el Usuario
- **La función `print()` explicada al máximo detalle**:
  - Sintaxis básica: `print("texto")`
  - Parámetro `sep`: cómo separar múltiples argumentos (ejemplos con diferentes separadores)
  - Parámetro `end`: qué pasa al final del print (saltos de línea, espacios, etc.)
  - Imprimir múltiples valores separados por comas
  - Formateo básico sin f-strings
  
- **Las f-strings (formatted strings) - EXPLICACIÓN EXTENSA**:
  - ¿Qué son las llaves `{}` dentro de strings?
  - Sintaxis: `f"Hola {variable}"`
  - Insertar variables directamente en el texto
  - Expresiones dentro de las llaves: `{variable + 5}`
  - Formateo de números: `{numero:.2f}` para decimales
  - Alineación y relleno: `{texto:>10}` 
  - Ejemplos prácticos uno por uno
  
- **La función `input()` explicada completamente**:
  - Sintaxis: `input("mensaje opcional")`
  - ¿Qué devuelve siempre? (¡siempre es string!)
  - Cómo mostrar un mensaje al usuario
  - Capturar el valor en una variable
  - Convertir el input a otros tipos: `int(input())`, `float(input())`
  - Errores comunes: olvidar convertir números
  - Múltiples inputs consecutivos
  - Input vacío: ¿qué pasa si el usuario no escribe nada?
  
- **Proyecto práctico**: Formulario de registro completo

#### Lección 5: Funciones Built-in Esenciales (Parte 1)
- `len()`: longitud de strings, listas, etc. (explicado con ejemplos de contar letras)
- `range()`: generar secuencias de números
  - `range(5)` → 0,1,2,3,4
  - `range(2, 7)` → 2,3,4,5,6
  - `range(0, 10, 2)` → 0,2,4,6,8 (paso personalizado)
  - Usos comunes con for loops
- `str.upper()` y `str.lower()`: mayúsculas y minúsculas
- `str.strip()`: eliminar espacios en blanco
- `str.replace()`: reemplazar texto
- `str.split()`: dividir strings en listas
- `str.join()`: unir listas en strings
- Cada método con 3-5 ejemplos prácticos

---

### **MÓDULO 2: ESTRUCTURAS DE CONTROL**

#### Lección 6: Condicionales - Tomando Decisiones
- El statement `if`: sintaxis y explicación línea por línea
- Indentación en Python: ¿por qué es crucial?
- `else`: cuando la condición es falsa
- `elif`: múltiples condiciones (explained with flowcharts)
- Condicionales anidados: if dentro de if
- Condiciones compuestas con `and`, `or`, `not`
- El operador ternario: `x if condition else y`
- Truthy y Falsy values: qué se considera True o False
  - `0`, `""`, `[]`, `{}`, `None` son Falsy
  - Todo lo demás es Truthy
- Diagramas de flujo explicativos
- Ejercicios: calculadora de IMC, validador de contraseñas, sistema de calificaciones

#### Lección 7: Bucles - Repitiendo Acciones
- **Bucle `for` explicado exhaustivamente**:
  - Sintaxis: `for variable in iterable:`
  - Iterar sobre rangos: `for i in range(5):`
  - Variable `i`: qué es y por qué se llama así
  - Iterar sobre strings: `for letra in "hola":`
  - Iterar sobre listas (se introduce el concepto)
  - `range()` con inicio, fin y paso
  - Acumuladores: sumar valores en un bucle
  - Contadores: contar ocurrencias
  - Break y continue dentro de for
  - Else en bucles for (poco conocido pero útil)
  - Ejemplos: tablas de multiplicar, sumatorias, búsqueda
  
- **Bucle `while` explicado exhaustivamente**:
  - Sintaxis: `while condicion:`
  - Diferencia con for: cuándo usar cada uno
  - Contadores manuales: `i = i + 1`
  - Evitar bucles infinitos
  - Break y continue en while
  - While con condiciones compuestas
  - Menús interactivos con while True
  - Ejemplos: adivinar número, validación de inputs, menús

- **Control de flujo avanzado**:
  - `break`: salir del bucle inmediatamente
  - `continue`: saltar a la siguiente iteración
  - `pass`: placeholder que no hace nada
  - Bucles anidados: for dentro de for
  - Patrones con asteriscos (ejercicios clásicos)

---

### **MÓDULO 3: ESTRUCTURAS DE DATOS**

#### Lección 8: Listas - Colecciones Ordenadas
- ¿Qué es una lista? (analogía: lista de compras)
- Creación: `[1, 2, 3]` vs `list()`
- Índices: acceso con `[0]`, `[1]`, etc.
- Índices negativos: `[-1]` último elemento, `[-2]` penúltimo
- Slicing (rebanadas): `[inicio:fin:paso]`
  - `lista[0:3]` → primeros 3 elementos
  - `lista[:3]` → mismo resultado
  - `lista[2:]` → desde el índice 2 hasta el final
  - `lista[:]` → copia completa
  - `lista[::2]` → cada segundo elemento
  - `lista[::-1]` → invertir lista
- Métodos de listas (CADA UNO CON 5 EJEMPLOS):
  - `append()`: agregar al final
  - `insert()`: agregar en posición específica
  - `remove()`: eliminar por valor
  - `pop()`: eliminar por índice y devolver valor
  - `clear()`: vaciar lista completa
  - `index()`: encontrar posición de un valor
  - `count()`: contar ocurrencias
  - `sort()`: ordenar (ascending/descending)
  - `reverse()`: invertir orden
  - `copy()`: copiar lista
  - `extend()`: agregar otra lista
- Listas anidadas: listas dentro de listas
- Comprensión de listas (list comprehensions) básica
- Ejercicios: gestor de tareas, carrito de compras, estadísticas

#### Lección 9: Tuplas - Listas Inmutables
- ¿Qué es una tupla? diferencias con listas
- Creación: `(1, 2, 3)` vs `tuple()`
- Tuple con un solo elemento: `(1,)` ¡la coma es importante!
- Inmutabilidad: por qué no se pueden modificar
- Ventajas de usar tuplas
- Desempaquetado de tuplas: `a, b, c = tupla`
- Intercambio de variables: `a, b = b, a`
- Tuplas anidadas
- Cuando usar tuplas vs listas
- Ejercicios prácticos

#### Lección 10: Diccionarios - Pares Clave-Valor
- ¿Qué es un diccionario? (analogía: diccionario real)
- Creación: `{"clave": "valor"}` vs `dict()`
- Acceder a valores: `diccionario["clave"]`
- Método `get()`: acceso seguro con valor por defecto
- Agregar/modificar pares clave-valor
- Eliminar elementos: `del`, `pop()`, `popitem()`
- Métodos importantes:
  - `keys()`: obtener todas las claves
  - `values()`: obtener todos los valores
  - `items()`: obtener pares clave-valor
  - `update()`: actualizar con otro diccionario
  - `setdefault()`: establecer valor si no existe
- Iterar sobre diccionarios:
  - `for clave in diccionario:`
  - `for clave, valor in diccionario.items():`
- Diccionarios anidados
- Comprensión de diccionarios
- Ejercicios: agenda telefónica, inventario, traductor simple

#### Lección 11: Conjuntos (Sets) - Elementos Únicos
- ¿Qué es un set? (colección sin duplicados)
- Creación: `{1, 2, 3}` vs `set()`
- Set vacío: `set()` NO `{}` (esto es diccionario)
- Añadir elementos: `add()`, `update()`
- Eliminar: `remove()`, `discard()`, `pop()`
- Operaciones de conjuntos:
  - Unión: `|` o `union()`
  - Intersección: `&` o `intersection()`
  - Diferencia: `-` o `difference()`
  - Diferencia simétrica: `^` o `symmetric_difference()`
- Subconjuntos y superconjuntos
- Sets inmutables: `frozenset`
- Ejercicios: eliminar duplicados, comparar colecciones

---

### **MÓDULO 4: FUNCIONES Y PROGRAMACIÓN MODULAR**

#### Lección 12: Funciones Definidas por el Usuario (Parte 1)
- ¿Por qué usar funciones? (DRY: Don't Repeat Yourself)
- Definición: `def nombre_funcion():`
- Llamar/ejecutar una función
- Parámetros vs argumentos (diferencia clara)
- Parámetros posicionales
- Retorno de valores: `return`
  - Qué pasa si no hay return (devuelve None)
  - Retornar múltiples valores (tupla implícita)
- Scope (alcance) de variables:
  - Variables locales (dentro de función)
  - Variables globales (fuera de función)
  - Palabra clave `global`
- Ejercicios: calculadora modular, validadores

#### Lección 13: Funciones Definidas por el Usuario (Parte 2)
- Parámetros por defecto: `def func(param=valor):`
- Argumentos nombrados (keyword arguments): `func(nombre="Ana")`
- `*args`: cantidad variable de argumentos posicionales
- `**kwargs`: cantidad variable de argumentos nombrados
- Combinación: `(param, *args, **kwargs)`
- Funciones recursivas (explicado con factorial y Fibonacci)
- Documentación de funciones: docstrings
- Type hints (pistas de tipo): `def func(x: int) -> str:`
- Funciones lambda (anónimas): `lambda x: x * 2`
- Ejercicios avanzados

#### Lección 14: Módulos y Paquetes
- ¿Qué es un módulo? (archivo .py)
- Importar módulos: `import modulo`
- Importar funciones específicas: `from modulo import funcion`
- Alias: `import modulo as m`
- Módulos estándar útiles:
  - `math`: matemáticas avanzadas
  - `random`: números aleatorios
  - `datetime`: fechas y horas
  - `os`: sistema operativo
  - `sys`: parámetros del sistema
  - `json`: trabajar con JSON
  - `re`: expresiones regulares
- Crear tus propios módulos
- Paquetes: carpetas con `__init__.py`
- Instalar paquetes con pip
- Introducción a PyPI
- Ejercicios: organizador de archivos, generador de contraseñas

---

### **MÓDULO 5: PROGRAMACIÓN ORIENTADA A OBJETOS (POO)**

#### Lección 15: Clases y Objetos - Fundamentos
- ¿Qué es POO? (analogía: planos y casas)
- Clases vs Objetos (instancias)
- Definir una clase: `class MiClase:`
- El constructor `__init__()`
- El parámetro `self`: qué es y por qué es necesario
- Atributos de instancia
- Métodos de instancia
- Crear objetos: `objeto = MiClase()`
- Acceder a atributos y métodos
- Ejemplo completo paso a paso

#### Lección 16: POO Intermedio
- Atributos de clase vs instancia
- Métodos de clase: `@classmethod`
- Métodos estáticos: `@staticmethod`
- Encapsulamiento:
  - Atributos públicos
  - Atributos privados: `__atributo`
  - Getters y setters
  - Decorador `@property`
- Herencia: clases hijas y padres
- Sobrescribir métodos
- Función `super()`
- Herencia múltiple
- Ejercicios: sistema bancario, videojuego simple

#### Lección 17: POO Avanzado
- Polimorfismo: misma interfaz, diferentes implementaciones
- Clases abstractas: `abc.ABC`
- Métodos mágicos (dunder methods):
  - `__str__()` y `__repr__()`: representación string
  - `__len__()`: longitud
  - `__getitem__()`: acceso con corchetes
  - `__add__()`, `__sub__()`: operadores
  - `__eq__()`: comparación de igualdad
- Composición vs Herencia
- Ejercicios: biblioteca, sistema de reservas

---

### **MÓDULO 6: MANEJO DE ERRORES Y ARCHIVOS**

#### Lección 18: Excepciones y Manejo de Errores
- ¿Qué es una excepción?
- Errores comunes: SyntaxError, NameError, TypeError, ValueError, IndexError, KeyError
- Try-except básico
- Múltiples except para diferentes errores
- Else: ejecutar si no hay error
- Finally: ejecutar siempre
- Lanzar excepciones: `raise`
- Crear excepciones personalizadas
- Buenas prácticas
- Ejercicios: validador robusto, lector de archivos seguro

#### Lección 19: Manejo de Archivos
- Abrir archivos: `open()`
- Modos: `"r"`, `"w"`, `"a"`, `"rb"`, `"wb"`
- Leer archivos: `read()`, `readline()`, `readlines()`
- Escribir archivos: `write()`, `writelines()`
- Context managers: `with open(...) as f:`
- Archivos CSV: módulo `csv`
- Archivos JSON: módulo `json`
- Rutas de archivos: módulo `pathlib`
- Ejercicios: diario personal, gestor de contactos, backup simple

---

### **MÓDULO 7: TEMAS AVANZADOS**

#### Lección 20: Expresiones Regulares
- ¿Qué son regex?
- Módulo `re`
- Patrones básicos
- Metacaracteres: `.`, `*`, `+`, `?`, `[]`, `()`
- Búsqueda: `search()`, `findall()`
- Validación: emails, teléfonos
- Reemplazo: `sub()`
- Ejercicios: validador de formularios

#### Lección 21: Generadores e Iteradores
- Iteradores: `iter()`, `next()`
- Generadores: `yield` vs `return`
- Generadores infinitos
- Expresiones generadoras
- Módulo `itertools`
- Ejercicios: procesamiento eficiente de datos

#### Lección 22: Decoradores
- Funciones como objetos
- Funciones dentro de funciones
- Decoradores básicos
- Decoradores con parámetros
- Decoradores comunes: `@staticmethod`, `@classmethod`, `@property`
- Crear tus propios decoradores
- Ejercicios: logging, timing de funciones

#### Lección 23: Programación Funcional
- `map()`: aplicar función a todos los elementos
- `filter()`: filtrar elementos
- `reduce()`: reducir a un valor (functools)
- Funciones puras
- Inmutabilidad
- Ejercicios: transformación de datos

#### Lección 24: Introducción a Data Science
- NumPy: arrays multidimensionales
- pandas: DataFrames
- matplotlib: gráficos básicos
- Ejercicios: análisis de datos simple

---

### **MÓDULO 8: PROYECTOS FINALES**

#### Proyecto 1: Sistema de Gestión de Biblioteca
- CRUD completo (Crear, Leer, Actualizar, Eliminar)
- Persistencia en archivos JSON
- Búsquedas avanzadas
- Interfaz de línea de comandos

#### Proyecto 2: Juego de Aventuras Textual
- Clases y herencia
- Sistema de combate
- Inventario
- Múltiples habitaciones

#### Proyecto 3: Analizador de Texto
- Estadísticas de texto
- Expresiones regulares
- Generación de reportes
- Exportación a diferentes formatos

#### Proyecto 4: Automatización de Tareas
- Manipulación de archivos
- Web scraping básico
- Envío de emails
- Programación de tareas

---

## 🚀 Aplicación de Escritorio

El curso incluye una **aplicación de escritorio executable (.exe)** que contiene:

- ✅ **Terminal integrada**: Escribe y ejecuta código Python directamente
- ✅ **Editor de código**: Con resaltado de sintaxis, autocompletado y colores estilo VSCode
- ✅ **Sistema de ejercicios autocorregibles**: Retroalimentación instantánea
- ✅ **Seguimiento de progreso**: Mira cuánto has avanzado
- ✅ **Acceso offline**: No necesitas internet una vez instalado
- ✅ **Todo incluido**: Python, ejercicios, explicaciones, todo en un solo paquete

### Instalación de la Aplicación

1. Descarga el archivo `CursoPython.exe` desde la sección de Releases
2. Ejecuta el instalador
3. ¡Listo! Comienza a aprender

---

## 📝 Cómo Usar Este Curso

### Opción 1: Aplicación de Escritorio (Recomendada)
```bash
# Simplemente descarga y ejecuta CursoPython.exe
# No necesitas instalar nada más
```

### Opción 2: Desde el Repositorio (para desarrolladores)
```bash
# Clona el repositorio
git clone <url>

# Instala dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
python app.py
```

### Opción 3: GitHub Codespaces (sin descargar nada)
1. Abre este repositorio en GitHub
2. Haz clic en "Code" → "Codespaces"
3. Crea un codespace nuevo
4. Todo estará configurado automáticamente

---

## 🎓 Certificación

Al completar todos los ejercicios y proyectos, recibirás un certificado digital de completación del curso.

---

## 🤝 Contribuciones

¿Encontraste un error? ¿Tienes una sugerencia? ¡Las contribuciones son bienvenidas!

---

## 📄 Licencia

Este curso está bajo licencia MIT. Siéntete libre de usarlo y compartirlo.

---

## 👨‍🏫 Sobre el Autor

Curso creado con ❤️ para la comunidad hispanohablante.

---

## 📞 Soporte

Si tienes problemas o preguntas:
- Abre un issue en este repositorio
- Revisa la sección de FAQ
- Consulta la documentación de cada lección

---

**¡Comienza ahora con la Lección 1 y conviértete en un experto en Python!** 🐍🚀
