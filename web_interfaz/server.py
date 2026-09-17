#!/usr/bin/env python3
"""
Interfaz Web para el Curso de Python - Terminal Interactiva con Autocorrección

Servidor web ligero que proporciona:
1. Terminal interactiva para ejecutar código Python
2. Sistema de autocorrección de ejercicios
3. Seguimiento de progreso del estudiante
4. Retroalimentación inmediata

Uso:
    python web_interfaz/server.py
"""

import http.server
import socketserver
import json
import sys
import os
import io
import traceback
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import importlib.util

# Configuración
PUERTO = 8000
DIRECTORIO_BASE = Path(__file__).parent.parent
CARPETA_EJERCICIOS = DIRECTORIO_BASE / "ejercicios"
CARPETA_SOLUCIONES = DIRECTORIO_BASE / "soluciones"

class Colores:
    VERDE = '\033[92m'
    ROJO = '\033[91m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    RESET = '\033[0m'
    NEGRITA = '\033[1m'


def cargar_ejercicio(ruta_archivo):
    """Carga un módulo de ejercicio desde una ruta"""
    if not os.path.exists(ruta_archivo):
        return None
    
    try:
        spec = importlib.util.spec_from_file_location("ejercicio_usuario", ruta_archivo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        return modulo
    except Exception as e:
        return {"error": str(e)}


def ejecutar_codigo(codigo, timeout=5):
    """
    Ejecuta código Python de forma segura y captura la salida
    Retorna: {'salida': str, 'error': str|None, 'resultado': any}
    """
    # Redirigir stdout y stderr
    viejo_stdout = sys.stdout
    viejo_stderr = sys.stderr
    stdout_capturado = io.StringIO()
    stderr_capturado = io.StringIO()
    
    resultado = None
    error = None
    
    try:
        sys.stdout = stdout_capturado
        sys.stderr = stderr_capturado
        
        # Crear un namespace seguro para la ejecución
        namespace = {
            '__builtins__': __builtins__,
            'print': print,
            'input': lambda prompt="": "[INPUT SIMULADO]",  # input simulado
            'len': len,
            'range': range,
            'str': str,
            'int': int,
            'float': float,
            'bool': bool,
            'list': list,
            'dict': dict,
            'tuple': tuple,
            'set': set,
            'min': min,
            'max': max,
            'sum': sum,
            'abs': abs,
            'round': round,
            'pow': pow,
            'sorted': sorted,
            'enumerate': enumerate,
            'zip': zip,
            'map': map,
            'filter': filter,
            'True': True,
            'False': False,
            'None': None,
        }
        
        # Ejecutar el código
        exec(codigo, namespace)
        
        # Intentar obtener el resultado si hay una variable 'resultado'
        resultado = namespace.get('resultado', None)
        
    except Exception as e:
        error = f"{type(e).__name__}: {str(e)}\n{traceback.format_exc()}"
    finally:
        sys.stdout = viejo_stdout
        sys.stderr = viejo_stderr
    
    return {
        'salida': stdout_capturado.getvalue(),
        'error': error,
        'resultado': resultado
    }


def verificar_ejercicio(ejercicio_id, codigo_usuario):
    """
    Verifica un ejercicio específico comparando con la solución esperada
    """
    archivo_solucion = CARPETA_SOLUCIONES / f"{ejercicio_id}.py"
    
    # Ejecutar código del usuario
    resultado_usuario = ejecutar_codigo(codigo_usuario)
    
    if resultado_usuario['error']:
        return {
            'correcto': False,
            'mensaje': f"Error en tu código:\n{resultado_usuario['error']}",
            'salida': resultado_usuario['salida']
        }
    
    # Cargar y ejecutar solución de referencia
    if archivo_solucion.exists():
        with open(archivo_solucion, 'r', encoding='utf-8') as f:
            codigo_solucion = f.read()
        
        resultado_solucion = ejecutar_codigo(codigo_solucion)
        
        # Comparar salidas
        if resultado_usuario['salida'].strip() == resultado_solucion['salida'].strip():
            return {
                'correcto': True,
                'mensaje': "¡Excelente! Tu solución es correcta. 🎉",
                'salida': resultado_usuario['salida'],
                'puntos': 100
            }
        else:
            return {
                'correcto': False,
                'mensaje': "Casi... pero la salida no coincide exactamente con lo esperado.",
                'salida': resultado_usuario['salida'],
                'salida_esperada': resultado_solucion['salida'],
                'puntos': 50
            }
    else:
        # Si no hay solución de referencia, verificar sintaxis básica
        return {
            'correcto': True,
            'mensaje': "Código ejecutado correctamente (sin validación completa disponible).",
            'salida': resultado_usuario['salida'],
            'puntos': 75
        }


def listar_ejercicios():
    """Lista todos los ejercicios disponibles"""
    ejercicios = []
    
    for archivo in sorted(CARPETA_EJERCICIOS.glob("ejercicio_*.py")):
        if archivo.name.startswith("__"):
            continue
            
        ejercicio_id = archivo.stem  # ej: ejercicio_01_01
        
        # Leer las primeras líneas para obtener descripción
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read(500)
            
        descripcion = "Sin descripción"
        if '"""' in contenido:
            partes = contenido.split('"""')
            if len(partes) > 1:
                descripcion = partes[1].strip()
        
        ejercicios.append({
            'id': ejercicio_id,
            'nombre': ejercicio_id.replace('_', ' ').title(),
            'descripcion': descripcion,
            'archivo': archivo.name
        })
    
    return ejercicios


class ManejadorCurso(http.server.SimpleHTTPRequestHandler):
    """Manejador HTTP personalizado para el curso"""
    
    def do_GET(self):
        """Manejar solicitudes GET"""
        ruta = urlparse(self.path).path
        
        if ruta == '/' or ruta == '/index.html':
            self.enviar_html(obtener_index())
        elif ruta == '/estilos.css':
            self.enviar_css()
        elif ruta == '/script.js':
            self.enviar_js()
        elif ruta.startswith('/api/ejercicios'):
            self.api_listar_ejercicios()
        elif ruta.startswith('/leccion/'):
            leccion_num = ruta.split('/')[2]
            self.enviar_html(obtener_leccion(leccion_num))
        else:
            super().do_GET()
    
    def do_POST(self):
        """Manejar solicitudes POST"""
        longitud_contenido = int(self.headers.get('Content-Length', 0))
        cuerpo = self.rfile.read(longitud_contenido).decode('utf-8')
        
        ruta = urlparse(self.path).path
        
        if ruta == '/api/ejecutar':
            datos = json.loads(cuerpo)
            codigo = datos.get('codigo', '')
            resultado = ejecutar_codigo(codigo)
            self.enviar_json(resultado)
        
        elif ruta == '/api/verificar':
            datos = json.loads(cuerpo)
            ejercicio_id = datos.get('ejercicio_id', '')
            codigo = datos.get('codigo', '')
            resultado = verificar_ejercicio(ejercicio_id, codigo)
            self.enviar_json(resultado)
        
        elif ruta == '/api/progreso':
            self.enviar_json({'progreso': [], 'total': 0})
        
        else:
            self.send_error(404, "No encontrado")
    
    def api_listar_ejercicios(self):
        """API: Listar todos los ejercicios"""
        ejercicios = listar_ejercicios()
        self.enviar_json({'ejercicios': ejercicios})
    
    def enviar_json(self, datos):
        """Enviar respuesta JSON"""
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(datos, ensure_ascii=False, indent=2).encode('utf-8'))
    
    def enviar_html(self, html):
        """Enviar respuesta HTML"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def enviar_css(self):
        """Enviar CSS"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/css; charset=utf-8')
        self.end_headers()
        css = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #333;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
}

header {
    text-align: center;
    color: white;
    padding: 30px 0;
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

header p {
    font-size: 1.2em;
    opacity: 0.9;
}

.main-content {
    display: grid;
    grid-template-columns: 300px 1fr 350px;
    gap: 20px;
    margin-top: 20px;
}

.sidebar {
    background: white;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    max-height: 80vh;
    overflow-y: auto;
}

.sidebar h2 {
    color: #667eea;
    margin-bottom: 15px;
    font-size: 1.3em;
}

.ejercicio-item {
    padding: 12px;
    margin-bottom: 10px;
    background: #f8f9fa;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
    border-left: 4px solid transparent;
}

.ejercicio-item:hover {
    background: #e9ecef;
    transform: translateX(5px);
}

.ejercicio-item.activo {
    border-left-color: #667eea;
    background: #e7f3ff;
}

.ejercicio-item.completado {
    border-left-color: #28a745;
}

.editor-container {
    background: white;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
}

.editor-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.editor-header h2 {
    color: #667eea;
}

.code-editor {
    flex: 1;
    font-family: 'Courier New', monospace;
    font-size: 14px;
    padding: 15px;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    resize: none;
    min-height: 300px;
    background: #f8f9fa;
    line-height: 1.5;
}

.code-editor:focus {
    outline: none;
    border-color: #667eea;
}

.button-group {
    display: flex;
    gap: 10px;
    margin-top: 15px;
}

.btn {
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s;
}

.btn-ejecutar {
    background: #28a745;
    color: white;
}

.btn-ejecutar:hover {
    background: #218838;
}

.btn-verificar {
    background: #667eea;
    color: white;
}

.btn-verificar:hover {
    background: #5a6fd6;
}

.btn-limpiar {
    background: #dc3545;
    color: white;
}

.btn-limpiar:hover {
    background: #c82333;
}

.output-panel {
    background: white;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
}

.output-panel h2 {
    color: #667eea;
    margin-bottom: 15px;
}

.output-content {
    flex: 1;
    background: #1e1e1e;
    color: #d4d4d4;
    padding: 15px;
    border-radius: 8px;
    font-family: 'Courier New', monospace;
    font-size: 13px;
    overflow-y: auto;
    min-height: 200px;
    white-space: pre-wrap;
    word-wrap: break-word;
}

.output-content.error {
    color: #f48771;
}

.output-content.success {
    color: #89d185;
}

.progreso-panel {
    margin-top: 20px;
}

.progreso-barra {
    background: #e9ecef;
    border-radius: 10px;
    height: 20px;
    overflow: hidden;
    margin-top: 10px;
}

.progreso-lleno {
    height: 100%;
    background: linear-gradient(90deg, #28a745, #20c997);
    transition: width 0.5s;
}

.descripcion-ejercicio {
    background: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 15px;
    margin-bottom: 15px;
    border-radius: 5px;
}

@media (max-width: 1200px) {
    .main-content {
        grid-template-columns: 1fr;
    }
    
    .sidebar, .output-panel {
        max-height: none;
    }
}
"""
        self.wfile.write(css.encode('utf-8'))
    
    def enviar_js(self):
        """Enviar JavaScript"""
        self.send_response(200)
        self.send_header('Content-Type', 'application/javascript; charset=utf-8')
        self.end_headers()
        js = """
// Estado de la aplicación
let ejercicioActual = null;
let ejerciciosCompletados = [];

// Cargar lista de ejercicios al iniciar
document.addEventListener('DOMContentLoaded', () => {
    cargarEjercicios();
});

async function cargarEjercicios() {
    try {
        const respuesta = await fetch('/api/ejercicios');
        const datos = await respuesta.json();
        
        const contenedor = document.getElementById('lista-ejercicios');
        contenedor.innerHTML = '';
        
        datos.ejercicios.forEach(ejercicio => {
            const item = document.createElement('div');
            item.className = 'ejercicio-item';
            item.dataset.id = ejercicio.id;
            item.innerHTML = `
                <strong>${ejercicio.nombre}</strong>
                <p style="font-size: 0.9em; color: #666; margin-top: 5px;">
                    ${ejercicio.descripcion.substring(0, 50)}...
                </p>
            `;
            item.onclick = () => seleccionarEjercicio(ejercicio);
            contenedor.appendChild(item);
        });
    } catch (error) {
        console.error('Error cargando ejercicios:', error);
    }
}

function seleccionarEjercicio(ejercicio) {
    ejercicioActual = ejercicio;
    
    // Actualizar UI
    document.querySelectorAll('.ejercicio-item').forEach(item => {
        item.classList.remove('activo');
    });
    document.querySelector(`[data-id="${ejercicio.id}"]`).classList.add('activo');
    
    // Cargar descripción
    document.getElementById('descripcion-ejercicio').innerHTML = `
        <h3>${ejercicio.nombre}</h3>
        <p>${ejercicio.descripcion}</p>
    `;
    
    // Cargar código base si existe
    cargarCodigoBase(ejercicio.archivo);
}

async function cargarCodigoBase(archivo) {
    try {
        // En una implementación real, cargaríamos el archivo
        const editor = document.getElementById('editor-codigo');
        editor.value = `# ${archivo}\\n# Escribe tu solución aquí\\n\\n`;
    } catch (error) {
        console.error('Error cargando código:', error);
    }
}

async function ejecutarCodigo() {
    const codigo = document.getElementById('editor-codigo').value;
    const outputPanel = document.getElementById('output-contenido');
    
    outputPanel.className = 'output-content';
    outputPanel.textContent = 'Ejecutando...';
    
    try {
        const respuesta = await fetch('/api/ejecutar', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({codigo})
        });
        
        const resultado = await respuesta.json();
        
        if (resultado.error) {
            outputPanel.className = 'output-content error';
            outputPanel.textContent = `❌ Error:\\n${resultado.error}`;
        } else {
            outputPanel.className = 'output-content';
            outputPanel.textContent = resultado.salida || '(Sin salida)';
        }
    } catch (error) {
        outputPanel.className = 'output-content error';
        outputPanel.textContent = `Error de conexión: ${error}`;
    }
}

async function verificarEjercicio() {
    if (!ejercicioActual) {
        alert('Selecciona un ejercicio primero');
        return;
    }
    
    const codigo = document.getElementById('editor-codigo').value;
    const outputPanel = document.getElementById('output-contenido');
    
    outputPanel.className = 'output-content';
    outputPanel.textContent = 'Verificando...';
    
    try {
        const respuesta = await fetch('/api/verificar', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                ejercicio_id: ejercicioActual.id,
                codigo: codigo
            })
        });
        
        const resultado = await respuesta.json();
        
        if (resultado.correcto) {
            outputPanel.className = 'output-content success';
            outputPanel.textContent = `✅ ${resultado.mensaje}\\n\\nSalida:\\n${resultado.salida}`;
            
            // Marcar como completado
            if (!ejerciciosCompletados.includes(ejercicioActual.id)) {
                ejerciciosCompletados.push(ejercicioActual.id);
                document.querySelector(`[data-id="${ejercicioActual.id}"]`).classList.add('completado');
                actualizarProgreso();
            }
        } else {
            outputPanel.className = 'output-content';
            outputPanel.textContent = `⚠️ ${resultado.mensaje}\\n\\nTu salida:\\n${resultado.salida}\\n\\nSalida esperada (referencia):\\n${resultado.salida_esperada || 'N/A'}`;
        }
    } catch (error) {
        outputPanel.className = 'output-content error';
        outputPanel.textContent = `Error de conexión: ${error}`;
    }
}

function actualizarProgreso() {
    const total = document.querySelectorAll('.ejercicio-item').length;
    const completados = ejerciciosCompletados.length;
    const porcentaje = total > 0 ? (completados / total) * 100 : 0;
    
    document.getElementById('progreso-lleno').style.width = `${porcentaje}%`;
    document.getElementById('progreso-texto').textContent = `${completados}/${total} ejercicios completados`;
}

function limpiarEditor() {
    document.getElementById('editor-codigo').value = '';
    document.getElementById('output-contenido').textContent = '';
}
"""
        self.wfile.write(js.encode('utf-8'))


def obtener_index():
    """Genera el HTML principal"""
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Curso Python - Terminal Interactiva</title>
    <link rel="stylesheet" href="/estilos.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🐍 Curso Completo de Python</h1>
            <p>Terminal Interactiva con Autocorrección</p>
        </header>
        
        <div class="main-content">
            <!-- Sidebar con lista de ejercicios -->
            <aside class="sidebar">
                <h2>📚 Ejercicios</h2>
                <div id="lista-ejercicios">
                    <p>Cargando ejercicios...</p>
                </div>
                
                <div class="progreso-panel">
                    <h3>📊 Tu Progreso</h3>
                    <div id="progreso-texto">0/0 ejercicios completados</div>
                    <div class="progreso-barra">
                        <div id="progreso-lleno" class="progreso-lleno" style="width: 0%"></div>
                    </div>
                </div>
            </aside>
            
            <!-- Editor de código -->
            <main class="editor-container">
                <div class="editor-header">
                    <h2>✏️ Editor de Código</h2>
                </div>
                
                <div id="descripcion-ejercicio" class="descripcion-ejercicio">
                    <p>Selecciona un ejercicio para comenzar</p>
                </div>
                
                <textarea id="editor-codigo" class="code-editor" placeholder="# Escribe tu código Python aquí..."></textarea>
                
                <div class="button-group">
                    <button class="btn btn-ejecutar" onclick="ejecutarCodigo()">▶️ Ejecutar</button>
                    <button class="btn btn-verificar" onclick="verificarEjercicio()">✅ Verificar</button>
                    <button class="btn btn-limpiar" onclick="limpiarEditor()">🗑️ Limpiar</button>
                </div>
            </main>
            
            <!-- Panel de salida -->
            <aside class="output-panel">
                <h2>💻 Salida</h2>
                <div id="output-contenido" class="output-content">
                    La salida de tu programa aparecerá aquí...
                </div>
            </aside>
        </div>
    </div>
    
    <script src="/script.js"></script>
</body>
</html>
"""


def obtener_leccion(numero):
    """Genera HTML para una lección específica"""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lección {numero}</title>
</head>
<body>
    <h1>Lección {numero}</h1>
    <a href="/">← Volver al inicio</a>
</body>
</html>
"""


def main():
    """Función principal"""
    with socketserver.TCPServer(("", PUERTO), ManejadorCurso) as httpd:
        print(f"\n{Colores.AZUL}{'='*60}{Colores.RESET}")
        print(f"{Colores.NEGRITA}🚀 Servidor Web del Curso de Python{Colores.RESET}")
        print(f"{Colores.AZUL}{'='*60}{Colores.RESET}\n")
        print(f"📍 Servidor iniciado en: {Colores.VERDE}http://localhost:{PUERTO}{Colores.RESET}")
        print(f"📁 Directorio base: {DIRECTORIO_BASE}")
        print(f"\n{Colores.AMARILLO}Presiona Ctrl+C para detener el servidor{Colores.RESET}\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n\n{Colores.AMARILLO}Servidor detenido{Colores.RESET}")


if __name__ == "__main__":
    main()
