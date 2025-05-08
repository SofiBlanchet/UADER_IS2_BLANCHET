from abc import ABC, abstractmethod

class Numero(ABC):
    @abstractmethod
    def obtener_valor(self):
        pass

class NumeroBase(Numero):
    def __init__(self):
        self.valor = float(input("Ingrese un número: "))

    def obtener_valor(self):
        return self.valor

class DecoradorNumero(Numero):
    def __init__(self, numero: Numero):
        self.numero = numero

    def obtener_valor(self):
        return self.numero.obtener_valor()

class Sumar2(DecoradorNumero):
    def obtener_valor(self):
        return self.numero.obtener_valor() + 2

class MultiplicarPor2(DecoradorNumero):
    def obtener_valor(self):
        return self.numero.obtener_valor() * 2

class DividirPor3(DecoradorNumero):
    def obtener_valor(self):
        return self.numero.obtener_valor() / 3

if __name__ == "__main__":
    numero = NumeroBase()
    print(f"Valor original: {numero.obtener_valor()}")

    numero_con_suma = Sumar2(numero)
    print(f"Después de sumarle 2: {numero_con_suma.obtener_valor()}")

    numero_con_multiplicacion = MultiplicarPor2(numero_con_suma)
    print(f"Después de multiplicar por 2: {numero_con_multiplicacion.obtener_valor()}")

    numero_con_division = DividirPor3(numero_con_multiplicacion)
    print(f"Después de dividir por 3: {numero_con_division.obtener_valor()}")

    numero_anidado = DividirPor3(MultiplicarPor2(Sumar2(NumeroBase())))
    print(f"Operaciones anidadas: {numero_anidado.obtener_valor()}")
