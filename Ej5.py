import copy

class Componente:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Componente: {self.nombre}"

# Prototipo de avión
class Avion:
    def __init__(self, modelo):
        self.modelo = modelo
        self.body = None
        self.turbinas = []
        self.alas = []
        self.tren_aterrizaje = None

    def agregar_body(self, body):
        self.body = body

    def agregar_turbinas(self, turbina):
        self.turbinas = [copy.deepcopy(turbina) for _ in range(2)]

    def agregar_alas(self, ala):
        self.alas = [copy.deepcopy(ala) for _ in range(2)]

    def agregar_tren_aterrizaje(self, tren):
        self.tren_aterrizaje = tren

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar_componentes(self):
        return (
            f"Modelo: {self.modelo}\n"
            f"Body: {self.body}\n"
            f"Turbinas: {[str(t) for t in self.turbinas]}\n"
            f"Alas: {[str(a) for a in self.alas]}\n"
            f"Tren de aterrizaje: {self.tren_aterrizaje}"
        )

prototipo_avion = Avion("Boeing 737")
prototipo_avion.agregar_body(Componente("Fuselaje estándar"))
prototipo_avion.agregar_turbinas(Componente("Turbina GE"))
prototipo_avion.agregar_alas(Componente("Ala de 35m"))
prototipo_avion.agregar_tren_aterrizaje(Componente("Tren de aterrizaje reforzado"))


avion_personalizado = prototipo_avion.clonar()
avion_personalizado.modelo = "Boeing 737 Max"


print("Prototipo original:\n")
print(prototipo_avion.mostrar_componentes())

print("\nAvión clonado y personalizado:\n")
print(avion_personalizado.mostrar_componentes())
