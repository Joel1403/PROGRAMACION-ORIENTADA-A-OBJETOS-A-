# sistema_reservas.py
# Ejemplo del mundo real: Sistema de reservas de hotel usando POO

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        self.disponible = True


class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula


class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar_reserva(self):
        if self.habitacion.reservar():
            print(f"Reserva confirmada para {self.cliente.nombre}")
            print(f"Habitación: {self.habitacion.numero} - Tipo: {self.habitacion.tipo}")
        else:
            print("La habitación no está disponible")


if __name__ == "__main__":
    habitacion1 = Habitacion(101, "Doble", 50)
    cliente1 = Cliente("Carlos Pérez", "0102030405")
    reserva1 = Reserva(cliente1, habitacion1)

    reserva1.confirmar_reserva()
