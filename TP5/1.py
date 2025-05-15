class Manejador:
    def __init__(self):
        self.siguiente = None

    def establecer_siguiente(self, manejador):
        self.siguiente = manejador
        return manejador

    def manejar(self, numero):
        if self.siguiente:
            self.siguiente.manejar(numero)
        else:
            print(f"Número {numero} no consumido.")


class ManejadorPar(Manejador):
    def manejar(self, numero):
        if numero % 2 == 0:
            print(f"Número {numero} consumido por ManejadorPar.")
        else:
            super().manejar(numero)


class ManejadorPrimo(Manejador):
    def es_primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def manejar(self, numero):
        if self.es_primo(numero):
            print(f"Número {numero} consumido por ManejadorPrimo.")
        else:
            super().manejar(numero)


manejador_par = ManejadorPar()
manejador_primo = ManejadorPrimo()
manejador_final = Manejador()

manejador_par.establecer_siguiente(manejador_primo).establecer_siguiente(manejador_final)

for i in range(1, 101):
    manejador_par.manejar(i)
