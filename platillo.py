from MenuItem import MenuItem

class Platillo(MenuItem): 
    def __init__(self, precio: float, nombre: str, tamaño: float) -> None:
        super().__init__()
        self._precio = precio
        self.nombre = nombre
        self.tamaño = tamaño

    def servir(self):
        return f'El platillo {self.nombre} se está sirviendo'

    def get_precio(self):
        return self._precio * self.tamaño

    def __str__(self) -> str:
        return f'{self.nombre} - {self._precio}'
