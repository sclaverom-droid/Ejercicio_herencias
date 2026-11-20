# Un cliente compra un producto
# Crear la clase Cliente (heredada de Persona)
# Crear la clase Producto
# Definir comprar_producto(cliente, producto, uds)


# Creo la superclase
class Persona:
    def __init__(self, nombre_persona):
        self.nombre = nombre_persona


# Creo la clase Cliente que hereda de Persona
class Cliente(Persona):
    def __init__(self, nombre_cliente):
        super().__init__(nombre_cliente)


# Creo la clase Producto
class Producto:
    def __init__(self, nombre_producto, precio_producto):
        self.nombre = nombre_producto
        self.precio = precio_producto


# Creo la función para comprar productos
def comprar_producto(cliente, producto, uds):
    total = producto.precio * uds

    print("El cliente", cliente.nombre, "ha comprado", uds,
          producto.nombre)
    print("El precio total es:", total, "euros")


# Creo los objetos
cliente1 = Cliente("Juan")

producto1 = Producto("Ordenador", 500)

# Realizo la compra
comprar_producto(cliente1, producto1, 2)