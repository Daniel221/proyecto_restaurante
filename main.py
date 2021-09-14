from Mesa import Mesa
from Bebida import Bebida
from platillo import Platillo
from Persona import Persona

sprite = Bebida("Sprite", 1.2, 30)
coca = Bebida("coca-cola", 1, 20)
pizza = Platillo(20, "pizza", 1.3)

juan = Persona()
juan.addItem(sprite)
juan.addItem(coca)
juan.addItem(pizza)

pedro = Persona()
pedro.addItem(sprite)
pedro.addItem(coca)

mesa1 = Mesa()
mesa1.addPersona(pedro)
mesa1.addPersona(juan)
print(mesa1.obtenerTotal())