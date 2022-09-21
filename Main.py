class Vehiculo():
    color="Rojo"
    ruedas=4
    puertas=4

    def cambiarRuedas(self):
        pass
class Coche(Vehiculo):
    velocidad=100
    cilindrada=2.0

    def acelerar(self,cambioVelocidad):
        velocidad=self.velocidad
        velocidad+=cambioVelocidad

auto=Coche()
auto.color="Negro"
print("El color del auto es: ",auto.color)
print("El auto tiene :",auto.ruedas," ruedas")
print("El auto tiene ",auto.puertas," puertas")
print("El auto tiene una velocidad maxima de: ",auto.velocidad,"KM/H")
print("El auto tiene cilindrada de ", auto.cilindrada,"lts")

