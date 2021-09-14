from MenuItem import MenuItem


class Bebida(MenuItem):
    def __init__(self, nombre:str, tamaño:float, precio:float):
        self.nombre = nombre
        self.tamaño = tamaño
        self._precio = precio

    def __str__(self):
        return f'{self.nombre} - {self._precio}'

    def servir(self) -> str:
        return f'El platillo {self.nombre} se esta sirviendo'

    def get_precio(self):
        return self.tamaño * self._precio



