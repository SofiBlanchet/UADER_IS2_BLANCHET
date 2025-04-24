class Factura:
    def __init__(self, importe):
        self.importe = importe

    def generar_factura(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class FacturaIVAResponsable(Factura):
    def generar_factura(self):
        iva = self.importe * 0.21
        total = self.importe + iva
        return (
            f"Factura A\n"
            f"Condición: IVA Responsable Inscripto\n"
            f"Importe neto: ${self.importe:.2f}\n"
            f"IVA (21%): ${iva:.2f}\n"
            f"Total: ${total:.2f}"
        )

class FacturaIVANoInscripto(Factura):
    def generar_factura(self):
        return (
            f"Factura C\n"
            f"Condición: IVA No Inscripto\n"
            f"Total: ${self.importe:.2f} (IVA excluido)"
        )

class FacturaIVAExento(Factura):
    def generar_factura(self):
        return (
            f"Factura C\n"
            f"Condición: IVA Exento\n"
            f"Total: ${self.importe:.2f} (con discriminación de IVA)"
        )

# modos de uso
factura1 = FacturaIVAResponsable(1000)
print(factura1.generar_factura())

factura2 = FacturaIVANoInscripto(1000)
print(factura2.generar_factura())

factura3 = FacturaIVAExento(1000)
print(factura3.generar_factura())
