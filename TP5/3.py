class Observador:
    def __init__(self, id_unico):
        self.id_unico = id_unico

    def actualizar(self, id_emitido):
        if self.id_unico == id_emitido:
            print(f"Observador {self.id_unico} recibió su ID.")


class Sujeto:
    def __init__(self):
        self.observadores = []

    def agregar(self, observador):
        self.observadores.append(observador)

    def emitir_id(self, id_emitido):
        print(f"ID emitido: {id_emitido}")
        for observador in self.observadores:
            observador.actualizar(id_emitido)


observador1 = Observador("AB12")
observador2 = Observador("CD34")
observador3 = Observador("EF56")
observador4 = Observador("GH78")

sujeto = Sujeto()
sujeto.agregar(observador1)
sujeto.agregar(observador2)
sujeto.agregar(observador3)
sujeto.agregar(observador4)

ids_a_emitir = ["XY99", "AB12", "CD34", "ZZ00", "EF56", "GH78", "LM10", "MN20"]

for id_actual in ids_a_emitir:
    sujeto.emitir_id(id_actual)
