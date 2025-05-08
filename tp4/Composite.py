from abc import ABC, abstractmethod

class Pieza(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class PiezaSimple(Pieza):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def mostrar(self):
        print(f"Pieza: {self.nombre}")

class SubConjunto(Pieza):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.piezas = []

    def agregar(self, pieza: Pieza):
        self.piezas.append(pieza)

    def mostrar(self):
        print(f"Sub-conjunto: {self.nombre}")
        for pieza in self.piezas:
            pieza.mostrar()

class ProductoPrincipal:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.sub_conjuntos = []

    def agregar_subconjunto(self, subconjunto: SubConjunto):
        self.sub_conjuntos.append(subconjunto)

    def mostrar(self):
        print(f"Producto Principal: {self.nombre}")
        for subconjunto in self.sub_conjuntos:
            subconjunto.mostrar()

if __name__ == "__main__":
    pieza1 = PiezaSimple("Pieza 1")
    pieza2 = PiezaSimple("Pieza 2")
    pieza3 = PiezaSimple("Pieza 3")
    pieza4 = PiezaSimple("Pieza 4")
    pieza5 = PiezaSimple("Pieza 5")
    pieza6 = PiezaSimple("Pieza 6")
    pieza7 = PiezaSimple("Pieza 7")
    pieza8 = PiezaSimple("Pieza 8")
    pieza9 = PiezaSimple("Pieza 9")
    pieza10 = PiezaSimple("Pieza 10")
    pieza11 = PiezaSimple("Pieza 11")
    pieza12 = PiezaSimple("Pieza 12")
    pieza13 = PiezaSimple("Pieza 13")
    pieza14 = PiezaSimple("Pieza 14")

    subconjunto1 = SubConjunto("Sub-conjunto 1")
    subconjunto1.agregar(pieza1)
    subconjunto1.agregar(pieza2)
    subconjunto1.agregar(pieza3)
    subconjunto1.agregar(pieza4)

    subconjunto2 = SubConjunto("Sub-conjunto 2")
    subconjunto2.agregar(pieza5)
    subconjunto2.agregar(pieza6)
    subconjunto2.agregar(pieza7)
    subconjunto2.agregar(pieza8)

    subconjunto3 = SubConjunto("Sub-conjunto 3")
    subconjunto3.agregar(pieza9)
    subconjunto3.agregar(pieza10)
    subconjunto3.agregar(pieza11)
    subconjunto3.agregar(pieza12)

    subconjunto_opcional = SubConjunto("Sub-conjunto Opcional")
    subconjunto_opcional.agregar(pieza13)
    subconjunto_opcional.agregar(pieza14)

    producto = ProductoPrincipal("Producto Principal")
    producto.agregar_subconjunto(subconjunto1)
    producto.agregar_subconjunto(subconjunto2)
    producto.agregar_subconjunto(subconjunto3)

    print("Estructura sin subconjunto opcional:")
    producto.mostrar()

    producto.agregar_subconjunto(subconjunto_opcional)

    print("\nEstructura con subconjunto opcional:")
    producto.mostrar()
