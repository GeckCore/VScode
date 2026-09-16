"""
Tests para la Lección 02: Variables y Tipos de Datos
"""

def run_tests():
    """Ejecuta todos los tests de la lección 02"""
    resultados = {'total': 0, 'aprobados': 0}
    
    print("  Tests de variables y tipos:")
    
    # Test 1: Calculadora de área
    try:
        from ejercicios import ejercicio_02_01
        print("  ✓ Ejercicio 2.1 completado")
        resultados['aprobados'] += 1
    except (ImportError, Exception):
        print("  ✗ Ejercicio 2.1 pendiente o con errores")
    resultados['total'] += 1
    
    # Test 2: Conversor de temperaturas
    try:
        from ejercicios import ejercicio_02_02
        print("  ✓ Ejercicio 2.2 completado")
        resultados['aprobados'] += 1
    except (ImportError, Exception):
        print("  ✗ Ejercicio 2.2 pendiente o con errores")
    resultados['total'] += 1
    
    # Test 3: Información personal
    try:
        from ejercicios import ejercicio_02_03
        print("  ✓ Ejercicio 2.3 completado")
        resultados['aprobados'] += 1
    except (ImportError, Exception):
        print("  ✗ Ejercicio 2.3 pendiente o con errores")
    resultados['total'] += 1
    
    # Test 4: Operaciones con strings
    try:
        from ejercicios import ejercicio_02_04
        print("  ✓ Ejercicio 2.4 completado")
        resultados['aprobados'] += 1
    except (ImportError, Exception):
        print("  ✗ Ejercicio 2.4 pendiente o con errores")
    resultados['total'] += 1
    
    return resultados

if __name__ == "__main__":
    run_tests()
