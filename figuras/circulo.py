import math
from figuras.figura import Figura

class Circulo(Figura):

    def __init__(self):
        super().__init__()
        self.radio = 0

    def leerDatosCirculo(self):
        self.leerDatosFigura()
        self.radio = float(input("Radio: "))

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

    def mostrarDatosCirculo(self):
        self.mostrarDatosFigura()
        print("Radio:", self.radio)
        print("Área:", round(self.calcularArea(), 2))