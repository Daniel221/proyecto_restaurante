from MenuItem import MenuItem

class Persona:
  def __init__(self):
    self._orden = []
    self._total = 0.0

  def addItem(self, item:MenuItem) -> float:
    self._orden.append(item)
    self._total += item.get_precio()

  def __str__(self):
    salida = ''
    for item in self._orden:
      salida += f'{item}\n'
    return salida

    #return '\n'.join(self.orden)

  def total(self):
    return self._total

  