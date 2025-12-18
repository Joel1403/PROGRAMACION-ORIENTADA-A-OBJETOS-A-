# tienda_virtual.py
# Ejemplo del mundo real: Tienda virtual usando Programación Orientada a Objetos

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.reducir_stock(cantidad):
            self.productos.append((producto, cantidad))
            print(f"{producto.nombre} agregado al carrito")
        else:
            print(f"No hay stock suficiente de {producto.nombre}")

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos:
            total += producto.precio * cantidad
        return total


if __name__ == "__main__":
    producto1 = Producto("Laptop", 800, 5)
    producto2 = Producto("Mouse", 20, 10)

    carrito = Carrito()
    carrito.agregar_producto(producto1, 1)
    carrito.agregar_producto(producto2, 2)

    print("Total a pagar:", carrito.calcular_total())
