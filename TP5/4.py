import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

class MemoriaState:
    def __init__(self, memorias):
        self.memorias = memorias
        self.pos = 0

    def scan(self):
        for etiqueta, (tipo, frecuencia) in self.memorias.items():
            print(f"Sintonizando... Memoria {etiqueta}: {frecuencia} {tipo}")

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

        self.memorias = {
            "M1": ("AM", "1380"),
            "M2": ("FM", "89.1"),
            "M3": ("AM", "1510"),
            "M4": ("FM", "103.9")
        }
        self.memoria_state = MemoriaState(self.memorias)

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()
        self.memoria_state.scan()

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
