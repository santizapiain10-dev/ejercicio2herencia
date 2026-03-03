from figuras.circulo import Circulo
from figuras.triangulo import Triangulo

def main():

    print("CÍRCULO")
    c = Circulo()
    c.leerDatosCirculo()
    c.mostrarDatosCirculo()

    print("TRIÁNGULO")
    t = Triangulo()
    t.leerDatosTriangulo()
    t.mostrarDatosTriangulo()