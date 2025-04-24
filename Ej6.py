import copy

class Prototipo:
    def clonar(self):
        return copy.deepcopy(self)


class Documento(Prototipo):
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def mostrar(self):
        return f"Título: {self.titulo}\nContenido: {self.contenido}"


original = Documento("Factura", "Este es el contenido de la factura.")
copia1 = original.clonar()
copia2 = copia1.clonar()

print("Original:")
print(original.mostrar())
print("\nCopia 1:")
print(copia1.mostrar())
print("\nCopia 2 (copia de la copia):")
print(copia2.mostrar())


print("\n¿Copia1 es el mismo objeto que Original?", copia1 is original)
print("¿Copia2 es el mismo objeto que Copia1?", copia2 is copia1)
