#!/usr/bin/env python3
"""
Sistema de Tests Autocorregibles para el Curso de Python

Uso:
    python ejercicios/run_tests.py              # Ejecutar todos los tests
    python ejercicios/run_tests.py leccion01    # Ejecutar tests de una lección
"""

import sys
import os
import importlib.util

# Colores para la salida
class Colores:
    VERDE = '\033[92m'
    ROJO = '\033[91m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    RESET = '\033[0m'
    NEGRITA = '\033[1m'

def imprimir_header():
    print(f"\n{Colores.AZUL}{'='*60}{Colores.RESET}")
    print(f"{Colores.NEGRITA}🧪 SISTEMA DE TESTS AUTOCORREGIBLES{Colores.RESET}")
    print(f"{Colores.AZUL}{'='*60}{Colores.RESET}\n")

def cargar_modulo(ruta_archivo, nombre_modulo):
    """Carga un módulo Python desde una ruta"""
    if not os.path.exists(ruta_archivo):
        return None
    
    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
    modulo = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(modulo)
        return modulo
    except Exception as e:
        return None

def test_ejercicio(nombre_test, funcion_test, args_esperados, resultado_esperado):
    """Ejecuta un test individual"""
    try:
        resultado = funcion_test(*args_esperados)
        if resultado == resultado_esperado:
            print(f"  {Colores.VERDE}✓{Colores.RESET} {nombre_test}")
            return True
        else:
            print(f"  {Colores.ROJO}✗{Colores.RESET} {nombre_test}")
            print(f"      Esperado: {resultado_esperado}")
            print(f"      Obtenido: {resultado}")
            return False
    except Exception as e:
        print(f"  {Colores.ROJO}✗{Colores.RESET} {nombre_test} (Error: {e})")
        return False

def ejecutar_tests_leccion(leccion):
    """Ejecuta todos los tests de una lección"""
    carpeta_tests = os.path.join(os.path.dirname(__file__), 'tests')
    archivo_tests = f"test_{leccion}.py"
    ruta_tests = os.path.join(carpeta_tests, archivo_tests)
    
    if not os.path.exists(ruta_tests):
        print(f"  {Colores.AMARILLO}⚠ No hay tests definidos para {leccion}{Colores.RESET}")
        return None
    
    modulo_tests = cargar_modulo(ruta_tests, f"test_{leccion}")
    if not modulo_tests:
        print(f"  {Colores.ROJO}✗ Error al cargar tests para {leccion}{Colores.RESET}")
        return None
    
    # Ejecutar función main si existe
    if hasattr(modulo_tests, 'run_tests'):
        return modulo_tests.run_tests()
    
    return None

def main():
    imprimir_header()
    
    # Determinar qué tests ejecutar
    if len(sys.argv) > 1:
        lecciones = sys.argv[1:]
    else:
        # Ejecutar todas las lecciones disponibles
        lecciones = [
            'leccion01', 'leccion02', 'leccion03', 'leccion04',
            'leccion05', 'leccion06', 'leccion07', 'leccion08',
            'leccion09', 'leccion10', 'leccion11', 'leccion12'
        ]
    
    resultados = {}
    
    for leccion in lecciones:
        print(f"{Colores.NEGRITA}{leccion}:{Colores.RESET}")
        resultado = ejecutar_tests_leccion(leccion)
        
        if resultado is not None:
            resultados[leccion] = resultado
            total = resultado.get('total', 0)
            aprobados = resultado.get('aprobados', 0)
            
            if total > 0:
                porcentaje = (aprobados / total) * 100
                color = Colores.VERDE if porcentaje == 100 else Colores.AMARILLO if porcentaje >= 50 else Colores.ROJO
                print(f"  {color}{aprobados}/{total} tests aprobados ({porcentaje:.0f}%){Colores.RESET}\n")
        else:
            print(f"  {Colores.AMARILLO}Sin tests disponibles{Colores.RESET}\n")
    
    # Resumen final
    print(f"\n{Colores.AZUL}{'='*60}{Colores.RESET}")
    print(f"{Colores.NEGRITA}📊 RESUMEN{Colores.RESET}")
    print(f"{Colores.AZUL}{'='*60}{Colores.RESET}")
    
    if resultados:
        total_general = sum(r.get('total', 0) for r in resultados.values())
        aprobados_general = sum(r.get('aprobados', 0) for r in resultados.values())
        
        if total_general > 0:
            porcentaje_general = (aprobados_general / total_general) * 100
            print(f"Tests aprobados: {aprobados_general}/{total_general} ({porcentaje_general:.1f}%)")
    
    print(f"\n{Colores.VERDE}¡Sigue practicando!{Colores.RESET}\n")

if __name__ == "__main__":
    main()
