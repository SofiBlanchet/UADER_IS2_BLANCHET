
class Boton:
    def mostrar(self):
        pass

class Ventana:
    def abrir(self):
        pass


class BotonClaro(Boton):
    def mostrar(self):
        return "Botón con tema CLARO"

class BotonOscuro(Boton):
    def mostrar(self):
        return "Botón con tema OSCURO"

class VentanaClara(Ventana):
    def abrir(self):
        return "Ventana con fondo blanco"

class VentanaOscura(Ventana):
    def abrir(self):
        return "Ventana con fondo negro"


class TemaFactory:
    def crear_boton(self):
        pass

    def crear_ventana(self):
        pass

class TemaClaroFactory(TemaFactory):
    def crear_boton(self):
        return BotonClaro()

    def crear_ventana(self):
        return VentanaClara()

class TemaOscuroFactory(TemaFactory):
    def crear_boton(self):
        return BotonOscuro()

    def crear_ventana(self):
        return VentanaOscura()


def construir_interfaz(factory: TemaFactory):
    boton = factory.crear_boton()
    ventana = factory.crear_ventana()
    print(boton.mostrar())
    print(ventana.abrir())


tema = TemaOscuroFactory()
construir_interfaz(tema)

tema = TemaClaroFactory()
construir_interfaz(tema)
