#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicación Web para el Curso de Python
Terminal interactiva con ejercicios autocorregibles
"""

from flask import Flask, render_template_string, request, jsonify
import subprocess
import sys
import os
import json

app = Flask(__name__)

# Plantilla HTML completa
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🐍 Curso Completo de Python</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Consolas', 'Monaco', monospace;
            background: #1e1e1e;
            color: #d4d4d4;
            min-height: 100vh;
        }
        
        .header {
            background: linear-gradient(135deg, #0e639c 0%, #007acc 100%);
            padding: 20px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        
        .header h1 {
            color: #ffffff;
            font-size: 28px;
            margin-bottom: 10px;
        }
        
        .header p {
            color: #4fc3f7;
            font-size: 14px;
        }
        
        .tabs {
            display: flex;
            background: #2d2d2d;
            padding: 10px 20px 0;
            gap: 5px;
        }
        
        .tab {
            padding: 12px 24px;
            background: #1e1e1e;
            border: none;
            color: #888;
            cursor: pointer;
            border-radius: 8px 8px 0 0;
            font-size: 14px;
            transition: all 0.3s;
        }
        
        .tab:hover {
            background: #252526;
            color: #fff;
        }
        
        .tab.active {
            background: #1e1e1e;
            color: #4fc3f7;
            border-bottom: 2px solid #4fc3f7;
        }
        
        .tab-content {
            display: none;
            padding: 20px;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .editor-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            height: calc(100vh - 250px);
            min-height: 500px;
        }
        
        .panel {
            background: #252526;
            border-radius: 8px;
            padding: 15px;
            display: flex;
            flex-direction: column;
            border: 1px solid #3c3c3c;
        }
        
        .panel-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            padding-bottom: 10px;
            border-bottom: 1px solid #3c3c3c;
        }
        
        .panel-title {
            color: #4fc3f7;
            font-weight: bold;
            font-size: 14px;
        }
        
        .editor-container {
            flex: 1;
            position: relative;
        }
        
        #codeEditor {
            width: 100%;
            height: 100%;
            background: #1e1e1e;
            color: #d4d4d4;
            border: none;
            padding: 15px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 14px;
            resize: none;
            outline: none;
            line-height: 1.5;
            border-radius: 4px;
        }
        
        #codeEditor:focus {
            box-shadow: 0 0 0 2px #007acc;
        }
        
        .output-container {
            flex: 1;
            background: #000000;
            border-radius: 4px;
            padding: 15px;
            overflow-y: auto;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 13px;
            color: #00ff00;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        
        .output-error {
            color: #ff4444 !important;
        }
        
        .output-success {
            color: #00ff00 !important;
        }
        
        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            font-weight: bold;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #2da042 0%, #3cb043 100%);
            color: white;
        }
        
        .btn-primary:hover {
            background: linear-gradient(135deg, #3cb043 0%, #4bc053 100%);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(45, 160, 66, 0.4);
        }
        
        .btn-secondary {
            background: #6c6c6c;
            color: white;
        }
        
        .btn-secondary:hover {
            background: #7c7c7c;
        }
        
        .btn-warning {
            background: #d4a017;
            color: black;
        }
        
        .btn-warning:hover {
            background: #e4b027;
        }
        
        .input-simulador {
            background: #2d2d2d;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
        }
        
        .input-item {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
        }
        
        .input-item label {
            color: #4fc3f7;
            font-size: 13px;
            min-width: 80px;
        }
        
        .input-item input {
            flex: 1;
            background: #3c3c3c;
            border: 1px solid #555;
            color: #fff;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 13px;
            outline: none;
        }
        
        .input-item input:focus {
            border-color: #007acc;
        }
        
        .btn-small {
            padding: 5px 10px;
            font-size: 12px;
        }
        
        .btn-danger {
            background: #f44336;
            color: white;
        }
        
        .actions {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        
        .exercise-selector {
            background: #2d2d2d;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .exercise-selector select {
            background: #3c3c3c;
            border: 1px solid #555;
            color: #fff;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 14px;
            margin-right: 10px;
        }
        
        .enunciado {
            background: #2d2d2d;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid #4fc3f7;
        }
        
        .enunciado h3 {
            color: #4fc3f7;
            margin-bottom: 10px;
        }
        
        .progress-section {
            background: #252526;
            padding: 30px;
            border-radius: 8px;
            text-align: center;
        }
        
        .progress-bar-container {
            background: #3c3c3c;
            border-radius: 20px;
            height: 30px;
            margin: 20px auto;
            max-width: 600px;
            overflow: hidden;
        }
        
        .progress-bar {
            background: linear-gradient(90deg, #4fc3f7 0%, #007acc 100%);
            height: 100%;
            border-radius: 20px;
            transition: width 0.5s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .stat-card {
            background: #2d2d2d;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        
        .stat-number {
            font-size: 36px;
            color: #4fc3f7;
            font-weight: bold;
        }
        
        .stat-label {
            color: #888;
            margin-top: 5px;
        }
        
        .welcome-message {
            background: linear-gradient(135deg, #1e3a5f 0%, #0e639c 100%);
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .welcome-message h2 {
            color: #fff;
            margin-bottom: 15px;
        }
        
        .welcome-message p {
            color: #4fc3f7;
            line-height: 1.6;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }
        
        .feature-card {
            background: #2d2d2d;
            padding: 20px;
            border-radius: 8px;
            text-align: left;
        }
        
        .feature-icon {
            font-size: 24px;
            margin-bottom: 10px;
        }
        
        .feature-title {
            color: #4fc3f7;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .feature-desc {
            color: #888;
            font-size: 13px;
            line-height: 1.5;
        }
        
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1e1e1e;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #424242;
            border-radius: 5px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🐍 Curso Completo de Python - Desde Cero hasta Experto</h1>
        <p>Aprende Python con ejercicios prácticos y terminal interactiva</p>
    </div>
    
    <div class="tabs">
        <button class="tab active" onclick="showTab('terminal')">🔧 Terminal Libre</button>
        <button class="tab" onclick="showTab('ejercicios')">📚 Ejercicios del Curso</button>
        <button class="tab" onclick="showTab('progreso')">📊 Mi Progreso</button>
    </div>
    
    <div class="container">
        <!-- Pestaña Terminal Libre -->
        <div id="terminal" class="tab-content active">
            <div class="welcome-message">
                <h2>¡Bienvenido a la Terminal Libre! 🚀</h2>
                <p>Escribe cualquier código Python y ejecútalo instantáneamente. 
                   Usa la sección de inputs si tu código necesita datos del usuario.</p>
            </div>
            
            <div class="editor-section">
                <div class="panel">
                    <div class="panel-header">
                        <span class="panel-title">📝 Editor de Código</span>
                    </div>
                    <div class="editor-container">
                        <textarea id="codeEditor" placeholder="Escribe tu código Python aquí..."># ¡Bienvenido a la Terminal Libre! 🐍
# Prueba este código o escribe el tuyo propio:

nombre = "Estudiante"
print(f"¡Hola {nombre}!")
print("Este es tu espacio para experimentar")
print("")
print("Prueba con:")
print("- Variables")
print("- Operaciones matemáticas") 
print("- Bucles y condicionales")
print("- Funciones")
</textarea>
                    </div>
                    
                    <div class="input-simulador">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <span style="color: #4fc3f7; font-weight: bold;">📥 Inputs Simulados (para input())</span>
                            <button class="btn btn-secondary btn-small" onclick="agregarInput()">+ Agregar Input</button>
                        </div>
                        <div id="inputsContainer"></div>
                    </div>
                    
                    <div class="actions">
                        <button class="btn btn-primary" onclick="ejecutarCodigo()">
                            ▶ EJECUTAR
                        </button>
                        <button class="btn btn-secondary" onclick="limpiarTerminal()">
                            🗑 Limpiar
                        </button>
                    </div>
                </div>
                
                <div class="panel">
                    <div class="panel-header">
                        <span class="panel-title">💻 Salida</span>
                    </div>
                    <div id="outputTerminal" class="output-container">
                        ╔═══════════════════════════════════════════════════════════╗
                        ║     🐍 ¡BIENVENIDO AL CURSO COMPLETO DE PYTHON! 🐍       ║
                        ╠═══════════════════════════════════════════════════════════╣
                        ║                                                           ║
                        ║  Tienes acceso a:                                         ║
                        ║  ✅ Terminal Libre para tus pruebas                       ║
                        ║  ✅ Ejercicios autocorregibles por lección                ║
                        ║  ✅ Seguimiento de tu progreso                            ║
                        ║                                                           ║
                        ║  Comienza con la Lección 1 en la pestaña                  ║
                        ║  "Ejercicios del Curso"                                   ║
                        ║                                                           ║
                        ║  ¡Mucho éxito en tu aprendizaje! 🚀                       ║
                        ╚═══════════════════════════════════════════════════════════╝
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Pestaña Ejercicios -->
        <div id="ejercicios" class="tab-content">
            <div class="exercise-selector">
                <label style="color: #4fc3f7; margin-right: 10px;">Selecciona Lección:</label>
                <select id="leccionSelector">
                    <option value="0">Lección 1: Introducción</option>
                    <option value="1">Lección 2: Variables</option>
                    <option value="2">Lección 3: Operadores</option>
                    <option value="3">Lección 4: Entrada/Salida</option>
                </select>
                <button class="btn btn-primary" onclick="cargarEjercicio()">Cargar Ejercicio</button>
            </div>
            
            <div id="enunciadoContainer" class="enunciado" style="display: none;">
                <h3>📝 Enunciado</h3>
                <p id="enunciadoTexto"></p>
            </div>
            
            <div class="editor-section" id="ejercicioEditorSection" style="display: none;">
                <div class="panel">
                    <div class="panel-header">
                        <span class="panel-title">✏️ Tu Solución</span>
                    </div>
                    <div class="editor-container">
                        <textarea id="codigoEjercicio" placeholder="Escribe tu solución aquí..."></textarea>
                    </div>
                    
                    <div class="input-simulador">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <span style="color: #4fc3f7; font-weight: bold;">📥 Inputs (si el ejercicio usa input())</span>
                            <button class="btn btn-secondary btn-small" onclick="agregarInputEjercicio()">+ Agregar Input</button>
                        </div>
                        <div id="inputsEjercicioContainer"></div>
                    </div>
                    
                    <div class="actions">
                        <button class="btn btn-primary" onclick="verificarEjercicio()">
                            ✅ Verificar Solución
                        </button>
                        <button class="btn btn-warning" onclick="verSolucion()">
                            💡 Ver Solución
                        </button>
                    </div>
                </div>
                
                <div class="panel">
                    <div class="panel-header">
                        <span class="panel-title">📋 Resultado</span>
                    </div>
                    <div id="outputEjercicio" class="output-container">
                        Selecciona una lección y carga un ejercicio para comenzar.
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Pestaña Progreso -->
        <div id="progreso" class="tab-content">
            <div class="progress-section">
                <h2 style="color: #4fc3f7; margin-bottom: 20px;">📊 Tu Progreso en el Curso</h2>
                
                <div class="progress-bar-container">
                    <div id="progressBar" class="progress-bar" style="width: 0%;">0%</div>
                </div>
                
                <div class="stats">
                    <div class="stat-card">
                        <div id="statCompletados" class="stat-number">0</div>
                        <div class="stat-label">Ejercicios Completados</div>
                    </div>
                    <div class="stat-card">
                        <div id="statTotal" class="stat-number">24</div>
                        <div class="stat-label">Total Ejercicios</div>
                    </div>
                    <div class="stat-card">
                        <div id="statLeccion" class="stat-number">1</div>
                        <div class="stat-label">Lección Actual</div>
                    </div>
                </div>
                
                <div style="margin-top: 30px;">
                    <button class="btn btn-secondary" onclick="reiniciarProgreso()">
                        🔄 Reiniciar Progreso
                    </button>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Variables globales
        let solucionActual = '';
        let progreso = JSON.parse(localStorage.getItem('progresoPython')) || { ejercicios: [], leccion: 1 };
        
        // Mostrar pestaña
        function showTab(tabName) {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            
            event.target.classList.add('active');
            document.getElementById(tabName).classList.add('active');
            
            if (tabName === 'progreso') {
                actualizarProgreso();
            }
        }
        
        // Agregar input simulado
        function agregarInput() {
            const container = document.getElementById('inputsContainer');
            const count = container.children.length + 1;
            
            const div = document.createElement('div');
            div.className = 'input-item';
            div.innerHTML = `
                <label>Input #${count}:</label>
                <input type="text" class="simulated-input" placeholder="Valor que devolverá input()">
                <button class="btn btn-danger btn-small" onclick="this.parentElement.remove()">×</button>
            `;
            container.appendChild(div);
        }
        
        function agregarInputEjercicio() {
            const container = document.getElementById('inputsEjercicioContainer');
            const count = container.children.length + 1;
            
            const div = document.createElement('div');
            div.className = 'input-item';
            div.innerHTML = `
                <label>Input #${count}:</label>
                <input type="text" class="simulated-input-ej" placeholder="Valor que devolverá input()">
                <button class="btn btn-danger btn-small" onclick="this.parentElement.remove()">×</button>
            `;
            container.appendChild(div);
        }
        
        // Ejecutar código
        async function ejecutarCodigo() {
            const codigo = document.getElementById('codeEditor').value;
            const inputs = Array.from(document.querySelectorAll('.simulated-input')).map(i => i.value);
            
            const outputDiv = document.getElementById('outputTerminal');
            outputDiv.innerHTML = '⏳ Ejecutando...';
            
            try {
                const response = await fetch('/ejecutar', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ codigo, inputs })
                });
                
                const resultado = await response.json();
                
                let html = '';
                if (resultado.salida) {
                    html += '<div class="output-success">=== SALIDA ===\\n' + escapeHtml(resultado.salida) + '</div>';
                }
                if (resultado.error) {
                    html += '<div class="output-error">\\n=== ERROR ===\\n' + escapeHtml(resultado.error) + '</div>';
                }
                html += '\\n=== EJECUCIÓN FINALIZADA ===';
                
                outputDiv.innerHTML = html.replace(/\\n/g, '<br>');
            } catch (error) {
                outputDiv.innerHTML = '<div class="output-error">❌ Error de conexión: ' + error.message + '</div>';
            }
        }
        
        // Limpiar terminal
        function limpiarTerminal() {
            document.getElementById('codeEditor').value = '';
            document.getElementById('outputTerminal').innerHTML = '';
            document.getElementById('inputsContainer').innerHTML = '';
        }
        
        // Cargar ejercicio
        function cargarEjercicio() {
            const indice = document.getElementById('leccionSelector').value;
            const ejercicios = {
                0: {
                    enunciado: "Ejercicio 1: Escribe un programa que muestre tu nombre en pantalla usando print().",
                    codigo: "# Escribe tu código aquí\\n\\n",
                    solucion: 'print("Tu Nombre")'
                },
                1: {
                    enunciado: "Ejercicio 2: Crea tres variables (nombre, edad, altura) e imprímelas.",
                    codigo: "# Crea tus variables aquí\\n\\n",
                    solucion: 'nombre = "Ana"\\nedad = 25\\naltura = 1.68\\n\\nprint(nombre)\\nprint(edad)\\nprint(altura)'
                },
                2: {
                    enunciado: "Ejercicio 3: Realiza una suma y una multiplicación, luego muestra los resultados.",
                    codigo: "# Realiza operaciones aquí\\n\\n",
                    solucion: 'suma = 15 + 27\\nmultiplicacion = 8 * 7\\n\\nprint(f"Suma: {suma}")\\nprint(f"Multiplicación: {multiplicacion}")'
                },
                3: {
                    enunciado: "Ejercicio 4: Pide al usuario su nombre y ciudad, luego salúdalo personalmente.",
                    codigo: "# Usa input() para pedir datos\\n\\n",
                    solucion: 'nombre = input("¿Cuál es tu nombre? ")\\nciudad = input("¿En qué ciudad vives? ")\\n\\nprint(f"¡Hola {nombre}! Bienvenido desde {ciudad}")'
                }
            };
            
            const ej = ejercicios[indice];
            solucionActual = ej.solucion;
            
            document.getElementById('enunciadoContainer').style.display = 'block';
            document.getElementById('enunciadoTexto').textContent = ej.enunciado;
            document.getElementById('ejercicioEditorSection').style.display = 'block';
            document.getElementById('codigoEjercicio').value = ej.codigo;
            document.getElementById('outputEjercicio').innerHTML = 'Escribe tu solución y presiona "Verificar Solución"';
            document.getElementById('inputsEjercicioContainer').innerHTML = '';
        }
        
        // Verificar ejercicio
        async function verificarEjercicio() {
            const codigo = document.getElementById('codigoEjercicio').value;
            const inputs = Array.from(document.querySelectorAll('.simulated-input-ej')).map(i => i.value);
            
            const outputDiv = document.getElementById('outputEjercicio');
            outputDiv.innerHTML = '⏳ Verificando...';
            
            try {
                const response = await fetch('/ejecutar', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ codigo, inputs })
                });
                
                const resultado = await response.json();
                
                let html = '';
                if (resultado.error) {
                    html += '<div class="output-error">❌ Error en la ejecución:\\n' + escapeHtml(resultado.error) + '</div>';
                } else {
                    html += '<div class="output-success">✅ ¡Código ejecutado correctamente!\\n\\n';
                    html += '=== TU SALIDA ===\\n' + escapeHtml(resultado.salida || '') + '</div>';
                    
                    if (resultado.salida && resultado.salida.trim().length > 0) {
                        html += '\\n\\n✅ ¡Excelente! Tu código produce salida.';
                        html += '\\n💡 Compara tu salida con lo que esperabas.';
                        
                        // Guardar progreso
                        guardarProgreso('Ejercicio completado');
                    } else {
                        html += '\\n\\n⚠️ Tu código no produjo salida visible.';
                    }
                }
                
                outputDiv.innerHTML = html.replace(/\\n/g, '<br>');
            } catch (error) {
                outputDiv.innerHTML = '<div class="output-error">❌ Error: ' + error.message + '</div>';
            }
        }
        
        // Ver solución
        function verSolucion() {
            if (confirm('¿Estás seguro de que quieres ver la solución?\\n\\nIntenta primero resolverlo por ti mismo.')) {
                document.getElementById('codigoEjercicio').value = solucionActual.replace(/\\n/g, '\\n');
            }
        }
        
        // Guardar progreso
        function guardarProgreso(ejercicio) {
            if (!progreso.ejercicios.includes(ejercicio)) {
                progreso.ejercicios.push(ejercicio);
                localStorage.setItem('progresoPython', JSON.stringify(progreso));
            }
        }
        
        // Actualizar progreso
        function actualizarProgreso() {
            const total = 24;
            const completados = progreso.ejercicios.length;
            const porcentaje = Math.round((completados / total) * 100);
            
            document.getElementById('progressBar').style.width = porcentaje + '%';
            document.getElementById('progressBar').textContent = porcentaje + '%';
            document.getElementById('statCompletados').textContent = completados;
            document.getElementById('statLeccion').textContent = Math.floor(completados / 6) + 1;
        }
        
        // Reiniciar progreso
        function reiniciarProgreso() {
            if (confirm('¿Estás seguro de que quieres reiniciar todo tu progreso?\\n\\nEsta acción no se puede deshacer.')) {
                progreso = { ejercicios: [], leccion: 1 };
                localStorage.setItem('progresoPython', JSON.stringify(progreso));
                actualizarProgreso();
                alert('🔄 Progreso reiniciado');
            }
        }
        
        // Escape HTML
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        // Inicializar
        actualizarProgreso();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    data = request.get_json()
    codigo = data.get('codigo', '')
    inputs = data.get('inputs', [])
    
    # Preparar script con inputs simulados
    script = codigo
    
    try:
        resultado = subprocess.run(
            [sys.executable, '-c', script],
            capture_output=True,
            text=True,
            timeout=30,
            input='\n'.join(inputs) if inputs else None
        )
        
        return jsonify({
            'salida': resultado.stdout,
            'error': resultado.stderr
        })
    except subprocess.TimeoutExpired:
        return jsonify({
            'salida': '',
            'error': '❌ TIMEOUT: El código tardó demasiado en ejecutarse (>30s)'
        })
    except Exception as e:
        return jsonify({
            'salida': '',
            'error': f'❌ ERROR: {str(e)}'
        })

if __name__ == '__main__':
    print("=" * 60)
    print("🐍 CURSO COMPLETO DE PYTHON - SERVIDOR WEB")
    print("=" * 60)
    print("\n📍 Abre tu navegador en: http://localhost:5000")
    print("\n✨ Características:")
    print("   - Terminal libre para pruebas")
    print("   - Ejercicios autocorregibles")
    print("   - Seguimiento de progreso")
    print("   - Soporte para input() simulado")
    print("\n⚠️  Presiona Ctrl+C para detener el servidor\n")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=False)
