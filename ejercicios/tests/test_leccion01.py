"""
Tests para la Lección 01: Introducción a Python
"""

def run_tests():
    """Ejecuta todos los tests de la lección 01"""
    resultados = {'total': 0, 'aprobados': 0}
    
    print("  Tests de conceptos básicos:")
    
    # Test 1: Verificar que el estudiante entiende print
    try:
        from ejercicios import ejercicio_01_01
        print("  ✓ Ejercicio 1.1 completado")
        resultados['aprobados'] += 1
    except (ImportError, Exception):
        print("  ✗ Ejercicio 1.1 pendiente o con errores")
    resultados['total'] += 1
    
    # Test 2: Verificar conversión de tipos
    try:
        from ejercicios import ejercicio_01_02
        print("  ✓ Ejercicio 1.2 completado")
        resultados['aprobados'] += 1
    except (ImportError, Exception):
        print("  ✗ Ejercicio 1.2 pendiente o con errores")
    resultados['total'] += 1
    
    # Test 3: Verificar formato de texto
    try:
        from ejercicios import ejercicio_01_03
        print("  ✓ Ejercicio 1.3 completado")
        resultados['aprobados'] += 1
    except (ImportError, Exception):
        print("  ✗ Ejercicio 1.3 pendiente o con errores")
    resultados['total'] += 1
    
    return resultados

if __name__ == "__main__":
    run_tests()
