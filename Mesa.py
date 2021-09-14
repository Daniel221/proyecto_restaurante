from Persona import Persona

class Mesa:
  def __init__(self):
    self.personas = []

  def obtenerTotal(self) -> float:
    total = 0
    for persona in self.personas:
      total += persona.total
    
    return total
  
  def addPersona(self, persona:Persona):
    self.personas.append(Persona)
  



