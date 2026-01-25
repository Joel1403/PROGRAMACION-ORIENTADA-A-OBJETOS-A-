class Archivo:
    """
    Modelo que representa un archivo del sistema.
    """

    def __init__(self, nombre, modo='w'):
        """
        Constructor (__init__):
        Inicializa el objeto y abre un archivo en el sistema.
        Define el estado inicial y los datos obligatorios.
        """
        self.nombre = nombre
        self.modo = modo
        self.archivo = open(self.nombre, self.modo)
        print(f"[INIT] Archivo '{self.nombre}' abierto en modo '{self.modo}'.")

    def escribir(self, texto):
        """
        Escribe texto en el archivo si está abierto.
        """
        if not self.archivo.closed:
            self.archivo.write(texto + '\n')

    def __del__(self):
        """
        Destructor (__del__):
        Libera el recurso cerrando el archivo.
        Puede ejecutarse al eliminar el objeto o al finalizar el programa.
        """
        try:
            if hasattr(self, 'archivo') and not self.archivo.closed:
                self.archivo.close()
                print(f"[DEL] Archivo '{self.nombre}' cerrado correctamente.")
        except Exception as e:
            print(f"[DEL] Error al cerrar el archivo: {e}")
