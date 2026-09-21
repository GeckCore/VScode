# Lección 8 · Programación Orientada a Objetos (POO)

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion08-programacion-orientada-objetos/practica.ipynb)

## 🎯 Objetivos

- Entender qué son clases y objetos
- Crear clases con atributos (`__init__`) y métodos
- Reutilizar código con herencia
- Proteger datos con encapsulación y propiedades
- Usar `@dataclass` para clases de datos

---

## 1. La idea: objetos que combinan datos y comportamiento

Hasta ahora tenías datos (variables, listas) y comportamiento (funciones) por separado. La POO los une: un **objeto** es una entidad que tiene **datos** (atributos) y **acciones** (métodos). Piensa en un personaje de videojuego: tiene nombre, vida, nivel (datos) y puede atacar, curarse, subir de nivel (acciones).

Una **clase** es el molde; un **objeto** es una pieza construida con ese molde (también llamada *instancia*).

## 2. Tu primera clase

```python
class Perro:
    def __init__(self, nombre, raza):   # constructor: se ejecuta al crear el objeto
        self.nombre = nombre            # atributos: self.algo guarda el dato EN el objeto
        self.raza = raza

    def ladrar(self):                   # método: una función del objeto
        return f"{self.nombre} dice: ¡Guau!"


rex = Perro("Rex", "pastor")       # crear un objeto (instanciar)
toby = Perro("Toby", "caniche")    # otro objeto independiente

print(rex.nombre)       # Rex      (acceder a un atributo)
print(toby.ladrar())    # Toby dice: ¡Guau!   (llamar a un método)
```

Piezas clave:

- `__init__` es el **constructor**: se ejecuta automáticamente al crear el objeto (`Perro(...)`). Ahí se inicializan los atributos.
- `self` es una referencia **al propio objeto**. Es el primer parámetro de todos los métodos (Python lo rellena solo; tú no lo pasas al llamar: `rex.ladrar()`).
- Los **atributos** son variables pegadas al objeto: `self.nombre`. Cada objeto tiene los suyos: `rex.nombre` y `toby.nombre` son independientes.

## 3. Métodos que modifican el estado

```python
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return "Fondos insuficientes"
        self.saldo -= cantidad
        return self.saldo

cuenta = CuentaBancaria("Ana", 100)
cuenta.ingresar(50)
print(cuenta.saldo)            # 150
print(cuenta.retirar(500))     # Fondos insuficientes
```

Nótese cómo la lógica «no puedes retirar más de lo que hay» vive **dentro** del objeto. Nadie que use la clase puede romper esa regla por accidente. Eso es encapsular comportamiento.

## 4. `__str__`: cómo se imprime tu objeto

Si haces `print(cuenta)` verás algo feo como `<__main__.CuentaBancaria object at 0x...>`. Define `__str__` para darle una representación legible:

```python
class CuentaBancaria:
    ...
    def __str__(self):
        return f"Cuenta de {self.titular}: {self.saldo} €"

print(cuenta)   # Cuenta de Ana: 150 €
```

Los métodos con doble guion bajo (`__init__`, `__str__`, `__len__`…) se llaman **métodos especiales o dunder**. Python los invoca automáticamente en situaciones concretas (`print`, `len()`, operadores…).

## 5. Herencia: crear clases a partir de otras

Una clase hija **hereda** todos los atributos y métodos de la clase madre, y puede añadir o redefinir lo suyo:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

class Perro(Animal):                    # hereda de Animal
    def hablar(self):                   # sobrescribe (override) el método
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"

animales = [Perro("Rex"), Gato("Misu")]
for a in animales:
    print(a.hablar())    # cada uno habla a su manera: esto es POLIMORFISMO
```

Usa herencia cuando una clase **es un tipo de** otra (un Perro *es un* Animal). No la uses por ahorrar líneas si no hay relación lógica.

## 6. Encapsulación y propiedades

Marca atributos «internos» con un guion bajo inicial (`_vida`) y controla el acceso con **propiedades**:

```python
class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self._vida = 0
        self.vida = vida        # pasa por el setter (¡validación gratis!)

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = max(0, min(100, valor))   # la vida siempre entre 0 y 100

heroe = Personaje("Link", 150)
print(heroe.vida)   # 100 (el setter la recortó)
heroe.vida = -20
print(heroe.vida)   # 0 (nunca negativa)
```

El guion bajo `_vida` es una convención de «uso interno, no lo toques desde fuera». El doble guion `__vida` lo oculta aún más (name mangling).

## 7. `@dataclass`: clases de datos sin esfuerzo

Cuando una clase solo guarda datos, `dataclasses` te escribe el `__init__`, `__str__` y comparaciones automáticamente:

```python
from dataclasses import dataclass

@dataclass
class Punto:
    x: float
    y: float

p = Punto(3, 4)
print(p)              # Punto(x=3, y=4)  ← __str__ gratis
print(p == Punto(3, 4))  # True        ← comparación gratis
```

---

## ⚠️ Errores típicos

1. Olvidar `self` en la definición de métodos: `def ladrar():` en vez de `def ladrar(self):`.
2. Olvidar `self.` al usar atributos dentro de la clase: `nombre` (variable local) ≠ `self.nombre` (atributo).
3. Llamar al constructor como función suelta: es `Perro("Rex", "pastor")`, no `Perro.__init__(...)`.
4. Creer que `print` llama a tu método: sin `__str__` verás la dirección de memoria.

## 📝 Resumen

- Clase = molde; objeto = instancia. `__init__` inicializa, `self` es el propio objeto.
- Atributos = datos del objeto; métodos = sus acciones.
- `__str__` define cómo se imprime; `@dataclass` genera lo básico gratis.
- Herencia = «es un tipo de»; polimorfismo = mismo método, comportamiento distinto.
- Encapsula con `_atributo` + `@property` para validar.

## 🏋️ Práctica

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeckCore/VScode/blob/main/leccion08-programacion-orientada-objetos/practica.ipynb)

## ➡️ Siguiente paso

[Lección 9 · Manejo de archivos](../leccion09-manejo-archivos/)
