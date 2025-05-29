# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: old_primes.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-05-06 18:42:35 UTC (1746556955)
# Reusar el programa asegurando que puede recuperarse números hasta 
# el número indicado como parámetro.

import os
import sys

lower = 1
upper = 50

os.system('cls')

try:
    if len(sys.argv) == 1:
        lower = 1
        upper = 50
    elif len(sys.argv)==2:
        lower=1
        upper= int(sys.argv[1])
    elif len(sys.argv)>=3:
        lower= int(sys.argv[1])
        upper=int(sys.argv[2])
except:
    print ("Argumento inválido")
    exit()


print('Números primos entre %d y %d son:\n' % (lower, upper))

if lower > upper:
    print("por favor ingrese nuevamente dos valores")
    exit()

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print('%d' % num)
