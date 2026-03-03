from figuras.circulo import Circulo
from figuras.triangulo import Triangulo

def menuPrincipal():
    while True:
        print("Menu")
        print("1. Circulo")
        print("2. Triangulo")
        print("3. Salir")
        op = int(input("Ingrese una opcion: "))
        match(op):
            case 1:
                c = Circulo()
                c.leerDatosCirculo()
                c.mostrarDatosCirculo()
                print()
            case 2:
                t = Triangulo()
                t.leerDatosTriangulo()
                t.mostrarDatosTriangulo()
                print()
            case 3:
                print("Hasta despues")
                break
            case _:
                print("Ingrese una Opcion valida")