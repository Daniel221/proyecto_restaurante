from MenuItem import MenuItem

class Persona:
  def __init__(self):
    self._orden = []
    self._total = 0

  def addItem(self, item:MenuItem) -> float:
    self._orden.append(item)
    self._total += item.getPrecio

  @property
  def total(self):
    return self.total

  