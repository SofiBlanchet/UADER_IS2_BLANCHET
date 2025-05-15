class IteradorCadena:
    def __init__(self, cadena, reverso=False):
        self.cadena = cadena
        self.reverso = reverso
        self.posicion = len(cadena) - 1 if reverso else 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.reverso:
            if self.posicion < 0:
                raise StopIteration
            caracter = self.cadena[self.posicion]
            self.posicion -= 1
            return caracter
        else:
            if self.posicion >= len(self.cadena):
                raise StopIteration
            caracter = self.cadena[self.posicion]
            self.posicion += 1
            return caracter


class ColeccionCadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def iterador_directo(self):
        return IteradorCadena(self.cadena, reverso=False)

    def iterador_reverso(self):
        return IteradorCadena(self.cadena, reverso=True)


coleccion = ColeccionCadena("hola")

print("Directo:")
for c in coleccion.iterador_directo():
    print(c)

print("Reverso:")
for c in coleccion.iterador_reverso():
    print(c)
