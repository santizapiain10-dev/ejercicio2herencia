class Figura(object):

    def __init__(self):
        self.nombre = ""
        self.color = ""

    def leerDatosFigura(self):
        self.nombre = input("Forma: ")
        self.color = input("Color: ")

    def mostrarDatosFigura(self):
        print("Forma:", self.nombre)
        print("Color:", self.color)