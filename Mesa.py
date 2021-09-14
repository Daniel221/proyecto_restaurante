from Persona import Persona

class Mesa:
  def __init__(self):
    self.personas = []

  def __str__(self):
    salida = ''
    for item in self.personas:
      salida += f'{item}\n'
    return salida

  def obtenerTotal(self) -> float:
    total = 0.0
    for persona in self.personas:
      total += persona.total()
    
    return total
  
  def addPersona(self, persona:Persona):
    self.personas.append(persona)
  



