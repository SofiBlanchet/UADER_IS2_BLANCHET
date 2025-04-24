class FactorialSingleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(FactorialSingleton, cls).__new__(cls)
        return cls._instancia

    def calcular_factorial(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


f1 = FactorialSingleton()
f2 = FactorialSingleton()

print(f1 is f2)  

print(f1.calcular_factorial(6))