class CartaFlyweight:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def mostrar(self, estado_extrinseco):
        print(f"{self.valor} de {self.palo} - {estado_extrinseco}")


class CartaFlyweightFactory:
    def __init__(self):
        self.carta_cache = {}

    def obtener_carta(self, valor, palo):
        clave = f"{valor} de {palo}"
        if clave not in self.carta_cache:
            self.carta_cache[clave] = CartaFlyweight(valor, palo)
        return self.carta_cache[clave]


if __name__ == "__main__":
    factory = CartaFlyweightFactory()

    carta1 = factory.obtener_carta("As", "Espadas")
    carta2 = factory.obtener_carta("Rey", "Corazones")
    carta3 = factory.obtener_carta("As", "Espadas")  

    carta1.mostrar("Posición en la mesa: (0, 0), Boca arriba")
    carta2.mostrar("Posición en la mesa: (1, 0), Boca abajo")
    carta3.mostrar("Posición en la mesa: (2, 0), Boca arriba")
