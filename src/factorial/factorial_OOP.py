#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        """Constructor que puede ser usado para inicializar variables si fuera necesario."""
        pass

    def calcular_factorial(self, num):
        """Método para calcular el factorial de un número dado."""
        if num < 0:
            print(f"El factorial de un número negativo ({num}) no existe.")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min, max):
        """Método que calcula los factoriales entre min y max (inclusive)."""
        if min > max:
            print("El rango no es válido. Asegúrese de que min <= max.")
            return
        for num in range(min, max + 1):
            print(f"El factorial de {num} es {self.calcular_factorial(num)}")


if __name__ == "__main__":

    rango = input("Ingrese el rango (por ejemplo: 4-8): ")

    try:
        min_value, max_value = map(int, rango.split('-'))
        
        factorial_obj = Factorial()
        factorial_obj.run(min_value, max_value)
    except ValueError:
        print("Por favor, ingrese un rango válido en el formato 'min-max'.")
