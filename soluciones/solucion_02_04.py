"""
Solución Ejercicio 2.4: Operaciones con strings
"""

texto = "Python es increíble"

# 1. Convertir a mayúsculas
mayusculas = texto.upper()
print(f"Mayúsculas: {mayusculas}")

# 2. Convertir a minúsculas
minusculas = texto.lower()
print(f"Minúsculas: {minusculas}")

# 3. Contar letra 'e'
veces_e = texto.count('e')
print(f"La letra 'e' aparece {veces_e} veces")

# 4. Reemplazar palabra
nuevo_texto = texto.replace("increíble", "fantástico")
print(f"Texto modificado: {nuevo_texto}")
