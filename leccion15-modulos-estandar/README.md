# Lección 15: Módulos Estándar Útiles

## 📖 Introducción

Python incluye una biblioteca estándar rica con módulos listos para usar. Esta lección cubre los más útiles:

- **datetime** - Manejo de fechas y horas
- **json** - Trabajo con datos JSON
- **random** - Generación de números aleatorios
- **os y sys** - Interacción con el sistema operativo
- **math** - Funciones matemáticas avanzadas
- **re** - Expresiones regulares

## 🎯 Módulo datetime

Manejo de fechas y horas.

### Fechas básicas
```python
from datetime import date, datetime, timedelta

# Fecha actual
hoy = date.today()
print(f"Hoy es: {hoy}")  # 2024-01-15

# Fecha y hora actuales
ahora = datetime.now()
print(f"Ahora: {ahora}")  # 2024-01-15 14:30:45.123456

# Crear fecha específica
navidad = date(2024, 12, 25)
print(f"Navidad: {navidad}")

# Formatear fecha
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M")
print(f"Formateada: {fecha_formateada}")  # 15/01/2024 14:30

# Parsear string a fecha
texto_fecha = "25/12/2024"
fecha_parseada = datetime.strptime(texto_fecha, "%d/%m/%Y")
print(f"Parseada: {fecha_parseada.date()}")
```

### Operaciones con fechas
```python
# Diferencia entre fechas
dias_para_navidad = navidad - hoy
print(f"Días para Navidad: {dias_para_navidad.days}")

# Sumar/restar tiempo
una_semana = timedelta(days=7)
proxima_semana = hoy + una_semana
print(f"Próxima semana: {proxima_semana}")

# Calcular edad
nacimiento = date(1990, 5, 15)
edad_dias = hoy - nacimiento
edad_anios = edad_dias.days // 365
print(f"Edad: {edad_anios} años")
```

## 📚 Módulo json

Trabajo con datos en formato JSON.

### Parsear JSON
```python
import json

# JSON string a diccionario
json_string = '{"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}'
datos = json.loads(json_string)
print(datos["nombre"])  # Juan
print(type(datos))  # <class 'dict'>
```

### Convertir a JSON
```python
# Diccionario a JSON string
persona = {
    "nombre": "María",
    "edad": 25,
    "habilidades": ["Python", "JavaScript", "SQL"],
    "activo": True
}

json_string = json.dumps(persona, indent=2, ensure_ascii=False)
print(json_string)
```

### Leer/escribir archivos JSON
```python
# Escribir JSON a archivo
with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(persona, f, indent=2, ensure_ascii=False)

# Leer JSON desde archivo
with open('datos.json', 'r', encoding='utf-8') as f:
    datos_leidos = json.load(f)
    print(datos_leidos)
```

## ⚡ Módulo random

Generación de números y selecciones aleatorias.

```python
import random

# Número aleatorio entre 0 y 1
print(random.random())  # 0.847362...

# Número entero en rango
print(random.randint(1, 100))  # 42

# Número flotante en rango
print(random.uniform(1.5, 5.5))  # 3.284...

# Elección aleatoria de lista
colores = ["rojo", "verde", "azul", "amarillo"]
print(random.choice(colores))  # "azul"

# Muestra aleatoria (sin repetición)
print(random.sample(colores, 2))  # ["verde", "rojo"]

# Barajar lista
random.shuffle(colores)
print(colores)  # Orden mezclado

# Semilla para reproducibilidad
random.seed(42)
print(random.randint(1, 100))  # Siempre 82 con esta semilla
```

## 📦 Módulos os y sys

### Módulo os - Sistema operativo
```python
import os

# Directorio actual
directorio = os.getcwd()
print(f"Directorio actual: {directorio}")

# Cambiar directorio
os.chdir('/tmp')

# Listar archivos
archivos = os.listdir('.')
print(f"Archivos: {archivos[:5]}")  # Primeros 5

# Crear directorio
os.makedirs('mi_carpeta/nueva', exist_ok=True)

# Unir rutas (multiplataforma)
ruta_completa = os.path.join('home', 'usuario', 'documentos')
print(ruta_completa)  # home/usuario/documentos

# Información de archivo
existe = os.path.exists('archivo.txt')
es_archivo = os.path.isfile('archivo.txt')
es_directorio = os.path.isdir('mi_carpeta')
tamano = os.path.getsize('archivo.txt')

# Eliminar archivo
os.remove('archivo_temporal.txt')

# Variables de entorno
path_python = os.environ.get('PATH')
usuario = os.environ.get('USER', 'Usuario desconocido')
```

### Módulo sys - Sistema Python
```python
import sys

# Versión de Python
print(f"Versión: {sys.version}")

# Argumentos de línea de comandos
if len(sys.argv) > 1:
    print(f"Argumentos: {sys.argv[1:]}")

# Ruta de búsqueda de módulos
print(f"Paths: {sys.path[:3]}")  # Primeros 3

# Salir del programa
# sys.exit(0)  # Salida normal
# sys.exit(1)  # Salida con error

# Redirigir salida
sys.stdout.write("Mensaje a stdout\n")
sys.stderr.write("Mensaje de error\n")
```

## 📐 Módulo math

Funciones matemáticas avanzadas.

```python
import math

# Constantes
print(f"PI: {math.pi}")  # 3.14159...
print(f"E: {math.e}")    # 2.71828...
print(f"Tau: {math.tau}")  # 6.28318...

# Redondeo
print(math.ceil(4.2))    # 5 (hacia arriba)
print(math.floor(4.8))   # 4 (hacia abajo)
print(math.trunc(4.8))   # 4 (parte entera)

# Potencias y raíces
print(math.pow(2, 3))    # 8.0
print(math.sqrt(16))     # 4.0
print(math.exp(2))       # e^2 = 7.389...

# Logaritmos
print(math.log(100, 10))  # 2.0 (log base 10)
print(math.log10(100))    # 2.0
print(math.log2(8))       # 3.0

# Trigonometría (radianes)
angulo = math.radians(90)  # Convertir grados a radianes
print(math.sin(angulo))    # 1.0
print(math.cos(angulo))    # 0.0
print(math.tan(angulo))    # Muy grande

# Factorial y combinatoria
print(math.factorial(5))   # 120
print(math.comb(5, 2))     # 10 (combinaciones)
print(math.perm(5, 2))     # 20 (permutaciones)

# Máximo común divisor y mínimo común múltiplo
print(math.gcd(48, 18))    # 6
print(math.lcm(4, 6))      # 12
```

## 🔍 Módulo re - Expresiones Regulares

Patrones para buscar y manipular texto.

```python
import re

# Buscar patrón
texto = "Mi email es usuario@ejemplo.com"
patron = r'\w+@\w+\.\w+'
resultado = re.search(patron, texto)
if resultado:
    print(f"Email encontrado: {resultado.group()}")

# Encontrar todos los matches
texto = "Teléfonos: 123-456, 789-012, 345-678"
patron = r'\d{3}-\d{3}'
todos = re.findall(patron, texto)
print(todos)  # ['123-456', '789-012', '345-678']

# Validar patrón completo
email = "usuario@ejemplo.com"
patron = r'^[\w\.]+@[\w\.]+\.\w+$'
if re.match(patron, email):
    print("Email válido")

# Reemplazar
texto = "Hola mundo cruel"
nuevo = re.sub(r'mundo cruel', 'Python', texto)
print(nuevo)  # "Hola Python"

# Dividir por patrón
texto = "uno,dos;tres cuatro"
partes = re.split(r'[,\s;]+', texto)
print(partes)  # ['uno', 'dos', 'tres', 'cuatro']

# Grupos de captura
texto = "Nombre: Juan, Edad: 30"
patron = r'Nombre: (\w+), Edad: (\d+)'
match = re.search(patron, texto)
if match:
    nombre = match.group(1)  # Juan
    edad = match.group(2)    # 30
    print(f"{nombre} tiene {edad} años")
```

### Patrones comunes
```python
patrones = {
    'email': r'[\w\.-]+@[\w\.-]+\.\w+',
    'telefono': r'\d{3}-\d{3}-\d{3}',
    'fecha': r'\d{2}/\d{2}/\d{4}',
    'url': r'https?://[\w\.-]+(?:/[\w\.-]*)*',
    'codigo_postal': r'\d{5}',
    'solo_letras': r'^[a-zA-Z]+$',
    'solo_numeros': r'^\d+$',
}
```

## 🎯 Ejemplos Prácticos

### Ejemplo 1: Gestor de archivos con logging
```python
import os
import json
from datetime import datetime

def organizar_archivos(directorio):
    """Organiza archivos por extensión"""
    archivos_por_ext = {}
    
    for archivo in os.listdir(directorio):
        ruta = os.path.join(directorio, archivo)
        if os.path.isfile(ruta):
            ext = os.path.splitext(archivo)[1] or 'sin_extension'
            if ext not in archivos_por_ext:
                archivos_por_ext[ext] = []
            archivos_por_ext[ext].append({
                'nombre': archivo,
                'tamano': os.path.getsize(ruta),
                'modificado': datetime.fromtimestamp(os.path.getmtime(ruta)).isoformat()
            })
    
    # Guardar reporte JSON
    with open('reporte_archivos.json', 'w', encoding='utf-8') as f:
        json.dump(archivos_por_ext, f, indent=2, ensure_ascii=False)
    
    return archivos_por_ext
```

### Ejemplo 2: Validador de datos con regex
```python
import re

class Validador:
    @staticmethod
    def es_email_valido(email):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        return bool(re.match(patron, email))
    
    @staticmethod
    def es_telefono_valido(telefono):
        patron = r'^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
        return bool(re.match(patron, telefono))
    
    @staticmethod
    def es_fecha_valida(fecha_str):
        try:
            datetime.strptime(fecha_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False
    
    @staticmethod
    def extraer_urls(texto):
        patron = r'https?://[\w\.-]+(?:/[\w\.-/?=&]*)*'
        return re.findall(patron, texto)
```

### Ejemplo 3: Calculadora científica
```python
import math

def calculadora_cientifica():
    """Calculadora con funciones avanzadas"""
    print("=== Calculadora Científica ===")
    print("Operaciones: sin, cos, tan, sqrt, log, exp, pow, factorial")
    
    while True:
        operacion = input("\nOperación (o 'salir'): ").lower()
        if operacion == 'salir':
            break
        
        try:
            if operacion in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'factorial']:
                num = float(input("Número: "))
                if operacion == 'sin':
                    resultado = math.sin(math.radians(num))
                elif operacion == 'cos':
                    resultado = math.cos(math.radians(num))
                elif operacion == 'tan':
                    resultado = math.tan(math.radians(num))
                elif operacion == 'sqrt':
                    resultado = math.sqrt(num)
                elif operacion == 'log':
                    resultado = math.log10(num)
                elif operacion == 'exp':
                    resultado = math.exp(num)
                elif operacion == 'factorial':
                    resultado = math.factorial(int(num))
            elif operacion == 'pow':
                base = float(input("Base: "))
                exp = float(input("Exponente: "))
                resultado = math.pow(base, exp)
            else:
                print("Operación no reconocida")
                continue
            
            print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Error: {e}")
```

## 📝 Ejercicios

### Ejercicio 15.1: Gestor de cumpleaños
Crea un programa que use `datetime` para calcular cuántos días faltan para tu próximo cumpleaños y qué día de la semana caerá.

### Ejercicio 15.2: Analizador de logs JSON
Lee un archivo de logs en formato JSON, filtra las entradas por fecha y genera un reporte con estadísticas.

### Ejercicio 15.3: Generador de contraseñas
Usa `random` para crear un generador de contraseñas seguras que incluya mayúsculas, minúsculas, números y símbolos.

### Ejercicio 15.4: Organizador de archivos
Crea un script que organice los archivos de una carpeta en subcarpetas según su extensión usando `os`.

### Ejercicio 15.5: Validador de formularios
Implementa un validador de formularios web usando expresiones regulares para emails, teléfonos, URLs y códigos postales.

### Ejercicio 15.6: Calculadora de interés compuesto
Usa `math` para crear una calculadora de interés compuesto con fórmula: A = P(1 + r/n)^(nt)

## ✅ Soluciones

Las soluciones están en la carpeta `soluciones/solucion_15_*.py`.

## 🔍 Test de Autoevaluación

1. ¿Cómo formateas una fecha para mostrar "dd/mm/yyyy"?
2. ¿Qué función convierte un diccionario a JSON string?
3. ¿Cómo seleccionas un elemento aleatorio de una lista?
4. ¿Cuál es la diferencia entre `os.getcwd()` y `os.chdir()`?
5. ¿Qué patrón regex usarías para validar un código postal de 5 dígitos?

## ➡️ Siguiente Lección

Continúa con la [Lección 16: Introducción a Data Science](../leccion16-intro-data-science/)
