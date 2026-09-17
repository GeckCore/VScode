# Lección 07: Diccionarios y Conjuntos

## 📖 Diccionarios

Un diccionario es una colección de pares clave-valor.

```python
# Crear diccionarios
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

vacio = {}
```

### Acceder a valores
```python
print(persona["nombre"])      # "Juan"
print(persona.get("edad"))    # 30
print(persona.get("pais", "España"))  # "España" (default)
```

### Modificar diccionarios
```python
persona["edad"] = 31          # Modificar
persona["profesion"] = "Dev"  # Agregar
del persona["ciudad"]         # Eliminar
```

## 📚 Conjuntos (Sets)

Colección no ordenada de elementos únicos.

```python
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3])

frutas.add("uva")           # Agregar
frutas.remove("banana")     # Eliminar
```

## ➡️ Siguiente Lección

[Lección 08: Programación Orientada a Objetos](../leccion08-programacion-orientada-objetos/)
