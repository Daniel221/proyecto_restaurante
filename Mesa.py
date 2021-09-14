from Persona import Persona

class Mesa:
  def __init__(self):
    self.personas = []

  def __str__(self):
    salida = ''
    for item in self.personas:
      print(item._total)
    return 'hola'

  def obtenerTotal(self) -> float:
    total = 0.0
    for persona in self.personas:
      total += persona._total
    
    return total
  
  def addPersona(self, persona:Persona):
    self.personas.append(Persona)
  



