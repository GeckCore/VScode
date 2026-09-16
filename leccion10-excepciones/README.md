# Lección 10: Excepciones

## 📖 Manejo de Errores

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Siempre se ejecuta")
```

## ➡️ Siguiente Lección

[Lección 11: Módulos y Paquetes](../leccion11-modulos-paquetes/)
