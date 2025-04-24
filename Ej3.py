class Hamburguesa:
    def __init__(self, tipo_entrega):
        self.tipo_entrega = tipo_entrega

    def entregar(self):
        if self.tipo_entrega == "mostrador":
            print("La hamburguesa ha sido entregada en el mostrador.")
        elif self.tipo_entrega == "retirada":
            print("La hamburguesa está lista para ser retirada por el cliente.")
        elif self.tipo_entrega == "delivery":
            print("La hamburguesa será enviada por delivery.")
        else:
            print("Método de entrega no reconocido.")

# de las formas que se podria usar
hamburguesa_mostrador = Hamburguesa("mostrador")
hamburguesa_mostrador.entregar()

hamburguesa_retirada = Hamburguesa("retirada")
hamburguesa_retirada.entregar()

hamburguesa_delivery = Hamburguesa("delivery")
hamburguesa_delivery.entregar()
