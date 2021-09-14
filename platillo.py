from MenuItem import MenuItem

class Platillo(MenuItem): 
    def __init__(self, precio: float, nombre: str, size: float) -> None:
        super().__init__()
        self.precio = precio
        self.nombre = nombre
        self.size = size

    def servir(self):
        return f'El platillo {self.nombre} se está sirviendo'

    def getPrecio(self):
        pass

    def __str__(self) -> str:
        return f'{super().__str__()}{self.nombre} - {self.precio}'
