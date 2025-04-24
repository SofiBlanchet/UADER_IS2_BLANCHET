class Impuestos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Impuestos, cls).__new__(cls)
        return cls._instancia

    def calcular_impuestos(self, base_imponible):
        if base_imponible < 0:
            raise ValueError("La base imponible no puede ser negativa.")

        iva = base_imponible * 1.21
        iibb = base_imponible * 1.05
        contribuciones = base_imponible * 1.012

        total_impuestos = iva + iibb + contribuciones
        return total_impuestos


impuestos = Impuestos()

base = 1000
total_impuestos = impuestos.calcular_impuestos(base)
print(f"Total de impuestos sobre {base} es: {total_impuestos}")
