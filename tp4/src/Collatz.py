#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

def collatz_iterations(n):
    """Calcula el número de iteraciones hasta que el número n converja a 1 usando la conjetura de Collatz."""
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2 
        else:
            n = 3 * n + 1 
        iterations += 1
    return iterations

def generate_collatz_data(limit):
    """Genera los números n entre 1 y limit con sus respectivos números de iteraciones."""
    data = []
    for n in range(1, limit + 1):
        iterations = collatz_iterations(n)
        data.append((n, iterations))
    return data


limit = 10000
data = generate_collatz_data(limit)


for n, iterations in data:
    print(f"El número {n} necesita {iterations} iteraciones para converger a 1.")
