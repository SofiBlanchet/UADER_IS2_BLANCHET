"""
getJason_v1_2.py - Versión refactorizada 1.2 con Patrón Cadena de Responsabilidad + Historial e Iterador

Copyright © 2024 UADER - FCyT - Ingeniería en Sistemas de Información
Todos los derechos reservados.

Este programa permite cargar saldos desde un archivo JSON,
realizar pagos balanceados automáticamente y listar el historial
cronológico utilizando un iterador personalizado.
"""

import os
import sys
import json
from abc import ABC, abstractmethod


class JsonReaderBase(ABC):
    @abstractmethod
    def cargar(self):
        pass

    @abstractmethod
    def obtener_valor(self, clave):
        pass


class JsonReaderSingleton(JsonReaderBase):
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, ruta_archivo=None):
        if not hasattr(self, 'inicializado'):
            self.ruta_archivo = ruta_archivo
            self.datos = {}
            self.inicializado = True

    def cargar(self):
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                self.datos = json.load(archivo)
        except FileNotFoundError:
            print(f"Error: El archivo '{self.ruta_archivo}' no fue encontrado.")
            sys.exit(4)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{self.ruta_archivo}' no tiene formato JSON válido.")
            sys.exit(6)
        except Exception as e:
            print(f"Error inesperado: {e}")
            sys.exit(7)

    def obtener_valor(self, clave):
        return self.datos.get(clave, f"La clave '{clave}' no se encontró en el archivo.")


class Banco:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.saldos = {}
        return cls._instancia

    def cargar_saldos(self, datos_dict):
        self.saldos = datos_dict.copy()

    def obtener_saldo(self, token):
        return self.saldos.get(token, 0)

    def tiene_saldo(self, token, monto):
        return self.saldos.get(token, 0) >= monto

    def debitar(self, token, monto):
        if self.tiene_saldo(token, monto):
            self.saldos[token] -= monto
            return True
        return False

    def mostrar_todos(self):
        return self.saldos.copy()


class PagoHandler:
    def __init__(self, banco):
        self._siguiente = None
        self._banco = banco

    def establecer_siguiente(self, siguiente):
        self._siguiente = siguiente
        return siguiente

    def manejar(self, monto, pedido_id):
        raise NotImplementedError()


class TokenHandler(PagoHandler):
    def __init__(self, banco, token):
        super().__init__(banco)
        self.token = token

    def manejar(self, monto, pedido_id):
        if self._banco.tiene_saldo(self.token, monto):
            self._banco.debitar(self.token, monto)
            return Pedido(pedido_id, self.token, monto, True)
        elif self._siguiente:
            return self._siguiente.manejar(monto, pedido_id)
        else:
            return Pedido(pedido_id, None, monto, False)


class Pedido:
    def __init__(self, pedido_id, token, monto, exito):
        self.pedido_id = pedido_id
        self.token = token
        self.monto = monto
        self.exito = exito

    def __str__(self):
        if self.exito:
            return f"Pedido #{self.pedido_id}: ✅ Pago de ${self.monto} desde {self.token}"
        else:
            return f"Pedido #{self.pedido_id}: ❌ Sin saldo suficiente para ${self.monto}"


class HistorialIterator:
    def __init__(self, historial):
        self._historial = historial
        self._indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice < len(self._historial):
            resultado = self._historial[self._indice]
            self._indice += 1
            return resultado
        raise StopIteration


class GestorPedidos:
    def __init__(self, handler_inicial):
        self.handler = handler_inicial
        self.historial = []
        self.contador = 1

    def realizar_pago(self, monto):
        pedido = self.handler.manejar(monto, self.contador)
        self.historial.append(pedido)
        self.contador += 1
        return str(pedido)

    def mostrar_historial(self):
        return "\n".join(str(p) for p in self)

    def __iter__(self):
        return HistorialIterator(self.historial)


def main():
    if '-v' in sys.argv or '--version' in sys.argv:
        print("Versión 1.2")
        sys.exit(0)

    if len(sys.argv) < 2:
        print("Uso: python getJason_v1_2.py <archivo_json>")
        sys.exit(2)

    archivo = sys.argv[1]
    if not archivo.endswith(".json"):
        print("Error: El archivo debe tener extensión .json")
        sys.exit(3)
    if not os.path.exists(archivo):
        print(f"Error: El archivo '{archivo}' no existe")
        sys.exit(4)

    lector = JsonReaderSingleton(archivo)
    lector.cargar()

    banco = Banco()
    banco.cargar_saldos({"token1": 1000, "token2": 2000})

    handler1 = TokenHandler(banco, "token1")
    handler2 = TokenHandler(banco, "token2")
    handler1.establecer_siguiente(handler2)

    gestor = GestorPedidos(handler1)

    print(gestor.realizar_pago(500))
    print(gestor.realizar_pago(1800))
    print(gestor.realizar_pago(300))
    print(gestor.realizar_pago(700))

    print("\nHistorial de pagos:")
    print(gestor.mostrar_historial())


if __name__ == "__main__":
    main()
