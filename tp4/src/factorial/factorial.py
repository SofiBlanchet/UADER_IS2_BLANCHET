#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print(f"El factorial de un número negativo ({num}) no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1:
    rango = input("Debe ingresar un rango (por ejemplo: -10 o 20-): ")
else:

    rango = sys.argv[1]

if '-' in rango:
    if rango.startswith('-'):
        try:
            fin = int(rango[1:])
            if fin <= 0:
                print("El número debe ser mayor que 0.")
                sys.exit()
            for num in range(1, fin + 1):
                print(f"El factorial de {num} es {factorial(num)}")
        except ValueError:
            print("Por favor, ingrese un número válido después de '-' (ej. -10).")
            sys.exit()
    elif rango.endswith('-'):
        try:
            inicio = int(rango[:-1])
            if inicio < 1 or inicio > 60:
                print("El número debe estar entre 1 y 60.")
                sys.exit()
            for num in range(inicio, 61):
                print(f"El factorial de {num} es {factorial(num)}")
        except ValueError:
            print("Por favor, ingrese un número válido antes de '-' (ej. 20-).")
            sys.exit()
    else:
        print("El formato no es válido. Debe ser '-hasta' o 'desde-' (ej. -10 o 20-).")
        sys.exit()
else:
    print("El argumento debe tener el formato correcto ('-hasta' o 'desde-').")
    sys.exit()
