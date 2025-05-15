from abc import ABC, abstractmethod

class Laminador(ABC):
    @abstractmethod
    def producir(self, ancho: float, espesor: float):
        pass

class TrenLaminador5m(Laminador):
    def producir(self, ancho: float, espesor: float):
        print(f"[Tren 5m] Produciendo lámina de 5 metros, {ancho} m de ancho, {espesor}\" de espesor.")

class TrenLaminador10m(Laminador):
    def producir(self, ancho: float, espesor: float):
        print(f"[Tren 10m] Produciendo lámina de 10 metros, {ancho} m de ancho, {espesor}\" de espesor.")

class Lamina:
    def __init__(self, ancho: float, espesor: float, laminador: Laminador):
        self.ancho = ancho
        self.espesor = espesor
        self.laminador = laminador

    def producir(self):
        print("[Lamina] Iniciando producción...")
        self.laminador.producir(self.ancho, self.espesor)


if __name__ == "__main__":
    tren5 = TrenLaminador5m()
    tren10 = TrenLaminador10m()

    lamina1 = Lamina(1.5, 0.5, tren5)
    lamina2 = Lamina(1.5, 0.5, tren10)

    lamina1.producir()
    lamina2.producir()
